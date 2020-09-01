import json
from difflib import get_close_matches
from time import sleep

data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys(),cutoff=0.7)) > 0 :
        yn= input("did you mean {} ? if yes enter y else enter n: " . format(get_close_matches(w,data.keys())[0])) 
        if yn == "y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "n":
            return "word doesnt exist"
        else:
            return "input not recognised"       
    else:
        return "the word doesn't exist"    

word = input("enter a word: ") 
op=translate(word)

if type(op)==list:
    for item in op:
        print(item)
else:
    print(op)        


sleep(5)