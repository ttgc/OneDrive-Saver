#!usr/bin/env python3.7
#-*-coding:utf-8-*-
#OneDrive auto saver script

import os, shutil
from Config import *
from Hidden import *

# Load config singleton once at start
Config()

def copydirectory(dir, dest, deep=True):
    with os.scandir(dir) as it:
        for entry in it:
            if entry.is_dir(follow_symlinks=False) and deep and not is_hidden(entry.name, entry.stat(follow_symlinks=False)):
                os.mkdir(os.path.join(dest, entry.name))
                copydirectory(entry.path, os.path.join(dest, entry.name), deep)
            elif entry.is_file(follow_symlinks=False) and not is_hidden(entry.name, entry.stat(follow_symlinks=False)):
                shutil.copyfile(entry.path, os.path.join(dest, entry.name), follow_symlinks=False)
                print(f"copied file {entry.path} successfuly to {dest}")
    print(f"copied directory {dir} successfuly to {os.path.dirname(dest)}")

def main():
    cfg = Config()
    backupdir = os.path.join(cfg["onedrive-path"], cfg["backup-directory"])
    if os.access(backupdir, os.W_OK):
        shutil.rmtree(backupdir, onerror=lambda fct, path, excinfo: print(f"\nERROR while removing {path} with function {fct} :\n{excinfo}\n"))
    os.mkdir(backupdir)
    for file in cfg["saved-paths"]:
        destdir = os.path.join(backupdir, file["dest-dirname"])
        os.mkdir(destdir)
        copydirectory(file["path"], destdir, cfg["deep-copy"])


# Launch main function
main()
