import os
fileDirectory = input("where is this file located? ")
fileName = input("what is the name of the file? include the extension ")
fileType = input("what is the file type? should be the same as the extension ")
fileConvertTo = input("what do you want to convert the file to? ")

def fileConversion(directory, name, originalExtension, newExtension):
    newFileName = list(name)
    for i in range(len(originalExtension)):
        newFileName.pop(-1)
    os.rename(name, ''.join(newFileName)+newExtension)

fileConversion(fileDirectory, fileName, fileType, fileConvertTo)

