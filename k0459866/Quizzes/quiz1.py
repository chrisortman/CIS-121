############################
#
# Please complete this quiz
#

# declare an int variable named total with the value of 0
total = 0
# declare an array (list) named numbers with all numbers 0 - 20
numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# write a for loop that processes each number
for nums in numbers:
    print nums
# if the number is even add it to total
    if nums % 2 == 0:
        cumulative = []
        total = total + nums
        cumulative.append(total)
# if the number is odd and a multiple of 5 display the number preceded by the word Checkpoint: on a single line
    if nums % 2 != 0 and nums % 5 == 0:
        print "Checkpoint"
#display the value of total followed by a dash and the word total
print total,"- total"
print ""
################################################################################
#ANSWER

# declare an int variable named total with the value of 0
total = 0
# declare an array (list) named numbers with all numbers 0 - 20
numbers = range(0,20)

# write a for loop that processes each number
def even(number):
    return number % 2 == 0
    
def divisible_by_five(number):
    return number % 5 == 0
# if the number is even add it to total
for i in numbers:
    if even(i):
        total = total + i
    elif divisible_by_five(i):
        print "Checkpoint %d" % i
# if the number is odd and a multiple of 5 display the number preceded by the word Checkpoint: on a single line
    if nums % 2 != 0 and nums % 5 == 0:
        print "Checkpoint"
#display the value of total followed by a dash and the word total
print total,"- total"