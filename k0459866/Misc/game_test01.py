# Line 2-36 was basically copied from example 43 on learnpythonthehardway.org
# INTRO
from sys import exit
from random import randint
import random
import time

# Global variables
kharlas = False
gold_list = [0,1,2,3,4,5,6,7,8,9,10]
gold = 0
bad_karma = 0
good_karma = 0
sword_damage = [0,1,2,3]
pirate_damage = [0,0,1,2,3,4]
kharlas_health = 10
your_health = 10

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
            print "Try again"
            print ""
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
            print "Try again"
            print ""
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
            time.sleep(5)
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
        print """
As you make your way down the path, the trees start to shift.
The path begins to narrow, and the trees seem to grow taller.
A chill starts to run up your spine.
You hear whispers in your ear, they say,
"Join us"
"You know you want to"
"When He comes, all who oppose him will suffer"
You jump, and you draw your sword.
You aren't certain, but something must be here.
What do you do?
swing sword
use tome
cower
        """
        
        action = raw_input("> ")
        
        if action == "cower":
            print """
You can't take this madness.
You break down and curl up into a ball.
You hear the whispers, they shift into booming, pitiful laughter.
"Those with weak will shall be crushed"
Your panicked breaths turn into heavy coughing.
As the world fades, you only hear laughter.
Unrelenting, unfeeling, laughter.
            """
            return 'death'
            
        elif action == "swing sword":
            print """
You take your sword and begin to swing it wildly.
After a few swings, the darkness begins to fade.
A gentleman is sitting on a tree stump to your left.
It doesn't seem like he noticed you.
You feel a strange force acting upon you.
A voice rings in your head.
It tells you to do things.
Violent things.
            """
            global bad_karma
            bad_karma = bad_karma + 1
            return 'forestr02'
            
        elif action == "use tome":
            print """
In your panic, you draw out the tome.
It seems, that in this dark mist surrounding you, the tome dimly shines.
It immediately swings open, and something happens.
A beam of light shines upwards from the tome.
It destroys all of the darkness around you.
You see the world as it was meant to now.
A gentleman is sitting on a tree stump to your left.
You feel a strange force acting upon you.
A voice rings in your head.
It tells you to do things.
It promises rewards to those who follow the rules.
You can't help but chuckle a bit at the absurd, off-topic comment.
            """
            global good_karma
            good_karma = good_karma + 1
            return 'forestr02'
            
        else:
            print "Try again"
            print ""
            return 'forestr01'

class ForestR02(Scene):
    
    def enter(self):
        print "Do you approach the man?"
        
        action = raw_input("> ")
        
        if action == "no":
            print """
You stand there, looking around.
Nothing else really happens.
            """
            return 'forestr02'
            
        elif action == "yes":
            print """
You walk towards the man.
As you're walking towards him, he stands up.
It doesn't seem like he notices you.
He starts to walk, only to drop a sheathed item.
Intended for you perhaps?
            """
            return 'forestr03'

class ForestR03(Scene):
    
    def enter(self):
        print """
What do you do?
help
stab
step back
        """
        
        action = raw_input("> ")
            
        if action == "help":
            print """
You jog over to the man, and help him pick up his things.
Although he looks intimidated by your presence, he looks nice.
He thanks you for helping him, and tells you a story.
            """
            time.sleep(5)
            global good_karma
            good_karma = good_karma + 1
            return 'roguestory'
            
        elif action == "step back":
            print """
You take a step back, letting the man pick up his items.
While you didn't help him, you also didn't approach him.
As he walks away, he looks back at you, and eyes you and your belongings.
He looks away, then vanishes, into thin air.
You turn around, ready to move forward.
            """
            print "You can go left or right."
                
            action2 = raw_input("> ")
                
            print """
You start to move, but something happens!
A figure leaps out of the brush and slashes at you with two menacing swords.
"No one ignores the Dread blade like that!"
You dodge his attack, but there's more where that came from.
You firmly grasp your sword, ready to swing.
            """
            return 'your_turn'
            
        elif action == "stab":
            print """
You see the weapon on the ground, and charge the man.
He grabs the weapon off the ground, and prepares to fight.
You are too fast, however, and you stab the man in the chest.
He laughs at you, and tells you that you made a mistake.
He then vanishes into thin air.
You turn around, ready to move forward.
                """
            print "You can go left or right."
                
            action2 = raw_input("> ")
                
            print """
You start to move, but something happens!
A figure leaps out of the brush and slashes at you with two menacing swords.
"No one ignores the Dread blade like that!"
You dodge his attack, but there's more where that came from.
You firmly grasp your sword, ready to swing.
            """
            return 'your_turn'
            
        else:
            return 'forestr03'

class Story(Scene):
    
    def enter(self):
        print "Do you want to listen to the story?"
        
        action = raw_input("> ")
        
        if action == "no":
            print """
You tell the man that you have a tight schedule.
He looks annoyed, but understands regardless.
            """
            global kharlas
            kharlas = True
            return 'forestr05'
            
        elif action == "yes":
            print "The man begins to go into a long story."
            print """
"Ya may be wonderin what a ol' man be doin out in this here forest, lad.
But not everything's as it seems.
I'm not no ordinary man, but I be a pirate.
Not just a pirate, but a captn!
Oh how I do miss the days on the high sea lad."
            """
            print """
"What's me name?
I went by many in my day.
The Cursed Sailor, The Dead Captain, The Dread Blade..."
The old pirate looks at his swords.
            """
            print """
"Ya see lad, these be no ordinary blades, these...
... these be the Dreadblades!"
The pirate quickly draws his swords, a black mist surrounding them.
"These be the blades that formed an empire.
Won countless battle.
Fell countless challengers."
            """
            print """
The pirate sheathes the Dreadblades underneathe his cloak.
"But those days be long over."
            """
            print """
The pirate looks at you once again.
"Oh ho! But you be lookin a little lonely there me matey!
Tell ya what, how about I tag along with ye, atleast for a little bit.
Let me show ya the kindness you've shown me!"
The pirate looks like he'll accompany you, for a little while.
"By the way, me name be Kharlas, lad.
Come, let's get a move on then!"
            """
            global kharlas
            kharlas = True
            return 'forestr05'

class Your_Turn(Scene):
    
    def enter(self):
        print """
What do you do?
slash
stab
swing
        """
        
        if kharlas_health <= 0:
            print """
With a final swing, the pirate falls.
His weapons fall to his side, with a thud.
The old man lies there, with no life left in him.
            """
            global gold
            gold = gold + random.choice(gold_list)
            global bad_karma
            bad_karma = bad_karma + 5
            return 'forestr04'
            
        elif your_health <= 0:
            print """
With maniacal laughter, the man swings at you.
You dodge him, but you stumble, due to your wounds.
As you fall to the ground, you feel a sharp pain pierce your chest.
            """
            return 'death'
            
        action = raw_input("> ")
        
        if action == "swing":
            hit1 = random.choice(sword_damage)
            if hit1 == 0:
                print """
You swing your sword at the man.
He dodges to the left, and you miss completely.
You prepare for his counter attack.
                """
                return 'pirate_turn'
            elif hit1 == 1:
                print """
You swing your sword at the man.
He tries to dodge, but you barely catch him in the arm.
It's not a deadly blow, but he's bleeding.
                """
                kharlas_health = kharlas_health - hit1
                return 'pirate_turn'
            elif hit1 == 2:
                print """
You swing your sword at the man.
He tries to parry the blow, but you strike true.
He's brought back by the clashing of steel.
While he tries to recover, you quickly swing at him.
He's caught in the back, quite a nasty cut.
                """
                kharlas_health = kharlas_health - hit1
                return 'pirate_turn'
            elif hit1 == 3:
                print """
You swing your sword at the man.
You swing past his defenses, and hit him with some force.
He groans with pain, but years of combat have hardened his fortitude.
                """
                kharlas_health = kharlas_health - hit1
                return 'pirate_turn'
                
        elif action == "stab":
            hit2 = random.choice(sword_damage)
            if hit2 == 0:
                print """
You try to stab at the man.
He dodges to the left, and you miss completely.
You prepare for his counter attack.
                    """
                return 'pirate_turn'
            elif hit2 == 1:
                print """
You try to stab the man.
He tries to dodge, but you barely catch him in the arm.
It's not a deadly blow, but he's bleeding.
                """
                kharlas_health = kharlas_health - hit2
                return 'pirate_turn'
            elif hit2 == 2:
                print """
You try to stab the man.
He tries to parry the blow, but you strike true.
You stab him in the stomach.
He wraps his hand around the wound, but then retaliates.
                """
                kharlas_health = kharlas_health - (hit2 + 1)
                return 'pirate_turn'
            elif hit2 == 3:
                print """
You try to stab the man.
He's completely taken by surprise, and you stab him.
A deep wound, right in the arm.
Bleeding a lot.
                """
                kharlas_health = kharlas_health - (hit2 + 1)
                return 'pirate_turn'
                
        elif action == "slash":
            hit3 = random.choice(sword_damage)
            if hit3 == 0:
                print """
You try to slash at the man.
He counters your attack, deflecting your blow.
Your hands shake, but your unharmed.
Same goes for the man
                """
                return 'pirate_turn'
                
            elif hit3 == 1:
                print """
You try to slash at the man.
The two of you lock into a quick duel.
Slashing back and forth, you manage to catch him in the arm.
He, also, catches you in the arm.
He jumps back, preparing for an attack.
                """
                kharlas_health = kharlas_health - hit3
                your_health = your_health - hit3
                return 'pirate_turn'
                
            elif hit3 == 2:
                print """
You try to slash at the man.
The both of you lock into a duel.
The clashing of steel ensues.
After many parrying blows, you manage to hit the man.
After you strike him, he leaps backwards, preparing an attack.
                """
                kharlas_health = kharlas_health - hit3
                return 'pirate_turn'
                
            elif hit3 == 3:
                print """
You try to slash at the man.
As he tries to parry your attacks, a thick shadow surrounds you.
The man is no where to be seen.
Laughter assaults your ears, and after a few moments, he's on you.
Fighting with extreme vigor, the man tries to end the fight.
You aren't so easily defeated, however...
As he goes for the final blow, you evade him.
Jumping behind him, you wildly slash at his back.
He writhes with pain, but kicks you, knocking you back.
The fog around you disapates.
You recover, preparing for the man's attack.
                """
                kharlas_health = kharlas_health - (hit3 + 2)
                return 'pirate_turn'
                
        else:
            return 'pirate_turn'

class Pirate_Turn(Scene):
    
    def enter(self):
        random.choice(pirate_damage)
        if pirate_damage == 0:
            print """
The man jumps at you, attempting to stab you.
You dodge his attacks, and he moves backwards.
            """
            return 'your_turn'
            
        elif pirate_damage == 1:
            print """
The man bounds towards you, both swords at the ready.
Although you deflect most of his blows, he manages to make a quick punch.
Caught off guard, he slashes you across the arm.
            """
            your_health = your_health - pirate_damage
            return 'your_turn'
            
        elif pirate_damage == 2:
            print """
The man pulls out a strange vial.
Pulling off the cork, he drinks the vial, and then charges forward at you.
With no time to react, he slices you in the leg.
            """
            kharlas_health = kharlas_health + 1
            your_health = your_health - pirate_damage
            return 'your_turn'
            
        elif pirate_damage == 3:
            print """
The man rolls a pair of dice towards you.
A five and a two.
Out of no where, you feel a dagger enter your back.
            """
            your_health = your_health - (pirate_damage + 1)
            return 'your_turn'
            
        elif pirate_damage == 4:
            print """
The man rolls a pair of dice towards you.
Snake eyes.
Suddenly, the man is upon you.
Wildly slashing your body, you can't help but stand there.
After what seems like an eternity, he stops, and steps back.
The pain is almost unberable.
You stand up, and prepare an attack.
            """
            your_health = your_health - (pirate_damage + 1)
            return 'your_turn'
            
        else:
            return 'your_turn'

class ForestR04(Scene):
    
    def enter(self):
        pass

class ForestR05(Scene):
    
    def enter(self):
        pass


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
        'forestr01': ForestR01(),
        'forestl02': ForestL02(),
        'forestr02': ForestR02(),
        'forestr03': ForestR03(),
        'roguestory': Story(),
        'forestl03': ForestL03,
        'your_turn': Your_Turn(),
        'pirate_turn': Pirate_Turn(),
        'forestr04': ForestR04(),
        'forestr05': ForestR05(),
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