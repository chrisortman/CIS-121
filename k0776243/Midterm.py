# Skeletons invade pirate ship.  Hero is stuck in bottom of ship and has to escape, get off the boat and to the island.  
from sys import exit
from random import randint
from ship import Ship

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)


class Water(object):
    
    def enter(self):
        print "You're swimming in the water."
        print "You're going to run out of energy and drown."
        print "Choose between 1. swimming to the island, 2. riding the shark to the island, or 3. following ADHD and seeing...wait was that a blue dot?"
        
        action = raw_input("Choose number between 1-3> ")
        
        if action == "1":
            print "You start breast crawling to the faraway island."
            print "Your lungs start dragging at the cold air."
            print "You start to sink and drown dead."
            print "You have one life left."
           
            return 'island'
        
        elif action == "2":
            print "You straddle the shark and he starts to swim."
            print "But sharks have no sense of direction."
            print "You go in circled til you get dizzy, fall into the water and hit your head on the boulder and die."
            print "You have one life left."
            
            return 'island'
            
        elif action == "3":
            print "You see something blue and swim after it."
            print "Turns out it's a mermaid tail and so you ride the mermaid."
            print "You have arrived at the island."
           
            return 'island'

class Island(Scene):
    
    def enter(self):
        print "You are now on the island."
        print "You need to signal for help."
        print "You have to choose to 1.set a palm tree aflame, 2. blow tar bubbles, or 3. eat bananas."
        
        action = raw_input("Choose number between 1-3>")
    
        if action == "1":
            print "You douse a palm tree with oil and set it on fire."
            print "It explodes in your face and you die."
            print "Well, sucker, you just lost."
            
        
        elif action == "2":
            print "You start blowing bubbles made of tar."
            print "It's working.  They are rising and creating a cloud above the island."
            print "Then you accidentally inhale the tar and it gets stuck in your lungs."
            print "You die a slow death.  Well, sucker, you just lost."
            
        elif action == "3":
            print "You go and eat bananas out of boredom."
            print "You are climbing a tree and accidentally knock a coconut into a live volcano."
            print "It erupts and creates a huge signal.  Surprisingly, you're fine."
            print "The British navy comes to your rescue."
            print "You win!!!"
        
        return "finished"

class Finished(object):
    def enter(self):
        print "done!"
        exit(0)
    
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            print "next scene is %s" % next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Map(object):

    scenes = {
        'ship': Ship(),
        'water': Water(),
        'island': Island(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
        
a_map = Map('ship')
a_game = Engine(a_map)
a_game.play()