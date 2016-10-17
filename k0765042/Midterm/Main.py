"""
Bryant Conquest
This is a Game
"""

from death import Finish
from death import lives
from scene import Scene
import lock
import random
import time


#Weapons
fist = 0
metal_pipe = 0



class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('death')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()



class GettingToKnowEveryone(Scene):

    def enter(self):
        lives = 2
        print "Gaurd: What is your name Sir"
        name = raw_input(">")
        time.sleep(1)
        if name == "Dave" or name == "dave":
            print("Gaurd: Oh Did not know that was you Dave sorry for the inconveince.")
            return 'death'
        else:
            print "Gaurd: Get moving %s" %name
            print "Gaurd: You nice and comfy in there?"
            print "Gaurd: Cause you better be you were the last one to be round up."
            print "Gaurd: Caused Quite a lot of trouble"
            print "Gaurd: And remember always tell the truth."
            return 'the_beginning'

class TheBeginning(Scene):

    def enter(self):
        global lives
        global metal_pipe
        print(chr(27) + "[2J")
        print "Prisoner 1: They Finally found you huh."
        print "Prisoner 1: You were are last chance.  "
        print "Prisoner 1: Did you ever Figure out your powers? "
        escape_choice = raw_input(">")
        time.sleep(1)
        if escape_choice == "Y":
            print "Prisoner 1: You sit on a throne of lies."
            print "The Prisoner pulls out a rusty pipe and hits you"
            print "The Prisoner washes away as if it was just a memory"
            print "-1 life"
            lives = lives - 1
        elif escape_choice == "N":
            print "Prisoner 1: One of the things you can do is you have lives that regenerate over time. "
            print "Prisoner 1: They also regenerate if you do something that is worthy."
            print "+1 Lives"
            lives = lives + 1
            print "Prisoner 1: I have a gift for you as well."
            print "The Prisoner washes away as if it was just a memory and drops a pipe"
            print "Do you pick up the pipe?"
            weapon_choice = raw_input(">")
            if weapon_choice == 'y' or weapon_choice == 'Y':
                print "Gained Metal Pipe"
                metal_pipe = 1
            elif weapon_choice == 'n' or weapon_choice == 'N':
                print "Have you not your tetnaus shots?"
            else:
                print "Invalid Answer"
            print "Behind him 2 tunnels appear one on the right and one on the left."
        else:
            print "Not a valid choice Y or N for an answer"
            return "the_beginning"
        print ("Which Tunnel do you pick the left or the right")
        choice = raw_input(">")
        if choice == "left":
            return 'left_tunnel'
        if choice == "right":
            return 'right_tunnel'

class LeftTunnel(Scene):

    def enter(self):
        global lives
        print "You find a chest and wonder what's inside"
        print "The Lock looks to be some mastermind type game"
        right = lock.passcode()
        print right
        if right == 1:
            print "You open the chest to find a golden sword"
            print "You trun around and see a silverish, dragon"
            print "What do you do? hit"
            raw_input(">")
            print "The Sword shatters in your hands as you hit the dragon."
            if metal_pipe == "1":
                print "You pull out your last defense a metal pipe."
                print "You stab the dragon with your pipe and it turns into stone"
                lives = 10
                return 'death'
            else:
                print "The Dragon eats you and you go towards the light."
                return 'death'
        elif right == 0:
            print "The chest starts making a ticking sound."
            print "You try to run away but the chest explodes."
            lives = 0
            return 'death'


class RightTunnel(Scene):

    def enter(self):
        global lives
        print "You are walking through the tunnel and see a light"
        print "You notice that the cave is now made out of a solid vine like structutrue that is on fire."
        print "You try and run away but die and fall into the abyss below"
        lives = 0
        return 'death'

class Map(object):

    scenes = {
            'getting_to_know_everyone': GettingToKnowEveryone(),
            'the_beginning': TheBeginning(),
            'left_tunnel': LeftTunnel(),
            'right_tunnel': RightTunnel(),
            'death': Finish(),
        }
        
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('getting_to_know_everyone')
a_game = Engine(a_map)
a_game.play()