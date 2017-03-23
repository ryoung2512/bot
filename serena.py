#!/usr/bin/python3
import os
import pywit
try:
    import pwd
except:
    print('')

USER = ''
def get_user_id():
    try:
        USER = pwd.getpwuid(os.getuid())[0]
    except ModuleNotFoundError:
        USER = os.getlogin()

def list_plugins():
    files = os.listdir(os.getcwd() + "/plugins/")
    plugins = []
    for p in files:
        plugin = p.split(".")
        plugins.append(plugin[0])
    return plugins

# make this a constant that way we have to reload to check for new plugins
PLUGINS = list_plugins()


def validate_command(user_input):
    split_input = user_input.split()
    if (len(split_input) > 1 and split_input[0] in PLUGINS) or (len(split_input) == 1 and split_input in PLUGINS):
        print("Valid command can now be executed")
    else:
        print("Sorry, that was an invalid command!")


def main():
    os.system('clear')
    print("Hello " + USER)
    user_input = ""
    while user_input != "quit":
        user_input = input(">> ")
        validate_command(user_input)

if __name__ == '__main__':
    main()
