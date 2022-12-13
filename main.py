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

# test if the folder is empty
def verification(list_s):
    if os.path.isdir(path):
        if not os.listdir(path):
            print("Le dossier est vide")
            take_soupe(list_s, "D://Bureau//projet_python//projet_cours//venv//fichier_projet")
        else:
            print("Le dossier contient des fichiers")
    else:
        print("Le dossier n'existe pas")

# Ouvrir chaque documents avec une boucle et mettre les textes dans des listes phrases par phrases
def text_in_list(files):
    text_list = {}
    for filename in os.listdir(files):
        with open(os.path.join(files, filename), 'r', encoding='utf8') as f:

            string_dec = f.read()
            #print(string_dec)
            try:
                """
                myregex = re.search(r'\n \|.*', string_dec)
                for i in range(myregex):
                    string_dec = string_dec.replace(myregex.group(i), " ")
                print(myregex)
                """
                #pattern = re.compile(r'\n \|.*')
                myregex = re.findall(r'\n \|.*', string_dec)
                #print(len(myregex))
                for m in range(len(myregex)):
                    #print(myregex[m])
                    string_dec = string_dec.replace(myregex[m], " ")
                #print(string_dec)

            except TypeError:
                print("no regexfind")

            characters = "{}[]=\"\\'!?|*</:>«»"
            for x in range(len(characters)):
                string_dec = string_dec.replace(characters[x], " ")
            #print(type(string_dec))

            string_dec = string_dec.replace(".jpg", " ")
            string_dec = string_dec.replace(".html", " ")
            string_dec = string_dec.replace(".png", " ")
            string_dec = string_dec.replace(".pdf", " ")
            string_dec = string_dec.replace(".org", " ")
            string_dec = string_dec.replace(".com", " ")
            string_dec = string_dec.replace(".bnf", " ")
            string_dec = string_dec.replace(".geo", " ")





            try:
                myregex = re.search(r'Notes et références(.*\n*)*', string_dec)
                res = string_dec
                res = res.replace(myregex.group(0), "")
                # print("".join((myregex.group(0))))
                # res = "".join(myregex).replace(res, "")
                #print(res)
            except AttributeError:
                print("no value")
                res = string_dec

            lines = res.split(".")
            #print(len(lines))
            #print(lines)
            #lines.append([item.split(" ") for item in lines])
            text_list[filename] = lines
            # print(len(text_list))
            # print((text_list))

    return text_list

    '''
            #re.sub(pattern, '', org_string)
            #lines = string_dec.split(".")
            #lines.append([item.split(" ") for item in lines])
            # regex supprimer la fin de la sélection après les réferences ^\n(== Notes et références ==)(.*\n*)*
            # prendre après l'infobox }}\n\[\[(.*\n*)*
            #retirer le début [^\}}\n[[](.*\n*)*
            #reboucler pour trier les espaces et les \n du raw par phrases dégagées pour attraper les mots
            
            #lines = lines.split("\n")
            # lines = lines.split(" ")
            #lines = f.read().split(" ")
            text_list[filename] = lines
            #print(len(text_list))
            #print((text_list))
        # return text_list
    '''

# Pour chaque documents, on va chercher à compter la fréquence des mots pour former un dictionnaire étant l'index des documents
# supprimer tous les mots ayant quatre ou moins de quatre lettres (c'est un peu brutal mais cela fonctionne assez bien), puis pour chaque mot d'un document, calculer sa fréquence par rapport à la fréquence de ce mot dans l'ensemble des documents du dossier dans lequel il se trouve : c'est l'heuristique du TF.IDF (term frequency inverse documentfreuency) => un mot est remarquable si sa fréquence dans un document est bien supérieure à sa fréquence dans le sous-corpus (mais cette heuristique ne fonctionne bien que si le corpus est assez grand).
# L'index sera un dictionnaire, qui sera propre (dans un fichier) pour éviter de recharger à chaque fois l'index
def delete_inf_4(list_words):
    tmp_val = []
    tmp_list = []
    for cle,valeur in list_words.items():
        for k in range(len(valeur)):
            tmp_val = list_words[cle][k].split() + tmp_val
    #print(tmp_val)
    for i in range(len(tmp_val)):
        compteur = (tmp_val.count(tmp_val[i]))
        #print(compteur)
        if ((compteur>4)&(tmp_val[i] not in tmp_list)&(len(tmp_val[i])>4)):
            #print(len(tmp_val[i]))
            #print(tmp_val[i])
            tmp_list.append(tmp_val[i])

    """
    for cle,valeur in list_of_words.items():
        for m in range(len(valeur)):
            myregex = re.findall(r'[^ ]*', valeur[m])
            #tmp_val = list_words[cle][m].split(" ")
            for j in range(len(myregex)):
                if ((len(myregex[j]) < 4)&(len(myregex[j]) > 0)):
                    print(list_words[cle][m])
                    list_words[cle][m] = list_words[cle][m].replace(myregex[j], " ")
    """
    return(tmp_list)

def index_function(dict_index, list_words):
    dict_to_list = []
    dico_final = {}
    for cle, valeur in dict_index.items():
        dict_to_list = dict_to_list + valeur
        for j in list_words:
            new_word = []
            tmp_len = 0
            for k in dict_to_list:
                if ((j != None) & (j in k)):
                    new_word.append(tmp_len)
                    #print("found!")
                tmp_len+=1
            dico_final[j] = new_word
    return(dico_final)




    '''
    #new_list = [item for item in list_words if len(list_words) < 4]
    def top5_words(new_list):
        counts = collections.Counter()
        return counts.most_common(5)
    '''

# Pour chaque liste, on va parcourir les phrases et faire afficher le fichier et chaque phrases contenant les termes du dictionnaire et compter le nombre de mots matcher par phrases

# On va avoir ce format de lancement projet.py cèpe champignons, on doit passer des termes qui peuvent être potentiellement de l'index

# Press the green button in the gutter to run the script.

if __name__ == '__main__':

    list_of_soupe = set_soupe()
    verification(list_of_soupe)
    dict_of_words = text_in_list(path)
    #print(list_of_words['bortsch'])
    #print(len(list_of_words['bortsch']))
    list_of_words_more4 = (delete_inf_4(dict_of_words))
    #print((list_of_words_more4))
    resfinal = index_function(dict_of_words, list_of_words_more4)





















'''
# list of links about soupe
def set_soupe():
    return ["https://fr.wikipedia.org/w/index.php?title=Chaudr%C3%A9e&action=raw",
            "https://fr.wikipedia.org/w/index.php?title=Soupe_au_fromage&action=raw",
            "https://fr.wikipedia.org/w/index.php?title=Oukha&action=raw",
            "https://fr.wikipedia.org/w/index.php?title=Bourride&action=raw",
            "https://fr.wikipedia.org/w/index.php?title=Gaspacho&action=raw",
            "https://fr.wikipedia.org/w/index.php?title=Bortsch&action=raw",
            "https://fr.wikipedia.org/w/index.php?title=Garbure&action=raw"]

# download the soupe reference
def take_soupe(sousoupe, path_dir):
    ite = 1
    for name in sousoupe:
        print("download fichier " + str(ite))
        op = str(path_dir + "//fichier" + str(ite))
        ite += 1
        wget.download(name, out=op)

# test if the folder is empty
def verification(list_s):
    if os.path.isdir(path):
        if not os.listdir(path):
            print("Le dossier est vide")
            take_soupe(list_s, "D://Bureau//projet_python//projet_cours//venv//fichier_projet")
        else:
            print("Le dossier contient des fichiers")
    else:
        print("Le dossier n'existe pas")

# Ouvrir chaque documents avec une boucle et mettre les textes dans des listes phrases par phrases
def text_in_list(files):
    text_list = []
    for filename in os.listdir(files):
        with open(os.path.join(files, filename), 'r', encoding='utf8') as f:
            lines = f.read().split(" ")
            text_list.append(lines)
            #print(delete_inf_4(lines))
            #lines = [filename.split(" ") for filename in f]
            #lines = [line.rstrip('\n') for line in f]
    return text_list
'''