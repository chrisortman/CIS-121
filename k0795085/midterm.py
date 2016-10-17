from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Death(Scene):

    quips = [
        "You died.  You kinda suck at this.",
         "Your mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
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

class CentralCorridor(Scene):

    """def enter(self):
        print "You Wake up in a cave, it is cold and youre wearing rags. There is blood on the ground but it isnt yours, you must have wounded the bear when you stabbed it with your dagger. You remember you were exploring the cave when you heard a noise behind you and thats when the bear attacked. You decide your goal is to leave the cave."
       
        action = raw_input("> ")

        if action == "left":
            print "You dont get too far before you hear noises. Faint bumps and groans but as you get closer you find a door. You decide to open it because there is a little warmness radiating off of it. You open it and you there is a snap. You dont exactly feel the arrow pierce your skull but it still does." 
            return 'death'

        elif action == "right":
            print "You walk down a dimly lit path and feel your legs go out from under you, but you start to feel the wind on your face and before you realize youre falling you splat all over the ground."
            return 'death'

        elif action == "straight":
             print"You wander off down a dark corridor and find a chest with clothes and a dagger. You put on the clothes and feel the releif of warmness. You look to the right of you and there is a crypt with man standing with his back to you. Depending on your  morality, his life is in your hands" 
             return 'laser_weapon_armory'  

        else:
            print "Your options are, left, right or straight"
            return 'central_corridor'
            

class LaserWeaponArmory(Scene):
          
    def enter(self):
        print "You decide to spare the man and confront him. He explains he is trapped as well but there is a gate and you have to randomly guess the gates password. You look around the room for clues you find a book and it has the numbers 963 written in it."
            
        code = "%d" % (936)
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "You hear a crash and the crypt starts to shake"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "The man turns to you and draws his sword he asks for all your items. You explain how you got there and how you have nothing and he decides that he may as well kill you to reduce witnesses." 
            return 'the_bridge'
        else:
            print"The crypt caves in killing both you and the man."
            return 'death'



class TheBridge(Scene):

    def enter(self):
        print "You have ot make a split second decision, you draw the dagger and think to yourself you have to throw the dagger or try to take him in a duel."

        action = raw_input("> ")

        if action == "duel":
            print "You go to slash at him but the hilt isnt strong enough and his sword breaks it cutting your hand in half. In one swift motion he does a spin move and cuts your head in half just above the mouth"
            return 'death'

        elif action == "throw the dagger":
            print "Throwing knives has never been your specialty but you decide its your best shot. You flip the knife around in your hand and throw it as hard as you can. The hilt hits him in the forehead and he starts to charge. You go into the fetal positiona nd you hear a breath and the noise of a sword going through flesh, he slipped on a rock and killed himself. You pry the sword out of him and move on."
            return 'escape_pod'
        else:
            print "Your options are slash or throw the dagger"
            return "the_bridge"""


class EscapePod(Scene):

    def enter(self):
        print "You run through the gate abut the way out is blocked by another gate, there are 5 levers to choose from."

        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")


        if int(guess) != good_pod:
            print "You pull lever %d and an arrow shoots out of the wall behind you and hits you in the back you soon bleed out." % guess
            
            return 'death'
        else:
            print "You pull lever %d and the door opens and light floods the cave you rush out of the cave only to be shot dead by a city gaurd." % guess

            return 'finished'

class Finished(Scene):

    def enter(self):
        print "You die either way there is no winning"
        return 'finished'
        
class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
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
        
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()