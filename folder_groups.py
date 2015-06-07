#!/usr/bin/env

from itertools import groupby

def getFolderGroup(filePaths):
    '''
    parameters:
        filePaths: list
            list of file paths, relative or absolute. These paths will then be grouped in a dictionary
    returns:
        dict

    '''
    folderDict = {}

    # Group the folder and files
    for folder, files in groupby(filePaths, key=lambda x: x.split('/')[0]):
        relativeFilePaths = []
        children = [child for child in files]

        if folder in children:
            children.remove(folder)

        for child in children:
            relativeFilePath = child.replace("{0}/".format(folder), '')
            relativeFilePaths.append(relativeFilePath)

        if relativeFilePaths:
            folderDict[folder] = getFolderGroup(relativeFilePaths)
        else:
            folderDict[folder] = ''

    return folderDict

'''
Example

python folder_groups.py
'''
filePaths = ['foo/scenes/render.hip',
             'foo/scenes/sim.hip',
             'foo/workspace.mel',
             'foo/models/body.abc',
             'foo/models/head.abc',
             'foo/cache/scene.abc']

allFolderDict = getFolderGroup(filePaths)

print allFolderDict
