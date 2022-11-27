# Chemin dossier contenant l'ensemble des textes, vérifier si ce dossier existe et si celui-ci contient des fichiers
# -*- coding: utf-8 -*-

import os, sys, collections, wget, re

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

            pattern1 = r'}}\n\[\[(.*\n*)*'
            #print(f.read())
            #print(len(f.read()))
            #print(f.read())
            print(re.findall(r"}}\n\[\[(.*\n*)*", f.read())) # pas possible il faut retirer toute la box de infot met pour ensuite pouvoir traiter le fichier

            #re.sub(pattern, '', org_string)

            lines = f.read().split(".")
            lines.append([item.split(" ") for item in lines])



            # regex supprimer la fin de la sélection après les réferences ^\n(== Notes et références ==)(.*\n*)*


            # prendre après l'infobox }}\n\[\[(.*\n*)*
            #retirer le début [^\}}\n[[](.*\n*)*
            #reboucler pour trier les espaces et les \n du raw par phrases dégagées pour attraper les mots
            #lines = lines.split("\n")
            # lines = lines.split(" ")
            #lines = f.read().split(" ")
            text_list[filename] = lines
            #print(len(text_list))
            print((text_list))

    return text_list

# Pour chaque documents, on va chercher à compter la fréquence des mots pour former un dictionnaire étant l'index des documents
# supprimer tous les mots ayant quatre ou moins de quatre lettres (c'est un peu brutal mais cela fonctionne assez bien), puis pour chaque mot d'un document, calculer sa fréquence par rapport à la fréquence de ce mot dans l'ensemble des documents du dossier dans lequel il se trouve : c'est l'heuristique du TF.IDF (term frequency inverse documentfreuency) => un mot est remarquable si sa fréquence dans un document est bien supérieure à sa fréquence dans le sous-corpus (mais cette heuristique ne fonctionne bien que si le corpus est assez grand).
# L'index sera un dictionnaire, qui sera propre (dans un fichier) pour éviter de recharger à chaque fois l'index
def delete_inf_4(list_words):
    test = []
    for cle,valeur in list_of_words.items():
        ite=0
        #print(valeur)
        for i in valeur:
            if len(i)>4:
                test.append(valeur[ite])
            ite+=1
        #print(test)
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
    list_of_words = text_in_list(path)
    #print(list_of_words)
    delete_inf_4(list_of_words)





















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