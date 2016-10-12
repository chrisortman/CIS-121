# M A T H
import math
import random
#SCIENTIFIC NOTATION
part1 = 7.04
part2 = (10^7)
big_num = part1 * part2
big_num2 = 7.04*10e6
print "part1 is equal to %s" % part1
print "part2 is equal to %s" % part2
print "big_num is equal to %s" % big_num
print "but big_num2 is equal to %s" % big_num2
print ""
################################################################################
#FIGURING OUT SQUARE ROOTS
print "What will 'x' be?"
x = input(">")
sqrt = x**(0.5)
print "The square root of %s is %s" % (x,sqrt)
print ""
################################################################################
#CUBE ROOTS
print "What will 'y' be?"
y = int(raw_input(">"))
for ans in range(0, abs(y) + 1):
    if ans ** 3 == abs(y):
        break
if ans ** 3 != abs(y):
    print y, 'is not a perfect cube root!'
else:
    if y < 0:
        ans = -ans
    print 'Cube root of ' + str(y) + ' is ' + str(ans)
print ""
################################################################################
#RANDOM
print "How many random numbers do you want to print?"
var1 = input(">")
foo = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
var2 = (random.choice(foo))
while var1 > 0:
    print var2
    var2 = (random.choice(foo))
    var1 = var1 - 1
print ""
################################################################################