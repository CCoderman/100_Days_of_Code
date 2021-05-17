from random import randint


# Day 4
# Create a RPS game

def rps_game():
    # Create rps variables
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    # List to store game images
    game_images = [rock, paper, scissors]

    # User input
    decision = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors:\n"))
    if decision != 0 and decision != 1 and decision != 2:
        print("Oops! Something went wrong. Did you put a number between 0 and 2?")
        exit()

    # Variable to randomize computer choice
    comp_decision = randint(0, 2)

    # logic to determine and print winner
    # If player picks rock (0)
    if decision == 0:
        print("You picked rock.")
        print(game_images[decision])
        if comp_decision == 1:
            print("The computer picked paper.")
            print(game_images[comp_decision])
            print("Paper beats rock. The computer wins!")
        elif comp_decision == 2:
            print("The computer picked scissors.")
            print(game_images[comp_decision])
            print("Rock beats scissors. You win!")
        else:
            print("The computer picked rock.")
            print(game_images[comp_decision])
            print("It's a tie!")
    # If the player picks paper
    elif decision == 1:
        print("You picked paper.")
        print(game_images[decision])
        if comp_decision == 0:
            print("The computer picked rock.")
            print(game_images[comp_decision])
            print("Paper beats rock. You win!")
        elif comp_decision == 2:
            print("The computer picked scissors.")
            print(game_images[comp_decision])
            print("Scissors beats rock. The computer wins!")
        else:
            print("The computer picked paper.")
            print(game_images[comp_decision])
            print("It's a tie!")
    # If the player picks scissors
    elif decision == 2:
        print("You picked scissors.")
        print(game_images[decision])
        if comp_decision == 0:
            print("The computer picked rock.")
            print(game_images[comp_decision])
            print("Rock beats scissors. The computer wins!")
        elif comp_decision == 1:
            print("The computer picked paper.")
            print(game_images[comp_decision])
            print("Scissors beats paper. You win!")
        else:
            print("The computer picked scissors.")
            print(game_images[comp_decision])
            print("It's a tie!")


if __name__ == "__main__":
    rps_game()
