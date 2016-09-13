from sys import argv

script, text, surround = argv
def meow(text, surround):
    new = text.replace("_"," ")
    x = surround*10
    print x, new.upper(),x
meow(text,surround)
