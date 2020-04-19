import os

# Get all files and folders from the path program
filesInFolder = ["017.Les procédures.mp4","018.Les fonctions.mp4"]
#print(filesInFolder)

for i in os.listdir() :
    filesInFolder.append(i)
#print(filesInFolder)
# Filter Folders from the list of filesInFolder
def testFunc(a):
    return not os.path.isdir(os.getcwd()+'\\'+a)
filesInFolder = list(filter(testFunc,filesInFolder))

# Filter the files that doesnt end with .txt
for file in filesInFolder:
    if not file.casefold().endswith('.mp4'):
        filesInFolder.remove(file)
# Read the contents of the files into the list allFilesContents
#print("\n".join(filesInFolder))

for i in range(filesInFolder.__len__()):
    os.rename(os.listdir()[i],filesInFolder[i])
