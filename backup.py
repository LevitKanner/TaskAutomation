"""
backup.py - Copies an entire folder and its content into a zip file whose filename increments
"""
import zipfile, os

def backupToZip(folder):
    # Back up the entire content of folder to a zip file
    number = 1

    folder = os.path.abspath(folder)
    while True:
        zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipFilename):
            break
        number += 1

    #create a new zip file
    print("Creating a new zip file %s" % zipFilename)
    zipedFile = zipfile.ZipFile(zipFilename, "w")

    # Walk the entire folder and compress its content
    for currentFolder, subfolders, files in os.walk(folder):
        print("Adding the content of %s..." % folder)
        zipedFile.write(currentFolder)

        # Add all files in the folder
        for file in files:
            basename = os.path.basename(folder)
            if file.startswith(basename + "_") and file.endswith(".zip"):
                continue
            else:
                zipedFile.write(os.path.join(currentFolder, file))

    zipedFile.close()
    print("Done")

backupToZip(".")