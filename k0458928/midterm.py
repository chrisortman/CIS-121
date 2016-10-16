from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
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

    quips = [
        "You died.  Better luck next time.",
         "Your mom would be proud...if she were smarter.",
         "LOSER",
         "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class RaceStart(Scene):

    def enter(self):
        print "You're at the start of the everest 500. The punishing track is topped with"
        print "a fresh dusting of snow. Your car, equipped with the finest parts money"
        print "can buy is ready to go. The only question is, are you?"
        print "\n"
        print "You and the five other races are signaled by the starter to fire up your engines."
        print "One racer is already out of the question due to the cold weather getting the"
        print "of his engine. You and four others still remain. You get out to a decent start"
        print "and find yourself in second place. You're approaching the first turn and may"
        print "have an outside line to get around the racer in first. The turn however, is hugged"
        print "by a deadly cliff. Do you take the outside lane and attempt to take the lead or"
        print "stay in the inside lane and remain behind the leader?"

        action = raw_input("> ")

        if action == "outside lane":
            print "You sweep to the outside lane and hit the gas, but your car loses control on"
            print "the snowy track and off the cliff you go."
            return 'death'

        elif action == "inside lane":
            print "Being the smart racer you are, you stay inside and remain behind the"
            print "leader. You know your opportunity to pass will eventually come. In second"
            print "place of five, you head down the track approaching an obstacle which"
            print "appears to be the exploding gates."
            return 'explosive_gates'

        else:
            print "THAT WON'T WORK!"
            print "You may enter 'outside lane', or 'inside lane'"
            return 'Race_start'
    
class ExplosiveGates(Scene):

    def enter(self):
        print "You and the others approach the six gates and pull into your designated slot."
        print "One slot is empty from the unforntunate racer at the beginning. The instructions"
        print "To pass the first obstacle read: 'Welcome to the exploding gates. As the name"
        print "says, these are gates that explode. If you don't wish to be blown up then you"
        print "must  enter the code into into the keypad on your computer in your vehicle. If you get the"
        print "code wrong 5 times then your gate will explode. After your first incorrect"
        print "answer you will be granted one hint.   The code consists of 3 integers."
        
        code = "%d" % (519)
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 5:
            print "BZZZZEDDD!"
            print "HINT: E A I"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "The gate opens and you race through into a long, straight stretch. You remain"
            print "in second place. Back in the direction of the gates, you hear an explosion."
            print "In your rearview mirror one two cars are visible. Four racers remain."
            return 'straight_stretch'
        else:
            print "The gate buzzes one last time and before you can even flinch your gate explodes."
            return 'death'



class Straightaway(Scene):

    def enter(self):
        print "You enter the straightaway in second place. This stretch covered with "
        print "snow so passing will be difficult, but you happen to have a full supply of nitrous oxide."
        print "You'll still have the downhill descent to try at passing the leader after"
        print "this stretch so passing isn't your only option.  Do you hit the nos and"
        print "go for the pass or follow the leader?"

        action = raw_input("> ")

        if action == "hit the nos":
            print "You hit the nos and accelerate past the leader. You have the lead"
            print "with not much race remaining. Immediately after taking the lead however,"
            print "the snow gets deeper. Due to the nos, you're traveling at too high of a"
            print "rate of speed. Your car loses control and rolls end over end 8 times"
            print "before exploding."
            return 'death'

        elif action == "follow the leader":
            print "You elect to go with the conservative approach knowing that an even"
            print "greater opportunity will later come. Right on the tail of the leader, you head"
            print "towards the last section of the race, the downhill descent."
            return 'downhill_descent'
        else:
            print "THAT WON'T WORK!"
            print "You may 'hit the nos' or 'follow the leader'"
            return "straight_stretch"


class DownhillDescent(Scene):

    def enter(self):
        print "The downhill descent is not in sight. The finish line is at the bottom of"
        print "the downhill descent so you'll need to make your move here. The downhill"
        print "descent consists of two steep, downhills lanes that both direct you to the"
        print "finish of the race. Lane 1 is a safe but narrow lane that you shouldn't"
        print "have any problem hitting the nos on. Lane 2 appears to be in much worse"
        print "condition but it's also an option. The leader chooses to head down lane 1."
        print "will you choose to make an attempt at getting around him in 1 or"
        print "blaze your own path through 2? Enter '1' or '2'"

        good_lane = "%d" % (2)
        guess = raw_input("[pod #]> ")


        if int(guess) != good_lane:
            print "You take a shot a lane 2 and hit the nos. At this point, you have no"
            print "control over your car and you're just begging to hit the finish line"
            print "in one piece. You car, spinning out of control enters the finish ilne"
            print "traveling backwards. You see the leader through your front windshield"
            print "which means that he is no longer the leader and that you won the race!"
            return 'finished'
        else:
            print "You follow the leader down lane 1 and then try to get around him but"
            print "lane 1 is too narrow! You run out of room and go right off the track"
            print "down a deep cliff."

            return 'death'

class Finished(Scene):

    def enter(self):
        print "You won! Good job. Please claim your prize at www.givememalware.com"
        return 'finished'
        
class Map(object):

    scenes = {
        'Race_start': RaceStart(),
        'explosive_gates': ExplosiveGates(),
        'straight_stretch': Straightaway(),
        'downhill_descent': DownhillDescent(),
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
        
a_map = Map('Race_start')
a_game = Engine(a_map)
a_game.play()
