#!/usr/bin/env python3
import prompt
import random
import operator


def greeting():
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')


def block_of_the_game_even():
    print('Answer "yes" if the number is even, otherwise answer "no"')
    count = 0
    for _ in range(3):
        random_number = random.randint(1, 1000)
        if random_number % 2 == 0:
            ans = 'yes'
        else:
            ans = 'no'
        print(f'Question: {random_number}')
        user_ans = prompt.string('Your answer: ')
        if random_number % 2 == 0 and user_ans == 'yes':
            print('Correct!')
            count += 1
        elif random_number % 2 != 0 and user_ans == 'no':
            print('Correct!')
            count += 1
        elif user_ans != 'yes' or user_ans != 'no':
            print(f"'{user_ans}' is wrong answer ;(. Correct answer was '{ans}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print(f"'{user_ans}' is wrong answer ;(. Correct answer was '{ans}'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


def block_of_the_game_calc():
    print('What is the result of the expression?')
    count = 0
    for _ in range(3):
        random_number_1 = random.randint(1, 100)
        random_number_2 = random.randint(1, 100)
        operators = {'*': operator.mul(random_number_1, random_number_2), '+': operator.add(random_number_1, random_number_2), '-': operator.sub(random_number_1, random_number_2)}
        keys_in_the_list = list(operators.keys())
        key = random.choice(keys_in_the_list)
        print(f'Question: {random_number_1} {key} {random_number_2}')
        user_ans = prompt.integer('Your answer: ')
        if user_ans == operators[key]:
            print('Correct!')
            count += 1
        elif user_ans != operators[key]:
            print(f"'{user_ans}' is wrong answer ;(. Correct answer was '{operators[key]}'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


def block_of_the_game_gcd():
    print('Find the greatest common divisor of given number.')
    flag = True
    gcd = 1
    for _ in range(3):
        random_number_1 = random.randint(1, 100)
        random_number_2 = random.randint(1, 100)
        print(f'Question: {random_number_1} {random_number_2}')
        user_ans = prompt.integer('Your answer: ')
        for i in range(1, max(random_number_1, random_number_2) + 1):
            if random_number_1 % i == 0 and random_number_2 % i == 0:
                gcd = i
        if user_ans == gcd:
            print('Correct!')
            gcd = 1
        else:
            flag = False
            print(f"'{user_ans}' is wrong answer ;(. Correct answer was '{gcd}'.")
            print(f"Let's try again, {name}!")
            break
    if flag:
        print(f'Congratulations, {name}!')
        