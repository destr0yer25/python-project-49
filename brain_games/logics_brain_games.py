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
            control = 'yes'
        else:
            control = 'no'
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')
        if random_number % 2 == 0 and user_answer == 'yes':
            print('Correct!')
            count += 1
        elif random_number % 2 != 0 and user_answer == 'no':
            print('Correct!')
            count += 1
        elif user_answer != 'yes' or user_answer != 'no':
            print(f'{user_answer} is wrong answer ;(. Correct answer was {control})')
            print(f"Let's try again, {name}!")
            break
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {control})')
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
