# Remove the first 3 characters from filename if the extension is avi

import os
folderPath = r'C:\Python'
fileExtension = 'avi'

if str(input('Rename files? (y/N)')).strip().upper()[0] == 'Y':
    for fileName in os.listdir(folderPath):
        if fileName[-len(fileExtension):].upper == fileExtension.upper:
            os.rename(folderPath + '\\' + fileName,
                      folderPath + '\\' + fileName[4:])
