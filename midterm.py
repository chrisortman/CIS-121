import time
class Cell(object):
    print "> You have just awoken in an underground cell. The lights are dimmed"
    print "> behind stone corners. God knows what time of day it is..."
    time.sleep(2)
    print "> Option 1: You could inspect the cell to see if there is"
    print "> anything of value with you (INSPECT_THE_CELL)."
    time.sleep(2)
    print "> Option 2: You could get some rest until something happens or until"
    print "> someone shows up by your cell (GO_TO_SLEEP)."
    time.sleep(2)
    bit_zero = raw_input("> What do you do? ")
    if bit_zero == "GO_TO_SLEEP":
        time.sleep(2)
        print "> You go to sleep. As it turns out, your cellmate awoke and"
        print "> promptly killed you (ENDING #1)."
    if bit_zero == "INSPECT_THE_CELL":
        time.sleep(2)
        print "> You are in the company of your resting cellmate. He looks like"
        print "> a poor beggar. It would be very wise to avoid him..."
        time.sleep(2)
        print "> Option 1: You could kill him. (KILL_HIM)."
        time.sleep(2)
        print "> Option 2: You could escape. (ESCAPE)."
        time.sleep(2)
        bit_one = raw_input("> What do you do? ")
        if bit_one == "KILL_HIM":
            time.sleep(2)
            print "> You wake up from your childish nightmare. You still live"
            print "> out the motions from your dream and you come close to"
            print "> killing your wife. She screams and grabs the nightlamp and"
            print "> Swings for your head. You are clocked outback into a deep,"
            print "> deep sleep..."
            time.sleep(2)
            print "> You awake back in your cell, now assuming that this is a"
            print "> lucid dream where magical powers are at your disposal. You"
            print "> notice that your cellmate has left, and the cell gate is"
            print "> broken bent, lying on the ground beneath you..."
            time.sleep(2)
            bit_two = raw_input("> What do you do? ")
        if bit_one == "ESCAPE":
            time.sleep(2)
            print "> You try for the cell door. Its column bars are rusted and"
            print "> weak..."
            time.sleep(2)
            print "> Option 1: You could break the cell door (BREAK_DOOR)."
            time.sleep(2)
            print "> Option 2: You could climb through the door (CLIMB)."
            time.sleep(2)
            print "> Option 3: You could kill him (KILL_HIM)."
            time.sleep(2)
            bit_three = raw_input("> What do you do? ")
            if bit_three == "BREAK_DOOR":
                time.sleep(2)
                print "> You walk to the back of the cell and then charge"
                print "> towards the cell door. On impact, the column bars are"
                print "> crudely bent outward and there is a gap wide enough to"
                print "> escape. However, your shoulder is bleeding, and the"
                print "> cellmate has awoken."
                time.sleep(2)
                print "> Option 1: You could climb through the door (CLIMB)."
                time.sleep(2)
                print "> Option 2: You could kill him (KILL_HIM)."
                time.sleep(2)
            if bit_three == "CLIMB":
                time.sleep(2)
                print "> You try to slip through the column bars, but your"
                print "> lungs have too much air in them. You decide to exhale"
                print "> all of your breath and you make it halfway through the"
                print "> bars. Unfortunately, you panic, and your lungs lock"
                print "> you in place. Your cellmate is turning in his cot."
                time.sleep(2)
            if bit_three == "KILL_HIM":
                import Echo
                assert Echo.enput == 8
                time.sleep(2)
                assert Echo.enput == 2
                assert Echo.echo_mac == 1
                Echo.echo_work = "Screaming in agony!!!"