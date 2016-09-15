from sys import argv

def prancercise(text,surround_char):
    surround = surround_char * 10
    return surround + text.upper().replace("_"," ") + surround

_, text, surround_char = argv

print prancercise(text,surround_char)
