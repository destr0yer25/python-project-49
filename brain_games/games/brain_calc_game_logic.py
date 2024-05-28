#!/usr/bin/env python3
import prompt
import random
import operator
from brain_games import common_logic_bg


def block_of_the_game_calc():
    print('What is the result of the expression?')
    count = 0
    for _ in range(3):
        random_number_1 = random.randint(1, 100)
        random_number_2 = random.randint(1, 100)
        operators = {
            '*': operator.mul(random_number_1, random_number_2),
            '+': operator.add(random_number_1, random_number_2),
            '-': operator.sub(random_number_1, random_number_2)
        }
        keys_in_the_list = list(operators.keys())
        key = random.choice(keys_in_the_list)
        print(f'Question: {random_number_1} {key} {random_number_2}')
        user_ans = prompt.integer('Your answer: ')
        if user_ans == operators[key]:
            print('Correct!')
            count += 1
        elif user_ans != operators[key]:
            print(f"'{user_ans}' is wrong answer ;(."
                  f"Correct answer was '{operators[key]}'.")
            print(f"Let's try again, {common_logic_bg.return_user_name()}!")
            break
    if count == 3:
        print(f'Congratulations, {common_logic_bg.return_user_name()}!')
