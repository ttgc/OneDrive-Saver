#!usr/bin/env python3.7
#-*-coding:utf-8-*-
#Hidden file and directory detection depending on OS used

import os, stat

def detect_platform(winfunc, unixfunc):
    def decorator(func):
        def inner(filename, stats):
            if (os.name == 'nt'): result = winfunc(filename, stats)
            elif (os.name == 'posix'): result = unixfunc(filename, stats)
            else: result = defaultfunc(filename, stats)
            return result
        return inner
    return decorator

def is_hidden_win(filename, stats):
    return bool(stats.st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)

def is_hidden_unix(filename, stats):
    return filename.startswith(".")

@detect_platform(is_hidden_win, is_hidden_unix)
def is_hidden(filename, stats): return False
