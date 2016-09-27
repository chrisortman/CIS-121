# declare an int variable named total with the value of 0
total = 0

# declare an array named numbers with all numbers 0 - 20
numbers =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# write a for loop that processes each number
def even(num):
    return num % 2 == 0

def odd(num):
    return num % 5 == 0

for num in numbers:
    
    if even(num):
        total = num + total
    elif odd(num):
        print "%d Checkpoint" % num




print  "%s - total" % total

    # if the number is even add it to total
# if the number is odd and a multiple of 5 display the number preceded by the word Checkpoint: on a single line

#display the value of total followed by a dash and the word total




