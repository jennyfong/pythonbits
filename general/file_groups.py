#!/usr/bin/env

'''
Methods to group files with the name together, indicating the number sequences

files = ['foo.001', 'foo.002', 'foo.003', 'foo.004', 'foo.008', 'moo.009']
getFileGroups(files)

This would return ['foo.1-4,8', 'moo.9']
'''
from itertools import groupby, count

def keyDifference(num, c=count()):
    """
    This is to calculate if there's a gap between the numbers
    For example:

    | number | counter | difference |
    |   1    | 0       | 1 |
    |   2    | 1       | 1 |
    |   3    | 2       | 1 |
    |   4    | 3       | 1 |
    |   7    | 4       | 2 |
    |   8    | 5       | 2 |
    |   10   | 6       | 4 |

    The difference can then be used to group 001-004, 007-008, 010 together

    If you prefer using lambda you could do groupby(numList, key=lambda x: x - next(count()))
    """
    return num - next(c)

def groupByNumbers(numList):
    """
    Get the numbers in groups

    parameters:

        numlist: `list`

    """
    numList = sorted(numList)
    numListText = []

    for key, group in groupby(numList, key=keyDifference):
        li = list(group)
        numListText.append(numRange(li))

    return ','.join(numListText)

def numRange(numList):
    """
    Get the first and last number in the list
    """
    start = numList[0]
    end = numList[-1]
    if start != end:
        return "{}-{}".format(start, end)
    else:
        return "{}".format(start)

def fileNumber(filePath):
    """
    Get the number of the file. foo.0080 would return 0080
    """
    num = filePath.split('.')[-1]
    return int(num)

def fileGroupName(filePath):
    """
    Get the group file name. foo.0080 would return foo
    """
    return filePath.split('.')[0]

def getFileGroups(files):
    """
    Return the file sets given a list of files

    parmeters:
        files : `list`
            list of files
    returns:

        list
    """

    # Sort the files so that they display in order
    files = sorted(files)

    fileGroups = []

    # Get the file groups
    for key, group in groupby(files, key=fileGroupName):
        # Get all the numbers in a sorted list, [0001, 0002] etc
        numList = [fileNumber(file) for file in group]
        frameNumbers = groupByNumbers(numList)
        frameText = "{}.{}".format(fileGroupName(key), frameNumbers)
        fileGroups.append(frameText)

    return fileGroups

files = ['foo.001', 'foo.002', 'foo.003', 'foo.004', 'foo.008', 'moo.009']
fileGroups = getFileGroups(files)
print fileGroups
