import time
from Kill import Death

class echelon_zero(object):
    def enter(self):
        print "> You have just awoken in an underground cell. The lights are dimmed"
        print "> behind stone corners. God knows what time of day it is..."
        time.sleep(2)
        print "> Option 1: You could inspect the cell to see if there is"
        print "> anything of value with you (INSPECT_THE_CELL)."
        time.sleep(2)
        print "> Option 2: You could get some rest until something happens or until"
        print "> someone shows up by your cell (GO_TO_SLEEP)."
        time.sleep(2)