#!/usr/bin/env python3
from brain_games import common_logic_bg
from brain_games.games.brain_progression_game_logic import (
    block_of_the_game_progression
)


def main():
    common_logic_bg.game_launch(block_of_the_game_progression)


if __name__ == '__main__':
    main()
