#!/usr/bin/python3
import utils.speechtt as user_speech
import utils.converse as converse


def main():
    user_input = ""
    communicator = converse.Communicator()
    intent = ""
    while intent != "goodbye":
        #user_input = user_speech.active_listen()
        if (communicator.get_type() == 'empty' or communicator.get_type() == 'stop'):
            user_input = input("> ")
        communicator.talk(user_input)
        intent = communicator.get_intent()
        communicator.print_message()


if __name__ == '__main__':
    main()
