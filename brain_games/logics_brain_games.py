import prompt
import random


def greeting():
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')


def block_of_the_game():
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
            print(f'{user_ans} is wrong answer ;(. Correct answer was {ans})')
            print(f"Let's try again, {name}!")
            break
        else:
            print(f'{user_ans} is wrong answer ;(. Correct answer was {ans})')
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
