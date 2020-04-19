"""
This Program takes a word and returns its definition
"""
# import libraries and others used in this program
import json
from difflib import get_close_matches
# Load the data.json database into data variable
data = json.load(open('data.json'))

def getDef(word,i=0):
    """This Function looks for the word in the dict and returns its difinition"""
    if i == 0:
        word = word.lower()
        if data.__contains__(word):
            for idx in range(data[word].__len__()):
                print(str(idx+1)+". ",data[word][idx])
        elif get_close_matches(word,data.keys()).__len__():
            print('the word',word,"was not found, do you mean one of the following")
            for idx in range(get_close_matches(word,data.keys()).__len__()):
                print(str(idx+1)+". "+get_close_matches(word,data.keys())[idx])
            getDef(word,int(input("choose the number of desired word, or -1 to exit: ")))
        else:
            return "Word does not exist, bye idiot"
    elif i <= -1 :
        print("exiting the program, goodbye")
    else :
        print("you have chossen the word:",get_close_matches(word,data.keys())[i-1],
              ", here are its deffinitions")
        for idx in range(data[get_close_matches(word,data.keys())[i-1]].__len__()):
            print(str(idx+1)+". "+ data[get_close_matches(word,data.keys())[i-1]][idx])
        return
# this part of the code is only run if the program is executed as a script
if __name__ == "__main__":
    print(getDef(input("Enter a Word: ")))
    # print("this is it, have fun idiot")
