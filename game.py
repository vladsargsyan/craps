# game.py


def check_result(first_roll, goal_number):
    """Checks if the player wins or loses based on the rules."""
    if first_roll in (7, 11):
        return "You won!"
    elif first_roll in (2, 3, 12):
        return "The casino wins!"
    else:
        return f"Now your goal number is {goal_number}"
