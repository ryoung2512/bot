#!/usr/bin/python3
import os

def listPlugins():
    files = os.listdir(os.getcwd() + "/plugins/")
    plugins = []
    for p in files:
        plugin = p.split(".")
        plugins.append(plugin[0])
    return plugins
print(listPlugins())
