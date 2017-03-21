#!/usr/bin/python3
import os

def listPlugins():
    plugins = os.listdir(os.getcwd() + "/plugins/")
    for p in plugins:
        plugin = p.split(".")
        print(plugin[0])
listPlugins()
