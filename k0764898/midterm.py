from death import Death
from scene import Scene

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class LobbyRoom(Scene):

    def enter(self):
        print "There is a party at an old mansion that you had been invited to where"
        print "multiple people are dancing in the lobby where you decided to hang out."
        print "As you were taking a sip of your punch you noticed a drop in the number of people."
        print "This was very unusual because the punch table was near the door."
        print "As far as you knew no one had left the mansion which lead to suspicions."
        print "/n"
        print "you start walking towards the main staircase which leads to two"
        print "seperate hallways. As you were walking you hear a scream from the"
        print "left hallway and no sound at all from the right"
        print "now which hallway will you choose?"
        
        move = raw_input("> ")
        
        if move == "take right hallway":
           print "well going back down the staircase would look very akward."
           print "The left hallway seems to be a little dangerous so the right"
           print "hallway seems to be the best option to stay away from whats happening."
           print "As you were walking you notice a little girl crying in a old"
           print "worn out dress with it seemed to be a worn out teddy bear"
           print "you go over to talk to the little girl only to find your neck"
           print "being impaled by a dagger"
           return 'death'
        elif move == "take left hallway":
           print "you walk down this dark sketchy looking hallway knowing"
           print "that someone had to be in great danger from that scream."
           print "you continue down the hallway only to notice a man on his knees"
           print "who seemed to have recently proposed to his girlfriend."
           return 'The_Bathroom'
        else:
            print "Not a Choice"
            return 'Lobby_Room'
class TheBathroom(Scene):

    def enter(self):
        print "That was definetly a possible solution for the sudden dissapearances."
        print "On to another topic after all that punch that was drank you had to use the bathroom"
        print "Reluctantly there was a bathroom just past the newly proposed lovers."
        print "once entered into the bathroom you feel very out of the ordinary."
        print "As you look in the mirror you notice a creepy little boy standing behind you."
        print "you turn around seeing the boy holding a bloody hammer"
        print "What should you do?"
        
        move = raw_input("> ")
        
        if move == "kick":
           print "you try kicking only to find your leg being hammered you then try"
           print "getting up only to find your other leg being hammered. With no legs"
           print "You try whipping your fists at him you miss and get brutally hammered"
           return 'death'
        elif move == "run as fast as possible":
           print "As soon as the little boy starts motioning forward you go into a dead sprint"
           print "out of the door and through the hallway. When you look back the boy is no longer behind"
           print "you. Well looks like you could have just been imagining things."
           print "You make your way back into the lobby only to see that everyone was fine."
           print "Well since you were either seeing things or there may be serial killer it was"
           print "definetly a good time to head home. You then head for the door."
           return 'The_Exit'
        else:
           print "Not a Choice"
           return 'The_Bathroom'
         
class TheExit(Scene):

    def enter(self):
        print "As you start to open the door it seems to be locked from the outside"
        print "Starting to panic you alarm the people dancing that they were trapped"
        print "Multiple people came up and tried opening the door unlocking the locks and"
        print "relocking them to make sure it was indeed stuck."
        print "once you turn around you see the little boy and a new girl with blood stained clothes"
        print "standing at the bottom of the staircase. In this moment what shall you do?"
        
        move = raw_input("> ")
        
        if move == "jump through window":
           print "you try jumping through the window only to have glass penetrate your skin"
           print "which then leads to you bleeding out while people trample over your body."
           return 'death'
        elif move == "gang up and attack":
           print "you convince the others that it was like 30 to 2 and these kids were clearly"
           print "serial killers. Everyone then rushes in together and they soon find out that"
           print "these kids were skilled with weapons and were swatting down the whole crowd like"
           print "flies untill they came to you where they easily beat you to nothin"
           return 'death'
        elif move == "trick them":
           print "you tell the little boy and girl you have candy in your car. They then nod their heads"
           print "and unlock the door. They then follow you to the car and you tell them its in the backseat."
           print "as there searching you simply close and lock the door giving you just enough time to make your"
           print "escape"
           return 'finished'
        else:
           print "Not a Choice"
           return 'The_Exit'
class Finished(Scene):

    def enter(self):
        print "Great job you have completed the game"
        return 'finished'

class Map(object):

    scenes = {
        'Lobby_Room': LobbyRoom(),
        'The_Bathroom': TheBathroom(),
        'The_Exit': TheExit(),
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

a_map = Map('Lobby_Room')
a_game = Engine(a_map)
a_game.play()