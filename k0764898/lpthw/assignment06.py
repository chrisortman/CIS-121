from sys import argv
script, text, surround  = argv
transformed = prancercise("say_hi_to","-")
print transformed
def prancercise(text,surround)

replace = text.replace("_"," ")
x = surround*10
print x,replace.upper(),x
prancercise(text,surround)