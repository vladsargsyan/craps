# main.py

from dice import roll_dice
from game import check_result


def main():

    # First roll
    first_roll = roll_dice()
    print(f"The sum of dice is {first_roll}")

    if first_roll in (7, 11):
        print("You won!")
    elif first_roll in (2, 3, 12):
        print("The casino wins!")
    else:
        goal_number = first_roll
        print(check_result(first_roll, goal_number))

        # Subsequent rolls
        while True:
            next_roll = roll_dice()
            print(f"The sum of dice is {next_roll}")

            if next_roll == goal_number:
                print("You won!")
                break
            elif next_roll == 7:
                print("You lose.")
                break


if __name__ == "__main__":
    main()
