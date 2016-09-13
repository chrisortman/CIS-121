#these two varibles are easier to understand than numbers

days_in_a_year = 365




#This line of code will ask a question and print a procuct
print "What is the product of 36 times 6?", 36 * 6

#This line of code prints a quotient of the numbers below
print "What is the quotient of 89/10", 89.0/10.0

#This line prints the product of the complex equation below 
print "What is the sum of 89/10 and 36 times six", 89.0/10.0 * (36 * 6)


#This line of code tells you how long you've been living in seconds through defined varibles
def seconds_alive ():
    my_age = input("Enter your age:")
    print "How many seconds have you been alive", my_age * days_in_a_year * 24 * 60 * 60  
    
seconds_alive()