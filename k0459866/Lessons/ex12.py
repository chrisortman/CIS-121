#import factorial
#import square

x = int(raw_input("What is 'x'?\n"))
y = int(raw_input("What is y?\n"))
# question0 = str(raw_input("Define a y value? (y/n)\n"))
# if (question0 == "y","Y","yes","Yes"):
#     y = int(raw_input("What will 'y' be?\n"))
# elif (y == "n","N","no","No"):
#     question2 = str(raw_input("Is y = 10 ok?\n"))
#     if (question2 == "y","Y","yes","Yes"):
#         y = 10
#     elif (question2 == "n","N","no","No"):
#         y = int(raw_input("What will 'y' be?\n"))
#     else:
#         print "Please insert and interger"
# else:
#     print "Please insert an interger."

print "Using that information, we can do some mathematical equations."

if x > y: #is not None:
    print "x, %d, is greater than y, %d." % (x, y)
elif x == y: #is not None:
    print "x, %d, is equal to y, %d." % (x, y)
elif x < y: #is not None:
    print "x, %d, is less than y, %d." % (x, y)
elif x is not int:
    print "x should be a interger, you put it as %d" % (x)
elif x is None:
    print "Please rerun the code."
else:
    print "Something went wrong!"
    
add = (x + y)
sub = (x - y)
mult = (x * y)
div = (x / y)   
rem = (x % y)
xeven = (x % 2 == 0)
xodd = (x % 2 != 0)
yeven = (y % 2 == 0)
yodd = (y % 2 != 0)
# xfact = (factorial(x))
# yfact = (factorial(y))

print "If you add x and y, you'll get %s." % add
print "If you subtract x and y, you'll get %s." % sub
print "If you multiply x and y, you'll get %s." % mult
print "If you divide x and y, you'll get %s, with a remainder of %s." % (div, rem)
if (x % 2 == 0):
    print "x is even."
if (x % 2 != 0):
    print "x is odd."
if (y % 2 == 0):
    print "y is even."
if (y % 2 != 0):
    print "y is odd."

print "If you square x, you get %s, and y squared is %s." % ((x^2),(y^2))
print "If you cube x, you get %s, and y cubed is %s." % ((x^3), (y^3))
#print "If you take x factorial, you get %s, and y factorial is %s." % ((xfact), (yfact))
#print "The square root of x is %s, and the square root of y is %s." % (square(x), square(y))
print ""

# from sys import argv
# import random

# value = (1,2,3,4,5,6)

# roll, string = argv

# def choice(roll):
    
#     random.choice(dice)
#     return choice

# choice(roll)
# dice = choice(value)