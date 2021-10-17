class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

central_corridor = Room("Central Corridor",
"""
The Gothons of planet Percel #25 have invaded your ship and
destroyed your entire crew. You aret he last surviving
member and your last mission is to geet the neutron destruct
bomb from the weapon armory.

Your are runnign down the centrla corridor to the weapons
armory when a gothon jumps out red skin , dark griemy
teeth, and evil clown costume flowing around his hate
fille body
""")


laser_weapon_armory = Room("laser Weapon Armory",
"""
You do a dive roll into the weapons armory, crouch and scan
the room for more Gothons that might be hiding. its dead
quiet too quiet. You stand up and run to the far side of the
room and find the neutron bomb in its container.
The deactivaiton code in 3 digits.
""")


the_bridge = Room("The Bridge",
"""
The container clicks and return the seal breaks letterring
gasout you grab the neutro bomb ans run as fast as you can
to the bridge and must place it in the right spot.

You burst onto the Bridge with the neutron destruct bomb under the door
and surprise 5 Gothons who are trying to take control of the ship
after them has even uglier clown costume than the last.
""")


escape_pod = Room("Escape Pod",
"""
You point your balster at the bomb under your arm and the Gothon
think their hand up and start to sweet. You inch back to the door
it and then carefully place the bomb on the floor, pointing your
blaster to the gothon.

You rush through the ship desparately trying to make it to
the escape pod before the shole ships explodes. It seems
like hardly any Gothoms are onthe ship, so your run is
clear of inteference. tere are 5 pods which do you takae?

""")


the_end_winner = Room("The End",
"""
You jump into pod 2 and hit the eject button. The pos easily opens
into space heading to the planet below. As it flies to the place
look back and see your ship implode then explodes like a bright star
taking out the Gothon ship at the same time. You won!
""")


the_end_loser = Room("The End",
"""
You jump into pod a random pod and hit the eject button. the pod easily opens
Then implodes as the hull rupture, crushing you body into jamjelly.
""")


escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
})

generic_death = Room("death", "You died.")

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '0123': the_bridge,
    '*': generic_death
})

central_corridor.add_paths({
    'shoot': generic_death,
    'dodge': generic_death,
    'tell a joke': laser_weapon_armory
})

START = 'central_corridor'

def load_room(name):
    """
    There is a potential security problem here.
    Who gets to set name? Can that expose a variable?
    """
    return globals().get(name)

def name_room(room):
    """
    Same possible security problem. Can you trust room?
    What a better solution than this globals lookups?
    """
    for key, value in globals().items():
        if value == room:
            return key
