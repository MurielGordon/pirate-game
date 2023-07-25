from sys import exit
from textwrap import dedent

print(dedent("""
Rough hands seize you from behind. You struggle, but it's no use, the hands are like iron.

"So this is who has been blundering around my ship," a voice says as another pair of hands tie your wrists 
behind your back.

You are spun around to face a tall elegantly dressed woman with an aura of authority about her. This must be
the captain of the ship.

"Make this little stowaway walk the plank!" she orders.

You're pushed towards a plank that is conviently standing ready to plunge idiots like yourself to your death.
You walk out onto it at swordpoint. You stand, shivering, staring at the water below you. If you had the use
of your hands you could swim easily, but without them...

"I'll untie your hands and let you swim to that island over there if you can complete the lyrics to this sea 
shanty," the captain says.

She sings:

"For it's cheer up me lads,
Let your hearts never fail
For the bonny ship The Diamond
Goes a-fishing for the --"

What's the last word of the shanty?
"""))

action = input("> ")

if action == "whale":
    print(dedent("""
    You got it right!
    Your bonds are cut and you're kicked forward on the plank.
    Nothing for it. Best be getting it over with.
    You jump in.
    """))

else:
    print(dedent("""
    Your lack of sea shanty knowledge is embarrassing and you should be embarressed.
    
    You are kicked into the sea and you drown.
    """))
    import skull
    exit(1)