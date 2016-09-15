from string import upper
from string import replace


def prancercise(hi, dash):
    big_hi = upper(hi)
    old = "_"
    new = " "
    return replace(big_hi,old, new)

dash = "-"
    
print dash*10 + prancercise("say_hi_to", "-") + dash*10