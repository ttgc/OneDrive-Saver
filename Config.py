#!usr/bin/env python3.7
#-*-coding:utf-8-*-
#Config class

import json

class Config:
    instance = None
    path = "config.json"

    def __new__(cls):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance

    def __init__(self):
        self.content = {}
        with open(Config.path, "r") as f:
            self.content = json.load(f)

    def __getitem__(self, item):
        return self.content[item]

    def __call__(self, *args):
        result = self.content
        for i in args:
            result = result[i]
