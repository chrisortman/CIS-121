############################
#
# Please complete this quiz
#

# declare an int variable named total with the value of 0
total = 0

# declare an array named numbers with all numbers 0 - 20
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# write a for loop that processes each number


# if the number is even add it to total
def even(x):
    return x % 2 == 0
    
def odd(x):
    return x % 5 == 0   
    
# if the number is odd and a multiple of 5 display the number preceded by the word Checkpoint: on a single line
for x in array:
    if even(x):
        total = x + total
    elif odd(x):
        print "Checkpoint: %s" % x 
         

print "%d-total" % total


#display the value of total followed by a dash and the word total


  


   
