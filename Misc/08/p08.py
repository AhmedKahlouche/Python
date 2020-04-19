"""
This Program reads all files that end with .txt in the same folder as the Program
and appends their contents to a new file names with the date of execution
"""
import os
import datetime

# Get all files and folders from the path program
filesInFolder = os.listdir()

# Filter Folders from the list of filesInFolder
def testFunc(a):
    return not os.path.isdir(os.getcwd()+'\\'+a)
filesInFolder = list(filter(testFunc,filesInFolder))

# Filter the files that doesnt end with .txt
for file in filesInFolder:
    if not file.casefold().endswith('.txt'):
        filesInFolder.remove(file)
# Read the contents of the files into the list allFilesContents
allFilesContents = []
for file in filesInFolder:
    with open(file,'r') as fileHanler:
        allFilesContents.append(fileHanler.read())

# Create a new file with the name of the date and put all
# contents of allFilesContents inside it
newFileName = datetime.datetime.now().strftime('%Y-%m-%d')
with open(newFileName+".txt",'wt') as newFileHandler:
    for item in allFilesContents:
        newFileHandler.write(item+"\n")

print(allFilesContents)
