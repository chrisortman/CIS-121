# Skeletons invade pirate ship.  Hero is stuck in bottom of ship and has to escape, get off the boat and to the island.  
from sys import exit
from random import randint

class Ship(object):
    
    def enter(self)
        print "You're stuck in the bottom of the ship and it's filling rapidly with water."
        print "Choose between: a crowbar, the trapdoor key, or broccoli."
    
    action = raw_input("> ")
    
    if action == "crowbar":
        print "You bash the crowbar into the overhead trapdoor."
        print "You pry it open and a skeleton sees you and stabs you."
        print "You die.  You have two lives left."
        
    elif action == "trapdoor key":
        print "You find the key and unlock the trapdoor."
        print "Once you get out in the open, you run for it, promptly fall in a puddle and off the ship."
        print "There's a shark in the water.  You die.  You have two lives left."
        
    elif action == "broccoli":
        print "You find stale broccoli."
        print "You make friends with the shark through a window and he bashes it open.  You're free."
        


class Water(object):
    
    def __init__(self, scene_map):
        print "You're swimming in the water."
        print "You're going to run out of air."
        print "Choose between swimming to the island, riding the shark to the island, or following ADHD and seeing...wait was that a blue dot?"
        
        action = raw_input("> ")
        
        if action == "swim to island":
            print "You start breast crawling to the faraway island."
            print "Your lungs start dragging at the cold air."
            print "You start to sink and drown dead."
            print "You have one life left."
        
        elif action == "ride shark to island":
            print "You straddle the shark and he starts to swim."
            print "But sharks have no sense of direction."
            print "You go in circled til you get dizzy, fall into the water and hit your head on the boulder."
            print "You have one life left."
        
        elif action == "follow ADHD":
            print "You see something blue and swim after it."
            print "Turns out it's a mermaid tail and so you ride the mermaid."
            print "You have arrived at the island."

class Island(Scene):
    
    def enter(self):
        print "You are now on the island."
        print "You need to signal for help."
        print "You have to choose between setting a palm tree aflame, blow tar bubbles, or eat bananas."
        
    action = raw_input(">")
    
    if action == "set palm tree aflame":
        print "You douse a palm tree with oil and set it on fire."
        print "It explodes in your face and you die."
        print "Well, sucker, you just lost."
        
    elif action == "blow tar bubbles":
        print "You start blowing bubbles made of tar."
        print "It's working.  They are rising and creating a cloud above the island."
        print "Then you accidentally inhale the tar and it gets stuck in your lungs."
        print "You die a slow death.  Well, sucker, you just lost."
        
    elif action == "eat bananas":
        print "You go and eat bananas out of boredom."
        print "You are climbing a tree and accidentally knock a coconut into a live volcano."
        print "It erupts.  You're fine."
        print "The British navy comes to your rescue."
        print "You win!!!"
