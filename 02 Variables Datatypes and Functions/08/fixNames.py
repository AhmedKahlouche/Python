import os
import string
# list of illegal characters in a name of a file
illegaleChars = ["/","?","<",">","\\",":","*","|","\""]
#rename files to have an ordered listdir
def fixNumbering(fileName):
    index = list(a for a,b in enumerate(fileName) if b in string.digits)
    if len(index) == 2:
        return fileName[:int(index[0])]+ "00" + fileName[int(index[0]):]
    elif len(index) == 3:
        return fileName[:int(index[0])]+ "0" + fileName[int(index[0]):]
    else:
        return fileName

for i in os.listdir():
    if i[:3] == "Mes":
        #print(i,"-->",fixNumbering(i))
        os.rename(i,fixNumbering(i))
# Get all files and folders from the path program
filesInFolder = []
for i in os.listdir() :
    filesInFolder.append(i)
# Filter Folders from the list of filesInFolder
def testFunc(a):
    return not os.path.isdir(os.getcwd()+'\\'+a)
filesInFolder = list(filter(testFunc,filesInFolder))
# Filter out the files that do not end with ".mp4"

for file in filesInFolder:
    if not file.casefold().endswith('mp4'):
        filesInFolder.remove(file)
# dont know why it happens but "fixNames.py" doesnt get eleminated
if "fixNames.py" in filesInFolder:
    filesInFolder.remove("fixNames.py")
# construct path and open the file that contains the names
filePath = os.getcwd()+"\\names.txt"
fp = open(filePath,'r',encoding='utf-8')
# Read each line as a list item
namesList = fp.readlines()

for i in range(len(namesList)) :
    # Clean the names and add the number
    namesList[i] = "{0:0=3d}.".format(i+1) + namesList[i].strip()[:-6] + ".mp4"
    # Check if the names are legal otherwise replace by "-"
    replaceIndex = list(a for a,b in enumerate(namesList[i]) if b in illegaleChars)
    for index in replaceIndex :
        namesList[i] = namesList[i][:index] + "-" + namesList[i][index+1:]

# Renaming the files
for i in range(namesList.__len__()):
    print(filesInFolder[i] , "-->" , namesList[i])
    os.rename(filesInFolder[i],namesList[i])
