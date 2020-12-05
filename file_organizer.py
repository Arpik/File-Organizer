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
def collectFiles(path):
    # Receives path from the command line and changes \\ to / 
    path = sys.argv[1].replace('\\', '/')
    
    fileExtansions = ['txt', 'docx', 'pdf', 'jpg','mp4', 'png', 'py', 'bmp']
    for file in desktopFiles:
        for extention in fileExtansions:
            if file.endswith(extention):
                # print(extention.upper())
                createFolder('../Desktop/{}'.format(extention.upper()))
                shutil.move('/Users/Roger/Desktop/{}'.format(file), '../Desktop/{}'.format(extention.upper()))
collectFiles('../Desktop/')

# def collectFiles(path):
# # loc = r'C:\Users\Roger\Desktop'
#     for file in os.listdir(path):
#         fName, fExt = os.path.splitext(file) 
#         print(fExt)

# collectFilesf