from sys import argv

script, string, repeat = argv

def prancercise(string, repeat):
    
    add_space = string.replace("_", " ")
    dash = repeat * 10
    return ("%s%s%s") % (dash, add_space.upper(), dash)