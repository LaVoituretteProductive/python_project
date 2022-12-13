import sys

import json



if __name__ == '__main__':
    for arg in sys.argv:
        print(arg)

    tf = open("myDictionary.json", "r")
    new_dict = json.load(tf)
    print(new_dict)

