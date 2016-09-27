from sys import argv
from prancercise import prancercise

if len(argv) == 3:
    script, string, repeat = argv
    output = prancercise(string, repeat)
    print output
    
else:
    print("Please input a statement and a surrounding character.")
    new_string = raw_input()
    new_repeat = raw_input()
    output = prancercise(new_string, new_repeat)
    print output