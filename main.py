import random


def welcome_message():
    return f"""
{'*' * 5}Number Guessing Game{'*' * 5}

Guess the number between 1 and 100.
    """


def game(difficulty):
    print("Let's start the game!")
    random_number = random.randint(1, 100)
    attempts = 0
    chances = 0
    match difficulty:
        case 1:
            chances = 10
        case 2:
            chances = 5
        case 3:
            chances = 3
        case _:
            chances = 0

    while chances > 0:
        try:
            user_guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("idiot")
            user_guess = int(input("\nEnter your guess (last chance): "))
        if user_guess > random_number:
            chances -= 1
            attempts += 1
            print(f"Wrong! Guess lower ({chances} chances left)")
        elif user_guess < random_number:
            chances -= 1
            attempts += 1
            print(f"Wrong! Guess Higher ({chances} chances left)")
        elif user_guess == random_number:
            return f"You guessed correctly in {attempts} attempts"


    if chances == 0:
        return f"You have no more chances!\n The correct number was {random_number}"
    return None


def main():
    print(welcome_message())
    is_running = True

    while is_running:
        print("""
Select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
        """)
        try:
            user_choice = int(input("Enter your choice: "))
            print(
                f"\nYou have selected the {"Easy" if user_choice == 1 else "Medium" if user_choice == 2 else "Hard" if user_choice == 3 else "none"} difficulty level")
            match user_choice:
                case 1:
                    print(game(1))
                case 2:
                    print(game(2))
                case 3:
                    print(game(3))
                case _:
                    print("Choose from 1 - 3")
            play_again = input("Do you want to play again? (Y/N): ").upper()
            match play_again:
                case "Y":
                    continue
                case "N":
                    is_running = False

        except ValueError:
            print("Enter a number!")
        except KeyboardInterrupt:
            print("\nGood bye!")
            is_running = False


if __name__ == "__main__":
    main()
