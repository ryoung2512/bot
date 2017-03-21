#!/usr/bin/python3
import os

def listPlugins():
    files = os.listdir(os.getcwd() + "/plugins/")
    plugins = []
    for p in files:
        plugin = p.split(".")
        plugins.append(plugin[0])
    return plugins

def main():
    user_input = ""
    while user_input != "quit":
        user_input = input(">> ")
        print("You entered " + user_input)
