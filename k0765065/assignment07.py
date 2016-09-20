from sys import argv

if len(argv) == 3:
    from prancercise import prancercise
    script, string, repeat = argv
    output = prancercise(string, repeat)
    print output
    
else:
    print("Please input a statement and a surrounding character.")