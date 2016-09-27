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
count = 0
rule = 0

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

checkpoint = []
checkpoint.append("Checkpoint")

for i in numbers: 
    value = i
    if i % 2 == 0:
        total = total + value
    elif value % 5 == 0:
            count = count + 1
            checkpoint.append(value)
    else:
        pass
while rule < count:
    rule = rule + 1
    print "Checkpoint %d" %checkpoint[rule]
   # print "WORK"    

print "%d - total" % total