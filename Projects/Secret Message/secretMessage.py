import os

def renameFiles ():
    #Get file names
    fileList = os.listdir(r"E:\Code\Udacity\Python\Projects\Secret Message")
    # Don't need debug statment
    #print(fileList)

    startPath = os.getcwd()

    #rename folder
    os.chdir(r"E:\Code\Udacity\Python\Projects\Secret Message")
    for fileName in fileList:
        print("Old name " + fileName)
        print("New name " + fileName.translate(None, "0123456789"))
        os.rename(fileName, fileName.translate(None, "0123456789"))
    os.chdir(startPath)

renameFiles()
