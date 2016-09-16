from sys import argv

script, string, repeat = argv

def prancercise(string, repeat):
    add_space = string.replace("_", " ")
    dash = repeat * 10
    print ("%s%s%s") % (dash, add_space.upper(), dash)

prancercise(string, repeat)