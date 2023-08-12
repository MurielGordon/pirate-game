import sys
import time
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



print(dedent("""
\n\n
___________________________
\n             
Rough hands seize you from behind.
You struggle, but it's no use, the hands are like iron.

"So this is who has been blundering around my ship," a voice says as another pair of hands
tie your wrists behind your back.

You are spun around to face a tall elegantly dressed woman with an aura of authority about her.
This must be the captain of the ship.

"Make this little stowaway walk the plank!" she orders."""
))

time.sleep(17)

print(dedent("""
\n\n
___________________________
\n
You're pushed towards a plank that is standing ready to plunge idiots like you to their deaths.
You walk out onto it at swordpoint.
You stand, shivering with fear, staring at the water below you.
If you had the use of your hands you could swim easily, but without them...

"I'll untie your hands and let you swim to that island over there if you can complete the lyrics
to this sea shanty," the captain says.

She sings:

"For it's cheer up me lads,
Let your hearts never fail
For the bonny ship The Diamond
Goes a-fishing for the --"

What's the last word of the shanty?
"""))

action = input("> ")

loading()

if action == "whale":
    sword()
    print(dedent("""
    You got it right!
    The bonny ship The Diamond goes a-fishing for the whale.
    Your bonds are cut and you're kicked forward on the plank.
    Nothing for it. Best be getting it over with.
    
    You jump in.
    """))

else:
    print(dedent(f"""
    \n\n
    You guessed {action}??? 
    The bonny ship The Diamond goes a-fishing for the {action}????
    
    That doesn't make any sense!
    
    Your lack of sea shanty knowledge is embarrassing and you should be embarrassed.
    
    You are kicked into the sea and you drown.
    """))
    import skull
    exit(1)