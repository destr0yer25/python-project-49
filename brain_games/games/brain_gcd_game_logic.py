#!/usr/bin/env python3
import prompt
import random
from brain_games import common_logic_bg


def search_gcd():
    gcd = 1
    random_number_1 = random.randint(1, 100)
    random_number_2 = random.randint(1, 100)
    print(f'Question: {random_number_1} {random_number_2}')
    user_ans = prompt.integer('Your answer: ')
    for i in range(1, max(random_number_1, random_number_2) + 1):
        if random_number_1 % i == 0 and random_number_2 % i == 0:
            gcd = i
    return user_ans, gcd


def block_of_the_game_gcd():
    print('Find the greatest common divisor of given numbers.')
    flag = True
    for _ in range(3):
        user_ans, gcd = search_gcd()
        if user_ans == gcd:
            print('Correct!')
        else:
            flag = False
            print(f"'{user_ans}' is wrong answer ;(."
                  f"Correct answer was '{gcd}'.")
            print(f"Let's try again, {common_logic_bg.return_user_name()}!")
            break
    if flag:
        print(f'Congratulations, {common_logic_bg.return_user_name()}!')
