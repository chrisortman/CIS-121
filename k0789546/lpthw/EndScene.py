prompt = "> "
class Scene(object):

    def enter(self):
        print ""
        exit(1)
        

class End(Scene):

    def enter(self):
        print "Do you go in? -y/n-"
        move = raw_input(prompt)
        
        if move == "y":
            print "Good job you won!!! You survived and made it to the base"
            exit()
        elif move == "n":
            print "You turn back around and look for shelter but before you can"
            print "The dog comes back and kills you"
            exit()
        
        else:
            print "DOES NOT COMPUTE"
            return "end"   