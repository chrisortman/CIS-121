print "I will find the average of five numbers."
import time
time.sleep(1.000)

var0 = input("> Enter a number: ")
var1 = input("> Enter another number: ")
var2 = input("> Enter another number: ")
if var2 == 0:
    
var3 = input("> Enter another number: ")
var4 = input("> Enter one more number: ")
import time
time.sleep(2.000)

print var0,"+",var1,"+",var2,"+",var3,"+",var4,"=", var0 + var1 + var2 + var3 + var4
total = var0 + var1 + var2 + var3 + var4
while total < 5.000:
    print "TOTAL IS LESS THAN 5!"
    total += 0.250
import time
time.sleep(0.500)

print total,"/ 5 = ", total / 5.000
average = total / 5.000
import time
time.sleep(0.500)

print "The average of your numbers is %s." % average