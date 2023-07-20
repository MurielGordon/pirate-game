import random
from sys import exit
from textwrap import dedent
        

user_action = input("Choose your weapon: rock, paper, or scissors: ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, the mermaid chose {computer_action}.\n")


def start():
    if user_action == computer_action:
        print(f"You both selected {user_action}. It's a tie!")
        print(dedent("""
        The mermaid sighs with disappointment.
        "I guess techinically you didn't lose. So I'll let you go," she says.
        You swim away, grateful to have won.
        """))
    elif user_action == "rock":
        if computer_action == "scissors":
            print(dedent("""
            Rock smashes scissors! You win!
            The mermaid sighs with disappointment.
            "You won fair and square. So I'll let you go," she says.
            You swim away, grateful to have won.
            """))
        else:
            print(dedent("""
            Paper covers rock. You lose.
            The mermaid smiles and reaches out to grab you.
            She drowns you in the crystal clear Caribbean water.
            """))
            death()
    elif user_action == "paper":
        if computer_action == "rock":
            print(dedent("""
            Paper covers rock! You win!
            The mermaid sighs with disappointment.
            "You won fair and square. So I'll let you go," she says.
            You swim away, grateful to have won.
            """))
        else:
            print(dedent("""
            Scissors cuts paper. You lose.
            The mermaid smiles and reaches out to grab you.
            She drowns you in the crystal clear Caribbean water.
            """))
            death()
    elif user_action == "scissors":
        if computer_action == "paper":
            print(dedent("""
            Scissors cuts paper! You win!
            The mermaid sighs with disappointment.
            "You won fair and square. So I'll let you go," she says.
            You swim away, grateful to have won.
            """))
        else:
            print(dedent("""
            Rock smashes scissors. You lose.
            The mermaid smiles and reaches out to grab you.
            She drowns you in the crystal clear Caribbean water.
            """))
            death()


def death():
    print("You are dead you are so dead.")
    exit(1)


start()
#hello