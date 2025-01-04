#!/usr/bin/env

from itertools import groupby

def getRootPath(path):
    rootPath = path.split('/')[0]
    return rootPath

def getFolderGroup(filePaths):
    '''
    Convert a list of paths into a dictionary, grouped by the folders

    parameters:
        filePaths: list
            list of file paths, these paths will then be grouped in a dictionary.
            paths will need to be separated by '/', if this is ran on windows systems, just convert it before passing
            the list in.
    returns:
        dict

    '''
    folderDict = {}

    # Group the folder and files, group by the first folder, using the '/' as the separator
    for folder, files in groupby(filePaths, key=getRootPath):
        relativeFilePaths = []
        # Convert the iterator (files) to a list (children)
        children = [child for child in files]

        # Remove the current folder in the children list, because we're going to put the children in this folder
        if folder in children:
            children.remove(folder)

        # Add the children's path to the list, without the current folder in the path
        # E.g. if the current folder is 'foo', and the child's path is foo/models/head.abc, this will now become
        # models/head.abc
        for child in children:
            relativeFilePath = child.replace("{0}/".format(folder), '')
            relativeFilePaths.append(relativeFilePath)

        # If there are relative paths, there are children in this folder. Get the children by calling this method
        # to get the dictionary for the children. Otherwise, empty string for this group.
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
