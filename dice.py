# dice.py

import random


def roll_dice():
    """Rolls two dice and returns their sum."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2
