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
        print "You have died"
        return "finished"

class CentralCorridor(Scene):

    def enter(self):
        print "Entering central corridor."
        player_choice = raw_input("Do you want to go left or right?\n>")
        if player_choice == "left":
            return "laser_weapon_armory"
        elif player_choice == "right":
            return "the_bridge"
        else:
            print "Thats not a direction you can go, friend."
            return "central_corridor"

class LaserWeaponArmory(Scene):

    def enter(self):
        print "Entering laser weapon armory."
        print "As nice as the guns are there all locked up."
        print "You decide to head back to the previous room."
        return "central_corridor"

class TheBridge(Scene):

    def enter(self):
        print "entering bridge."
        print "There is a door on the far wall"
        player_choice_2 = raw_input("Whould you like to go forward or back?\n>")
        if player_choice_2 == "forward":
            return "escape_pod"
        elif player_choice_2 == "back":
            return "central_corridor"
        elif player_choice_2 == "window":
            window_choice = raw_input("Wait you relize its outerspace on the other side of the window, You sure you want to jump out?\n")
            if window_choice == "yes":
                print "Well its your funeral"
                return "death"
            else:
                print "Good choice"
                return "the_bridge"
            
        else:
            print "Thats not a direction you can go, friend."

class EscapePod(Scene):

    def enter(self):
        print "entering escape pod."
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