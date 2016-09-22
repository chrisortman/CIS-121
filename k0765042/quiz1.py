############################
#
# Please complete this quiz
#

# declare an int variable named total with the value of 0

# declare an array named numbers with all numbers 0 - 20

# write a for loop that processes each number
# if the number is even add it to total
# if the number is odd and a multiple of 5 display the number preceded by the word Checkpoint: on a single line

#display the value of total followed by a dash and the word total

total = 0
onerange = range(1,21)


for x in onerange:
    if x %2 == 0:
        total = total + x
    elif x %5 == 0:
        print "Checkpoint %d" %x
print total, "- Total"