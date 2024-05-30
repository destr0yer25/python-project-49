#!/usr/bin/env python3
import prompt


def greeting():
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')


def return_user_name():
    return name


def game_launch(game_logic_module):
    print('Welcome to the Brain Games!')
    greeting()
    game_logic_module()
