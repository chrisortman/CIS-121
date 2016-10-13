############################
#
# Please complete this quiz
#

# declare an int variable named total with the value of 0

# declare an array named numbers with all numbers 0 - 20

""" > Write a for-loop that processes each number
    > If the number is even, add it to 'total'
    > If the number is odd, and a multiple of five, display the number, preceded
      by the word "Checkpoint:", on a single line
    > Display the value of 'total', followed by a dash, and the word "total" """

total = int(0)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20]
for number in numbers:
    if number % 2 == 0:
        total = total + number
    elif number % 5 == 0 and not number % 2 == 0:
        print "Checkpoint:", number
        
print total, "-", "total"