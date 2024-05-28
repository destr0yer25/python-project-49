#!/usr/bin/env python3
import prompt
import random
from brain_games import common_logic_bg


def is_even(number):
    return number % 2 == 0


def right_result():
    random_number = random.randint(1, 1000)
    correct_answer = 'yes' if is_even(random_number) else 'no'
    return random_number, correct_answer


def block_of_the_game_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    for _ in range(3):
        random_number, correct_answer = right_result()
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {common_logic_bg.return_user_name()}!")
            break
    if count == 3:
        print(f'Congratulations, {common_logic_bg.return_user_name()}!')
