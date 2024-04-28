# dice.py

import random


def roll_dice():
    """Rolls two dice and returns their sum."""
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2
