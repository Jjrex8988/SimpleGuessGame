import random

number_to_guess = random.randint(1, 10)

def welcome_msg():
    print("Welcome to the guess game")

def end_game():
    print("Thank you for playing game")


def get_user_input(prompt):
    invalid_input = True
    while invalid_input:
        print(prompt)
        user_input = input()
        if not user_input.isdigit():
            print("Input must be a number")
        else:
            user_input_int = int(user_input)
            if user_input_int < 1 or user_input_int > 10:
                print("Input must be in range of 1 to 10")
            else:
                invalid_input = False
    return user_input_int


def guess(get_user_input):
    number_to_tries = 1
    guess = int(input("Please guess a number between 1 to 10: "))

    while guess != number_to_guess:
        print("Sorry - Wrong number")

        if number_to_tries == 4:
            break
        elif guess < number_to_guess:
            print("Your guess was lower than the number to be guessed")
        else:
            print("Your guess was higher than the number to be guessed")
        number_to_tries += 1
        guess = int(input("Please guess a number between 1 to 10: "))
    return guess

def check_to_win(guess):
    if guess == number_to_guess:
        print("congratulation, you won")
    else:
        print("sorry, you loose")
        print("The number to be guessed: ", number_to_guess)
    play_again = input("Do you want to play again? (y/n): ")

    if play_again != "y" or play_again != "n":
        print("Please enter alphabet y or n only ")
        play_again = input("Do you want to play again@? (y/n): ")
        if play_again == "y":
            return get_user_input()

welcome_msg()

last_game = guess(get_user_input)
check_to_win(last_game)

end_game()
