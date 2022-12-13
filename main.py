# Chemin dossier contenant l'ensemble des textes, vérifier si ce dossier existe et si celui-ci contient des fichiers
# -*- coding: utf-8 -*-

import os, sys, collections, wget, re, json

path = './/venv//fichier_projet/'

# list of links about soupe
def set_soupe():
    return { "chaudrée" : "https://fr.wikipedia.org/w/index.php?title=Chaudr%C3%A9e&action=raw",
            "soupeaufromage" : "https://fr.wikipedia.org/w/index.php?title=Soupe_au_fromage&action=raw",
            "oukha" : "https://fr.wikipedia.org/w/index.php?title=Oukha&action=raw",
            "bourride" : "https://fr.wikipedia.org/w/index.php?title=Bourride&action=raw",
            "gaspacho" : "https://fr.wikipedia.org/w/index.php?title=Gaspacho&action=raw",
            "bortsch" : "https://fr.wikipedia.org/w/index.php?title=Bortsch&action=raw",
            "garbure" : "https://fr.wikipedia.org/w/index.php?title=Garbure&action=raw"}

# download the soupe reference
def take_soupe(sousoupe, path_dir):
    ite = 1
    for cle,valeur in sousoupe.items():
        print("download fichier " + str(ite))
        op = str(path_dir + "//" + cle)
        ite += 1
        wget.download(valeur, out=op)

# test if the folder is empty and download if not
def verification(list_s):
    if os.path.isdir(path):
        if not os.listdir(path):
            print("Le dossier est vide")
            take_soupe(list_s, "D://Bureau//projet_python//projet_cours//venv//fichier_projet")
        else:
            print("Le dossier contient des fichiers")
    else:
        print("Le dossier n'existe pas")

# Open each documents with a for to put the texts in list by sentences and clean the text raw
def clean_raw_file(files):
    text_list = {}
    for filename in os.listdir(files):
        with open(os.path.join(files, filename), 'r', encoding='utf8') as f:
            string_dec = f.read()

            try:
                myregex = re.findall(r'\n \|.*', string_dec)
                for m in range(len(myregex)):
                    string_dec = string_dec.replace(myregex[m], "")
            except TypeError:
                print("no regexfind")

            characters = "{}[]=\"\\'!?|*</:>«»()"
            for x in range(len(characters)):
                string_dec = string_dec.replace(characters[x], "")

            list_extension = [".jpg",".htlm",".png",".pdf",".org",".com",".bnf",".geo"]
            for x in range(len(list_extension)):
                string_dec = string_dec.replace(list_extension[x], "")

            list_mot_exclu = ["histoire", "lemonde", "souvent" , "(poisson)", "ouvrage", "roman", "citation", "département", "éditeur", "pages", "google", 'books', "ligne", "consulté", "servi", "vignette", "auteur", "éditeur", "année", "ainsi", "Fichier", "aussi", "était", "Infobox", "titre", "cette", "article", "ladepeche", "https", "toujours", "comme", "online", "gallery"]
            for x in range(len(list_mot_exclu)):
                string_dec = string_dec.replace(list_mot_exclu[x], "")

            try:
                myregex = re.search(r'Notes et références(.*\n*)*', string_dec)
                res = string_dec
                res = res.replace(myregex.group(0), "")
            except AttributeError:
                res = string_dec

            lines = res.split(".")
            text_list[filename] = lines

    return text_list

# Returned a list of all the words with more than 4 characters and more than 4 apparitions
def index_and_delete_inf_4(list_words):
    tmp_val = []
    tmp_list = []
    for cle,valeur in list_words.items():
        for k in range(len(valeur)):
            tmp_val = list_words[cle][k].split() + tmp_val
    for i in range(len(tmp_val)):
        compteur = (tmp_val.count(tmp_val[i]))
        if ((compteur>4)&(tmp_val[i].lower() not in tmp_list)&(len(tmp_val[i])>4)):
            tmp_list.append(tmp_val[i].lower())
    return(tmp_list)

#Returned a dict with a key of the keyword and a list of iteration of the sentences wich use it
#Returned a list with all the sentences in it
def display_index_dict(dict_index, list_words):
    dict_to_list = []
    dico_final = {}
    for cle, valeur in dict_index.items():
        dict_to_list = dict_to_list + valeur
        for word in list_words:
            new_word_for_dict = []
            sentence_place_ite = 0
            for sentence in dict_to_list:
                if ((word != None) & (word.lower() in sentence.lower())):
                    new_word_for_dict.append(sentence_place_ite)
                sentence_place_ite+=1
            dico_final[word] = new_word_for_dict
    return(dico_final, dict_to_list)

# Use the dict of wikipedia data and check if exist or not, if not create, else pass to the next sequence
# Clean the raw file and then get a list of all the words with more than 4 characters and more than 4 apparitions
# Create a dict with the results and the list of sentences and register in files
if __name__ == '__main__':

    list_of_soupe = set_soupe()
    verification(list_of_soupe)

    dict_of_words = clean_raw_file(path)
    list_of_words_more4 = (index_and_delete_inf_4(dict_of_words))
    resfinal, dico_sentence = display_index_dict(dict_of_words, list_of_words_more4)

    #display the dict and the key words
    print(resfinal)
    for cle,valeur in resfinal.items():
        print(cle)

    tf = open("myDictionary.json", "w")
    json.dump(resfinal, tf)
    tf.close()

    tf2 = open("mySentences.json", "w")
    json.dump(dico_sentence, tf2)
    tf2.close()