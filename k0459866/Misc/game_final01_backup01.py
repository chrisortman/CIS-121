# Line 2-36 was basically copied from example 43 on learnpythonthehardway.org
# INTRO
from sys import exit
from random import randint
import random

# print """
# You awaken in a strange land, you don't know how you go there and you don't know why.
# A man appears, he says,
# "Greetings traveller, you seemed to have come to our lands in a strange time."
# He continues on for a few seconds longer, but he is then interrupted by a strange flash of light.
# "I am sorry, but I must leave, here is a sword and a book of ancient knowledge."
# He then tells you to navigate the forest infront of you to reach the nearest town.
# The man then vanishes before your eyes.
# You take a few steps forward, preparing to enter the strange forest.
# The path continues for a few more feet, then seemingly stops.
# You look around, and can't tell which direction you're facing.
# The woods seems to shift and change.
# You take a deep breath and prepare for the long trek through these forboding timbers.
# There's no turing back now.
# """

class Scene(object):
    
    def enter(self):
        print "Not Availiable"
        exit(1)
    
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
    
    fatality = [
        "It's all over.",
        "The end is here.",
        "You've died.",
        "This is the end.",
        ]
        
    def enter(self):
        print Death.fatality[randint(0, len(self.fatality)-1)]
        exit(1)

class Forest(Scene):
    
    def enter(self):
        print "Do you go left or right?"
        
        action = raw_input("> ")
        
        if action == "left":
            print "You go left."
            return 'forestl01'
            
        elif action == "right":
            print "You go right."
            return 'forestr01'
            
        elif action == "go back":
            print """
You look around, only to see flatlands all around you.
There's no where else you could go but forward.
            """
            return 'forest'
            
        else:
            return 'forest'
################################################################################
# LEFT 1
class ForestL01(Scene):
    
    def enter(self):
        print """
You walk for a good mile through the clearing.
It appears you've made the right choice.
You continue to walk, only to come across a silent stream.
Will you swim across, wait, or check your items?
        """
        
        action = raw_input("> ")
    
        if action == "swim across":
            print """
All of a sudden, the stream turns into a rushing waterfall."
You try to struggle and swim to an egde, but all of the edges seemingly vanish.
The waterfall swallows you.
            """
            return 'death'
        
        elif action == "swim":
            print """
All of a sudden, the stream turns into a rushing waterfall.
You try to struggle and swim to an egde, but all of the edges seemingly vanish.
The waterfall swallows you.
            """
            return 'death'
    
        elif action == "wait":
            print """
You decide to sit down and wait.
You sit there for a few hours, but nothing happens.
It seems that waiting doesn't really do much right now.
        """
            return 'forestl01'
        
        elif action == "check items":
            print """
What do you want to look at?
You have:
tome
sword
lint
            """
            items = raw_input("> ")
            if items == "sword":
                print """
You unsheathe your sword.
As you observe it, it seems quite plain.
Hilt, blade, grip, nothing really catches your eye.
                """
                return 'forestl01'
            
            elif items == "lint":
                print """
What could this be?
Looking closer at it, you realize it's just pocket lint.
A disappointed look streches across your face.
You think it might come in handy some how.
You put it back in your pocket.
            """
                return 'forestl01'
            
            elif items == "tome":
                print """
You take a look inside the mysterious tome given to you earlier.
Flipping through the pages, your eyes seem to lock in on a specific page.
The page has a strange rune on it.
Coincidentally, the rune appears in front of you, on a patch of dead grass.
Stepping towards the rune, a patch of ice forms across the stream.
There is now a path available.
You continue forward.

After walking for a few minutes, the path splits yet again.
                """
                return 'forestl02'
                
        else:
            return 'forestl01'

# LEFT 2
class ForestL02(Scene):
    
    def enter(self):
        print "Do you go left or right?"
        
        action = raw_input("> ")
        
        if action == "left":
            print """
You start to go left, but you're cut off by an invisible barrier.
You take a few steps back.
            """
            # Possible easter egg/different ending?
            return 'forestl02'
            
        elif action == "right":
            print """
The path winds around many strange trees and stones.
After a few curves in the road, a mile long stretch comes into view.
After walking for what seems like forever, something appears.
A strange figure, covered in shadow with flaming red eyes, equiped with a strange weapon.
It doesn't look friendly.
It immediately dashes towards you.
            """
            return 'forestl03'

# LEFT 3
class ForestL03(Scene):
    def enter(self):
        print "You have enough time to make a move."
#        print 'If you need help with combat, type "tips"'
        
        action = raw_input("> ")
        
#         if action == "tips":
#             print """
# Combat works as follows:
# A list of abilities will be listed for you.
#             """
#             return 'forestl03'
        if action == "swing":
            print """
You swing your sword at the figure.
            """

class FinishedL(Scene):

    def enter(self):
        print "You won! Good job."
        return 'finished'
################################################################################
# RIGHT
class ForestR01(Scene):
    
    def enter(self):
        print
    
    
class FinishedR(Scene):

    def enter(self):
        print "You won! Good job."
        return 'finished'
################################################################################
# MAPPING
class Map(object):

    scenes = {
        'forest': Forest(),
        'forestl01': ForestL01(),
        'forestl02': ForestL02(),
        'forestl03': ForestL03,
        'death': Death(),
        'finishedl': FinishedL(),
        'finishedr': FinishedR(),
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('forest')
a_game = Engine(a_map)
a_game.play()