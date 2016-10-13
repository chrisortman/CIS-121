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

        # be sure to print out the last scene
        current_scene.enter()

class Finished(Scene):

    def enter(self):
        print "You won! Good job."
        return 'finished'

class Death(Scene):

    def enter(self):
        print "entering death scene"
        return "finished"

class CentralCorridor(Scene):

    def enter(self):
        print "entering central corridor scene"
        player_choice = raw_input("Do you want to run or fight?")
        if player_choice == "fight":
            return "laser_weapon_armory"
        else:
            return "escape_pod"

class LaserWeaponArmory(Scene):

    def enter(self):
        print "entering laser weapon armory scene"
        return "escape_pod"

class TheBridge(Scene):

    def enter(self):
        print "entering bridge scene"
        return "finished"

class EscapePod(Scene):

    def enter(self):
        print "entering escape pod scene"
        return "finished"


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