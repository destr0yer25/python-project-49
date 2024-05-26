#!/usr/bin/env python3
import prompt
import random


def greeting():
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')


def return_user_name():
    return name


def block_of_the_game_progression():
    print('What number is missing in the progression?')
    flag = True
    for _ in range(3):
        progress_list = []
        lgth = random.randint(5, 10)
        step = random.randint(1, 20)
        starting_number = random.randint(1, 100)
        next_number = starting_number
        for i in range(lgth):
            if i == 0:
                progress_list.append(f'{starting_number}')
            else:
                next_number += step
                progress_list.append(f'{next_number}')
        index_hidden_number = progress_list.index(random.choice(progress_list))
        hidden_number = progress_list[index_hidden_number]
        progress_list[index_hidden_number] = '..'
        print(f'Question: {" ".join(progress_list)}')
        user_ans = prompt.integer('Your answer: ')
        if index_hidden_number == 0 and user_ans == starting_number:
            print('Correct!')
        elif index_hidden_number <= len(progress_list) - 1 and user_ans == int(progress_list[index_hidden_number - 1]) + step:
            print('Correct!')
        else:
            flag = False
            print(f"'{user_ans}' is wrong answer ;(. Correct answer was '{hidden_number}'.")
            print(f"Let's try again, {name}!")
            break
    if flag:
        print(f'Congratulations, {name}!')


def block_of_the_game_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    flag = True
    for _ in range(3):
        ans = ''
        random_number = random.randint(1, 300)
        if random_number == 1:
            ans = 'no'
        elif random_number == 2:
            ans = 'yes'
        for i in range(2, random_number):
            if random_number % i == 0:
                ans = 'no'
                break
            else:
                ans = 'yes'
        print(f'Question: {random_number}')
        user_ans = prompt.string('Your answer: ')
        if user_ans == ans:
            print('Correct!')
        elif user_ans != ans:
            flag = False
            print(f"'{user_ans}' is wrong answer ;(. Correct answer was '{ans}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            flag = False
            print(f"'{user_ans}' is wrong answer ;(. Correct answer was '{ans}'.")
            print(f"Let's try again, {name}!")
            break
    if flag:
        print(f'Congratulations, {name}!')
