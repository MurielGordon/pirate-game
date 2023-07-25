from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):
    # is any of the stuff right below this necessary? I never see it print these two things:
    # what if I write "pass" under this instead?
    # "pass" doesn't seem to change anything about the behavior...so...I'll keep it I guess
    def enter(self):
        pass
        #print("This scene is not yet configured.")
        #print("Subclass it and implement enter().")
        #exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Death(Scene):
    quips = [
        "\nAt least now you can be a cool ghost.\n",
        "\nDon't quit your day job, adventuring is not for you.\n",
        "\nNow you get to be one of those iconic skull and crossbones that you always see in pirate movies.\n"
    ]

    def enter(self):
        import skull
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class ShipsBrig(Scene):
    def enter(self):
        print(dedent("""
        You awaken in a damp, dark room. A weak beam of sunlight shines through a grate in the ceiling. The room
        sways a bit, and you hear the creaking of wood. 
        
        You are on a ship, locked away in the brig.
        
        A voice croaks "You've got yourself in quite the scrape, eh? I'll remove those manacles if you can guess
        which cup the key is under."\n\n
        """))

        #import time
        #time.sleep(15)

        print(dedent("""
        You look down and see that your wrists are held in heavy iron manacles. You peer through the brig's darkness
        and see a wizened old man grinning toothlessly at you. His hands rest on two wooden cups turned upside down on the 
        table in front of him. He begins to slide them around on a small wooden table, laughing cruelly all the while.
        
        "If you guess wrong, old Hammertoes here will use his knife on you," the old man says, pointing to a capuchin
        monkey perched on a crate next to him. The monkey screams and bangs the butt of a dagger on the top of the
        crate.
        
        Which of the cups do you pick? 1 or 2?"""))

        correct_cup = randint(1,2)
        guess = input("[cup #]> ")

        if int(guess) != correct_cup:
            print(f"You pick cup number {guess}.")
            #time.sleep(3)
            print(dedent("""
                         The old man cackles wickedly. He lifts the cup to reveal not a 
                         key, but a small stone. 
                         "I guess it's death for you!" he laughs. The monkey lunges and, with a bloodcurdling scream,
                         plunges the dagger into your chest.
                         """))
            return 'death'
        else:
            print(f"You pick cup number {guess}.")
            #time.sleep(3)
            print(dedent(f"""
                         The old man scowls. He lifts the cup to reveal a small key, then
                         grudginlgy unlocks your manacles. You rush past him and run up the stairs, then turn right
                         to find find yourself facing a closed door.
                         """))
            return 'ships_magazine'


class ShipsMagazine(Scene):
    def enter(self):
        print(dedent("""
        You burst through the door and close it behind you. You have no idea what you're doing on this ship, but you've got to
        find a way off it.
        """))
        #import time
        #time.sleep(12)
        print(dedent("""
        You look around and find that you are in the ship's magazine. Stacked barrels of gunpowder line the walls
        around you. Pyrotechnics are just the thing to distract what seems to be a very unfriendly crew of pirates.
        
        How best to use this gunpowder? Should you throw a match and run?
        
        Type "yes" or "no."
        """))

        action = input("> ")

        if action == "yes":
            print(dedent("""
            You light a match and throw it, immediately turning to rush out the door.

            You aren't quick enough. The gunpowder ignites instantly and explodes. You are engulfed in a fireball 
            the size of a city block.
            """))
            return 'death'
        
        elif action == "no":
            print(dedent("""
            You know better than to go lighting matches in a room full of gunpowder. You look around for a fuse
            and find a bundle of them in a sack next to the door. You open kegs of gunpowder, pouring it
            in a line leading up to the door. 
            """))
            #time.sleep(10)
            print(dedent("""
            You lay the fuse and go to open the door. You plan to stretch your fuse out away from the
            powder so that you can light it safely. A voice behind you says:

            "Fooling with the powder are ye? And who might ye be?"
            """))
            #time.sleep(10)
            return 'bosun_talk'


class BosunTalk(Scene):
    def enter(self):
        print(dedent("""
        The ship's bosun found you! 

        "I ought to run ye through my with me cutlass!" the bosun hollers. He raises the sword and prepares to
        charge you, when two brilliant ideas come to you. You can either trip the bosun and run away, or distract
        him with a trick.

        So which will it be? Think fast!
        """))

        action = input("> ")

        if "trip" in action:
            print(dedent("""
            You stick your foot out to trip the bosun as he rushes toward you. He trips as you intended, but instead
            of falling to the side, he falls right at you, and his cutlass goes right through your middle.

            Looks like you didn't make it, matey!
            """))
            return 'death'
        
        elif "distract" or "trick" in action:
            print(dedent("""
            "Look behind you!" you yell, "A three headed monkey!"

            And the bosun is just dumb enough to fall for it. While he's doing that, you run around him and head
            for the stern of the ship, hoping to dive over the side and swim away.
            """))
            import time
            time.sleep(10)
            return 'walk_plank'


class WalkPlank(Scene):
    def enter(self):
        print(dedent("""
        You get to the stern and look down at the water below. It's a long way down. But it's your only way out.
        """))
        import sea_shanty
        return 'mermaid_encounter'


class MermaidEncounter(Scene):
    def enter(self):
        print(dedent("""
        The velocity of your plunge sends you deep under the water. You kick your feet and swim back up to the surface.
        You gasp as you surface and you hear the sound of the pirates laughing up above you. They jeer and mock you as
        you swim away but you ignore them. You have a long swim to an island to focus on. 

        You make tracks. 

        As you swim, you feel a tug on your leg. You turn and find that a mermaid has grabbed hold of your ankle. What
        now???

        "I demand you play a game with me," she says.

        "Peekaboo?" you ask hopefully. You're tired of these tests and games and are hoping for something innocuous.

        "No," she replies. "Rock, paper, scissors. And if I win I get to drown you."

        You sigh, then set your hands in the "ready" position for roshambo.
        """))
        import roshambo
        return 'finished'
    


class Finished(Scene):
    def enter(self):
        print(dedent("""
        You make it to the island. You crawl ashore and collapse on the warm sand.
        When you catch your breath, you sit up and look around. 
        On the island are many coconut trees, laden with fruit.
        Under one you see a huge chest. It is so full of its contents that the lid cracks open.
        The glint of gold can be seen from within the chest.
        Next to the chest is a bottle of rum and a handheld transciever.
        You should have no problem calling for help on that radio.
        But first, some rum, and maybe an hour or two to take inventory of the treasure chest.
        You grin happily.
        You won! Good job!
        """))
        return 'finished'
    

class Map(object):
    scenes = {
        'ships_brig': ShipsBrig(),
        'ships_magazine': ShipsMagazine(),
        'bosun_talk': BosunTalk(),
        'walk_plank': WalkPlank(),
        'mermaid_encounter': MermaidEncounter(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)
    

a_map = Map('ships_brig')
a_game = Engine(a_map)
a_game.play()