#!/usr/bin/python
import sys, os, shutil;
def delHideenRepoFile(theDir):
    if os.path.isfile(theDir):
        return;
    files = os.listdir(theDir);
    for aFile in files:
        subPath = theDir + "/" + aFile;
        isRepoFile = False;
        if os.path.isdir(subPath):
            if aFile == ".git":
                shutil.rmtree(subPath);
                isRepoFile = True;
                print subPath;
            elif aFile == ".svn":
                shutil.rmtree(subPath);
                isRepoFile = True;
                print subPath;
        if isRepoFile == False:
            delHideenRepoFile(subPath)
if __name__=="__main__":
    path = sys.argv[1];
    delHideenRepoFile(path);
