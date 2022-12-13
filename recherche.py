import sys
import json

if __name__ == '__main__':
    data_param = []
    for arg in sys.argv:
        data_param.append(arg)

    tf = open("myDictionary.json", "r")
    new_dict = json.load(tf)

    tf2 = open("mySentences.json", "r")
    new_sentences = json.load(tf2)

    for param in data_param:
        if ((param!='recherche.py')&(param in new_dict)):
            print('')
            print(" ****************** Le Paramètre " + str(param) + " est trouvé ******************")
            print('')
            for sentence in new_dict[param]:
                print(" -------------- PHRASE " + str(sentence) +" --------------")
                print(new_sentences[sentence])
