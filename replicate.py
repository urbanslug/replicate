#! /usr/bin/env python

import os
import re
import shutil
from optparse import OptionParser


def traverse (subDest, rootDir):
    for dirName, subDirs, files in os.walk(rootDir):
        for fileName in files:
            src = dirName + "/" + fileName
            dest = subDest + createDest(dirName)
            createPath (dest)
            copyfile(src, dest)
            #delExe (src)
            #delVbs (src)

def delExe (filePath):
    exe = re.search ('\.exe', filePath)
    if exe:
        os.remove (filePath)
        print ("removed exe: ", filePath)

def delVbs (filePath):
    vbs = re.search ('\.vbs', filePath)
    if vbs:
        os.remove (filePath)
        print ("Removed vbs: ", filePath)

def createDest (path):
    dirs = (re.split ('/', path)) [4::]
    toReplicate = '/'.join(dirs)
    return toReplicate


def copyfile (src, dest):
    shutil.copy(src, dest, follow_symlinks=True)

def createPath (newPath):
    if not os.path.exists (newPath):
        os.makedirs (newPath)

def parsePaths ():
    parser = OptionParser ()
    parser.add_option("-s", "--source",
                      dest="source",
                      help="The path to the source tree.")
    parser.add_option("-d", "--destination",
                      dest="destination",
                      help="Where you want to replicate the source tree to.")
    parser.add_option('-r', '--remove',
                      dest='remove',
                      help = 'The tree from which you want to remove the bad')
    (options, args) = parser.parse_args ()
    dest = options.destination; src = options.source
    if not re.search ('/$', options.destination): dest = options.destination + '/'
    if not re.search ('/$', options.source): src = options.source + '/'
    if src and dest: traverse (dest, src)


def main ():
    parsePaths ()


main ()
