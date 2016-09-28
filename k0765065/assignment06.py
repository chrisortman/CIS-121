from sys import argv
from prancercise import prancercise

script, string, repeat = argv

#def prancercise(string, repeat):
    #add_space = string.replace("_", " ")
    #dash = repeat * 10
    #print ("%s%s%s") % (dash, add_space.upper(), dash)

output = prancercise(string, repeat)
print output