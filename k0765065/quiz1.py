############################
#
# Please complete this quiz
#

# declare an int variable named total with the value of 0
z = 0

# declare an array named numbers with all numbers 0 - 20
number_list = []
x = 0

while x < 21:
    number_list.append(x)
    x = x + 1

# write a for loop that processes each number
# if the number is even add it to total
# if the number is odd and a multiple of 5 display the number preceded by the word Checkpoint: on a single line
total = 0
checkpoint_list = []
for number in number_list:
    if (number % 2) == 0:
        total = number + total
    #if (number % 2) != 0 AND (number % 5) == 0
    elif(number % 5) == 0:
        checkpoint_list.append(number)
    else:
        continue

#display the value of total followed by a dash and the word total
output = ""
for nums in checkpoint_list:
    output += "%r Checkpoint " % nums
    nums += 1

print output
print "%r total" % total

