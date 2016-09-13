from sys import argv

script, text, surround = argv

def prancercise(text, surround):
    new = text.replace("_", " ")
    d = surround * 10
    return d, new.upper(), d

prancercise(text, surround)
transformed = prancercise("say_hi_to", "-")

print transformed