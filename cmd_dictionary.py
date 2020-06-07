import json
from difflib import get_close_matches

def closeMatches(patterns, word): 
    nearest =get_close_matches(word, patterns.keys())
    if(len(nearest) != 0):
        print("\n\tThis is not an English word...\n\tDid you mean: \t")
        for item in nearest:
            print("\t" + item)
    else:
        print("\n\tThis is neither an English word nor it matches\n\tto any closest word in our Dictionary\n")
    


def translate(word):
    if word in load:
        return (load[word])
    elif word.title() in load:
        return (load[word.title()])
    elif word.upper() in load:
        return (load[word.upper()])
    else:
        closeMatches(load, word)
        return 0

if __name__ == "__main__":
    while (True):
        load = json.load(open("original.json"))
        word = input("\t---Enter a keyword to search---\n\t---or Enter 'q' to quit---\t")
        if word==  "q":
            break
        else:
            x = translate(word)
            if(x == 0):
                continue
            else:
                leng = len(x)
                if leng> 1:
                    print("\t There are more than one meanings to this word....and those are:\n")
                    for i in range(leng):
                        print("\n\t{}) {}\n".format(i+1,x[i]))
                else:
                    for i in range(leng):
                        print("\n\t{}\n".format(x[i]))