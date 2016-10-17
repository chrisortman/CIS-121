from sys import exit
from EndScene import Scene, End, prompt

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("End")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()
        
class FrontDoor(Scene):

    def enter(self):
        print "There was a major epidemic of a fatal disease, you have been in quarantine for months"
        print "they told you the air was still toxic and going outside will kill you"
        print "you haven't had any contact with the outside world for all that time"
        print "you find a way to escape but you only have a few minutes until someone notices you're gone"
        print "when you get to the door you open it and walk out"
        print "you can -walk- and explore or you can -run- and try not to get caught by the people who trapped you"
        print "what do you do?"

        move = raw_input(prompt)
        
        if move == "walk":
            print "The first thing you notice is that the air isn't toxic anymore"
            print "as you start walking you can see the city is abandoned and destroyed"
            print "you don't get very far because an infected survivor jumps out, infects you and kills you"
            exit()
        if move == "run":
            print "You run to the nearest car"             
            print "you start the engine and begin driving"
            return "driving"
            
        else:
            print "DOES NOT COMPUTE!"
            return "front_door"
            
class Driving(Scene):

    def enter(self):
        print "The street you drive along is completely empty"
        print "with abandoned cars on the side of the road"
        print "there is a store on the corner of the street"
        print "it looks like it might have some supplies left"
        print "do you -go to the store- or -keep driving-"
        
        move = raw_input(prompt)

        if move == "go to the store":
            return "store"

        elif move == "keep driving":
            print "You see the blinking gas light come up on the dash board"
            print "After a couple of minutes you run out of gas and come to a stop"
            print "The air conditioning stops working, you feel the cold air in your hands"
            print "You look around the car and see that there is no food or supplies"
            print "You decide to walk back to the store and look for suplpies"
            return "store"
            
        else:
            print "DOES NOT COMPUTE!"
            return "driving"


class Store(Scene):

    def enter(self):
        print "You enter the store"
        print "there are very few supplies left on the shelves"
        print "You grab a coat, a backpack, some food and a knife"
        print "You see there is a back room"
        print "Do you -enter the rooom- or do you -walk out- of the store"
        
        move = raw_input(prompt)
        
        if move == "enter the room":
            print "The room is filled with more supplies and food"
            print "There is a working radio and when you try it you see it works and are able"
            print "to communicate with another survivor, they tell you where they have been hiding out"
            print "and you decide to go there"
            print "Before you go they warn you to watch out for dangerous survivors and they tell you"
            print "to find a weapon just in case"
            return "outside"
        elif move == "walk out":
            print "Outside the store you see that your car is gone!"
            print "you hear a noise behind you and you think you see some people in the distance"
            print "You get shot by a survivor and die"
            exit()
        else:
            print "DOES NOT COMPUTE"
            return "store"
class Outside(Scene):
    def enter(self):
        print "You walk out of the store and you hear voices in the distance"
        print "you remember what they told you on the radio and start running"
        print "they see you and chase after you"
        print "Do you find a place to -hide- or try to -outrun- them?"
        move = raw_input(prompt)
        
        if move == "hide":
            print "You go into an abandonded biulding and find a hiding spot"
            print "You hear them come in after you and you wait until they leave"
            print "It starts to get dark so you decide to stay there for the night"
            return "secondday"
        
        elif move == "outrun":
            print "You run as fast as you can but they catch you and eat you"
            exit()
            
        else:
            print "DOES NOT COMPUTE"
            return "outside"
            
class SecondDay(Scene):
    def enter(self):
        print "When you wake up you eat something from your backpack and continue on your journey"
        print "You walk out of the building and start waking toward the base where they told you to go"
        print "After a couple of hours of walking you come across a dog that looks injured"
        print "Do you stop and try to -help the dog-? or do you -keep going-?"
        move = raw_input(prompt)
        
        if move == "help the dog":
            print "As you aproach the dog you take some food out of your backpack"
            print "when you try to give it food the dog bites in the leg and you die of infection"
            exit()
        elif move == "keep going":
            print "Not too long after you come across the dog you finally arrive at the subway"
            print "station they told you to go, you stare at it and decide whether or not to go in"
            return "end"
            
        else:
            print "DOES NOT COMPUTE"
            return "secondday"
        
        
class Map(object):

    scenes = {
        "front_door": FrontDoor(),
        "store" : Store(),
        "driving": Driving(),
        "outside" : Outside(),
        "secondday" : SecondDay(),
        "end" : End()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
a_map = Map('front_door')
a_game = Engine(a_map)
a_game.play()