import variables
from main_room import MainRoom
from red_room import RedRoom
from green_room import GreenRoom
from blue_room import BlueRoom


from scene import Scene
variables 


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            if next_scene_name is None:
                print "You are missing a return statement in your room"
                
            #print "next scene name is %s" % next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()
        

class Finished(Scene):

    def enter(self):
        print "You won! Good job."
        return 'finished'
        
class Map(object):
    
    scenes = {
        'main' : MainRoom(),
        'red' : RedRoom(),
        'green' : GreenRoom(),
        'blue' : BlueRoom(),
        'finished' : Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        #print "--", scene_name
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('main')
a_game = Engine(a_map)
a_game.play()