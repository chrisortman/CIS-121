from scene import Scene

class MainRoom(Scene):
    def enter(self):
        
        start = """
        You are in a dark room with 3 doors. 
        On the left there is a red door. 
        In the middle, a green one. 
        The door on the right is blue.
        Choose a door.
        """
        
        idk = "I don't know what that means."
        ch1 = "Blank"
        ch2 = "Blank"
        
        
        print start
        
        #color choice rgb
        while ch1 != "red" and ch1 != "green" and ch1 != "blue":
           
            ch1 = raw_input("ch1>")
            
            return ch1
            
