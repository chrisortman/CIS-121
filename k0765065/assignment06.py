from sys import argv

script, string, repeat = argv

def prancercise(string, repeat):
    x = string.replace("_", " ")
    y = repeat * 10
    print ("%s%s%s") % (y, x.upper(), y)

prancercise(string, repeat)