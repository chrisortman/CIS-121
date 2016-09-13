from string import swapcase
from string import replace

def prancercise(hi):
    old = "_"
    new = " "
    x = swapcase(hi)
    return replace(x, old, new)
    
    


dash = "-"

transformed = prancercise("say_hi_to")
print dash*10, transformed, dash*10