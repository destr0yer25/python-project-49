#!/usr/bin/env python3
from brain_games import common_logic_bg
from brain_games.games import brain_even_game_logic


def main():
    print('Welcome to the Brain Games!')
    common_logic_bg.greeting()
    brain_even_game_logic.block_of_the_game_even()


if __name__ == '__main__':
    main()
