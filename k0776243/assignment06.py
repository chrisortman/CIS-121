from string import upper
from string import replace


def prancercise(hi, dash):
    big_hi = upper(hi)
    old = "_"
    new = " "
    return replace(big_hi,old, new)

dashes = "-" * 10

    
print dashes, prancercise("say_hi_to", "-"), dashes