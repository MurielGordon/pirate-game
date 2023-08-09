import sys
import time
import random
from sys import exit
from textwrap import dedent


def loading():
    loading = 0
    loading_speed = 3
    loading_string = "." * 6
    for i in range(2):
        for index, char in enumerate(loading_string):
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(1.0 / loading_speed)
        index += 1
        sys.stdout.write("\b" * index + " " * index + "\b" * index)
        sys.stdout.flush()

def sword():
    print("""      
\n\n      
      \\
[]oooo|==================>
  \___/
""")
        

user_action = input("Choose your weapon: rock, paper, or scissors: ")
#loading()
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\n\nYou chose {user_action}, the mermaid chose {computer_action}.\n")


def start():
    if user_action == computer_action:
        sword()
        print(f"You both selected {user_action}. It's a tie!")
        print(dedent("""
        The mermaid sighs with disappointment.
        "I guess techinically you didn't lose. So I'll let you go," she says.
        You swim away, grateful to have won.
        """))
    elif user_action == "rock":
        if computer_action == "scissors":
            sword()
            print(dedent("""
            Rock smashes scissors! You win!
            \nThe mermaid sighs with disappointment.
            "You won fair and square. So I'll let you go," she says.
            You swim away, grateful to have won.
            """))
        else:
            print(dedent("""
            Paper covers rock. You lose.
            \nThe mermaid smiles and reaches out to grab you.
            She drowns you in the crystal clear Caribbean water.
            """))
            death()
    elif user_action == "paper":
        if computer_action == "rock":
            sword()
            print(dedent("""
            Paper covers rock! You win!
            \nThe mermaid sighs with disappointment.
            "You won fair and square. So I'll let you go," she says.
            You swim away, grateful to have won.
            """))
        else:
            print(dedent("""
            Scissors cuts paper. You lose.
            \nThe mermaid smiles and reaches out to grab you.
            She drowns you in the crystal clear Caribbean water.
            """))
            death()
    elif user_action == "scissors":
        if computer_action == "paper":
            sword()
            print(dedent("""
            Scissors cuts paper! You win!
            \nThe mermaid sighs with disappointment.
            "You won fair and square. So I'll let you go," she says.
            You swim away, grateful to have won.
            """))
        else:
            print(dedent("""
            Rock smashes scissors. You lose.
            \nThe mermaid smiles and reaches out to grab you.
            She drowns you in the crystal clear Caribbean water.
            """))
            death()


def death():
    import skull
    print("You are dead you are so dead.")
    exit(1)


start()