# from sys import argv

# script, text, surround = argv

# def prancercise(text, surround):
#     new = text.replace("_", " ")
#     space = text.replace(" ", "")
#     comma = text.replace(",", "")
#      d = surround * 10
#      return d,new.upper(),d
#     return prancercise
# #returns ('----------', 'SAY HI TO', '----------') instead of (----------SAY HI TO----------)

# prancercise(text, surround)
# transformed = prancercise("say_hi_to", "-")

# print transformed

# if (transformed == "('----------', 'SAY HI TO', '----------')"):
#     print "Somethings still not right."
# elif (transformed == "('----------SAY HI TO--------')"):
#     print "That's right!"
# else:
#     print "That's wrong, you want '----------SAY HI TO----------'"

from sys import argv

script, text, surround = argv

def prancercise(text, surround):
    new = text.replace("_", " ")
    return new.upper()
    
prancercise(text, surround)
transformed = prancercise("say_hi_to", "-")

print "%s%s%s" % ((("-")*10), transformed, (("-")*10))
