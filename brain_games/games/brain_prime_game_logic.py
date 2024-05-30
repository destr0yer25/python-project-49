#!/usr/bin/env python3
import prompt
import random
from brain_games import common_logic_bg


def is_prime():
    control = 'yes'
    random_number = random.randint(1, 300)
    if random_number == 1:
        control = 'no'
    for i in range(2, random_number):
        if random_number % i == 0:
            control = 'no'
            break
    return control, random_number


def block_of_the_game_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    flag = True
    for _ in range(3):
        ans, random_number = is_prime()
        print(f'Question: {random_number}')
        user_ans = prompt.string('Your answer: ')
        if user_ans == ans:
            print('Correct!')
        elif user_ans != ans:
            flag = False
            print(f"'{user_ans}' is wrong answer ;(."
                  f"Correct answer was '{ans}'.")
            print(f"Let's try again, {common_logic_bg.return_user_name()}!")
            break
        else:
            flag = False
            print(f"'{user_ans}' is wrong answer ;(."
                  f"Correct answer was '{ans}'.")
            print(f"Let's try again, {common_logic_bg.return_user_name()}!")
            break
    if flag:
        print(f'Congratulations, {common_logic_bg.return_user_name()}!')
