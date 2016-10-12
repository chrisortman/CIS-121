# I M P O R T S
import time
import random
import datetime
print "Which import do you want?"
#TIME
var1 = 10
while var1 > 1:
    print var1
    var1 = var1 - 1
    time.sleep(1)
print ""
################################################################################
#RANDOM
var2 = [0,1,2,3,4,5,6,7,8,9,10]
var3 = 5
while var3 > 1:
    print random.choice(var2)
    var3 = var3 - 1
print ""
################################################################################
#TIME + RANDOM
foo = [0,1,2,3,4,5,6,7,8,9,10]
x = 0
y = True

while y is True:
    print x
    if x < 10:
        x = x + 1
    elif x == 10:
        x = x - random.choice(foo)
    time.sleep(0.25)
print ""
################################################################################
#DATES & TIME (different time)
print datetime