#!/usr/bin/python3
import utils.speechtt as user_speech
import utils.converse as converse
import utils.commands as util
import utils.load_plugins as loadplugins

def main():
    user_input = ""
    print(util.get_username())
    communicator = converse.Communicator()
    intent = ""
    while intent != "goodbye":
        if communicator.get_type() == 'empty' or communicator.get_type() == 'stop' or intent =='empty':
            user_input = input("> ")
            print("Please say something: ")
            user_input = user_speech.active_listen()
            print("you: " + user_input)
        communicator.talk(user_input)
        intent = communicator.get_intent()
        print("intent: " + intent)
        communicator.print_message()


if __name__ == '__main__':
    main()
