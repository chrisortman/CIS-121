from prancercise import prancercise
from sys import argv


if argv == " ":
    text = raw_input("Insert Text: ")
    surround = raw_input("Insert Surround: ")
else:
    script, text, surround = argv
    prancercise(text, surround)