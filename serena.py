#!/usr/bin/python3
import utils.speechtt as user_speech
import utils.converse as converse
import utils.commands as util
import utils.load_plugins as loadplugins


def main():
    user_input = ""
    username = util.get_username()
    communicator = converse.Communicator()
    intent = ""
    while intent != "goodbye":
        user_input = input("> ")
        # user_input = user_speech.active_listen()
        print(username + ": " + user_input)
        communicator.talk(user_input)
        # intent = communicator.get_intent()
        communicator.print_message()


if __name__ == '__main__':
    main()
