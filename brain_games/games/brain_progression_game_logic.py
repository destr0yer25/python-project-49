#!/usr/bin/env python3
import prompt
import random
from brain_games import common_logic_bg


def creating_a_progression_series():
    progression_series = []
    lgth = random.randint(5, 10)
    step = random.randint(1, 20)
    first_number = random.randint(1, 100)
    next_number = first_number
    for i in range(lgth):
        if i == 0:
            progression_series.append(f'{first_number}')
        else:
            next_number += step
            progression_series.append(f'{next_number}')
    return progression_series, first_number, step


def block_of_the_game_progression():
    print('What number is missing in the progression?')
    flag = True
    for _ in range(3):
        progress_list, starting_number, step = creating_a_progression_series()
        index_hidden_number = progress_list.index(random.choice(progress_list))
        hidden_number = progress_list[index_hidden_number]
        progress_list[index_hidden_number] = '..'
        print(f'Question: {" ".join(progress_list)}')
        user_ans = prompt.integer('Your answer: ')
        if index_hidden_number == 0 and user_ans == starting_number:
            print('Correct!')
        elif (index_hidden_number <= len(progress_list)
              - 1 and user_ans == int(progress_list[index_hidden_number - 1])
              + step):
            print('Correct!')
        else:
            flag = False
            print(f"'{user_ans}' is wrong answer ;(."
                  f"Correct answer was '{hidden_number}'.")
            print(f"Let's try again, {common_logic_bg.return_user_name()}!")
            break
    if flag:
        print(f'Congratulations, {common_logic_bg.return_user_name()}!')
