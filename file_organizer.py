import os
import shutil

# Create new directory
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

# Collects files by putting them into appropriate folders.
def collectFiles():
    desktopFiles = os.listdir('../Desktop/')
    fileExtansions = ['txt', 'docx', 'pdf', 'jpg','mp4', 'png', 'py', 'bmp']
    for file in desktopFiles:
        for extention in fileExtansions:
            if file.endswith(extention):
                # print(extention.upper())
                createFolder('../Desktop/{}'.format(extention.upper()))
                shutil.move('/Users/Roger/Desktop/{}'.format(file), '../Desktop/{}'.format(extention.upper()))
collectFiles()