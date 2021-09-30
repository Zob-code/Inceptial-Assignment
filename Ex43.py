from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("This scene is not yet configured")
        print("Subscribe it and implement enter()")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("Finished")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinds suck at this.",
        "Your Mom would be proud .. if she were smarter.",
        "Such a luser."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
                     The Gothons of planet Percel #25 have invaded your ship and
                     destroyed your entire crew. You aret he last surviving
                     member and your last mission is to geet the neutron destruct
                     bomb from the weapon armory.

                     Your are runnign down the centrla corridor to the weapons
                     armory when a gothon jumps out red skin , dark griemy
                     teeth, and evil clown costume flowing around his hate
                     fille body"""))

        action = input("> ")

        if action == "shoot":
            print(dedent("""
                        Quick onth edraw you yank out your blaster and fire
                        it at the gothon. His clown is flowing and moving
                        around his body, which throws off your aim.
                        Your laser hits his contume but missed him entirely.
                        This completely ruins his brand new costume his mother
                        bought him, which makes him fly into an insane rage.
                        Then he eats you.
                         """))
            return 'death'

        elif action == "dodge":
            print(dedent("""
                         Like a world class boxer you dodge, weave slip and
                         slider right as the gothon's blaster cranks a laser
                         past your head. In the middle of your artful dodge
                         your slips and you bang you head on the metal
                         wall and pass out.hten the gothon eats you."""))

            return 'death'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
                     You do a dive roll into the weapons armory, crouch and scan
                     the room for more Gothons that might be hiding. its dead
                     quiet too quiet. You stand up and run to the far side of the
                     room and find the neutron bomb in its container.
                     The deactivaiton code in 3 digits."""))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZEDDD")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                         The container clicks and return the seal breaks
                         letterring gasout you grab the neutro bomb ans run as fast as you can
                         """))
            return 'excape_pod'
        else:
            print(dedent("""
                         The lock buzzers one last time andd then you hear a
                         sickeing melting sound as the mechanism is fused
                         together. You decide to sit there and finally the
                         gothons blow up the ship form thier ship and you die.
                         """))
            return 'death'

class EscapePod(Scene):
    def enter(self):
        print(dedent("""
                     Yourush through the ship desparately trying to make it to
                     the escape pod before the shole ships explodes. It seems
                     like hardly any Gothoms are onthe ship, so your run is
                     clear of inteference. tere are 5 pods which do you takae?
                     """))

        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                         You jump into pod {guess} and hit the eject button.
                         Then implodes as the hull rupture, crushing you body
                         into jamjelly.
                         """))
            return 'death'
        else:
            print(dedent("""
                         You jump into pod {guess} and hit the eject button
                         The pod easily slides into space. You won!!"""))

class Finished(Scene):
    def enter(self):
        print("You won the game")
        return 'finished'


class Map(object):
    scenes = {
        'central_corridor' : CentralCorridor(),
        'laser_weapon_armory' : LaserWeaponArmory(),
        'escape_pod' : EscapePod(),
        'death' : Death(),
        'finished' : Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
