step06l = str(raw_input("What would you like to do?\n"))
if (step06l == "go to the inn"):
    print """
The inn appears to be vacant at the moment.
You take a step back.
                            """
    step06l = str(raw_input("What would you like to do?\n"))
    if (step06l == "go to the inn"):
        print """
The inn isn't open, maybe you should talk to the people.
        """
        step06l = str(raw_input("What would you like to do?\n"))
if (step06l == "talk"):
    print """
You walk up to a group of villagers.
They greet you with a hearty "Hello".
                            """
step06lt = str(raw_input("What do you want to talk about?\n"))