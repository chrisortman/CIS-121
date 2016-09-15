# from sys import argv
# print argv
# script, user_name = argv
# prompt = '> '

# print "Welcome %s! You are currently running the %s script!" % (user_name, script)

# print "This program will ask you about your favorite food items."
# print "First off, what is your favorite thing to eat?"
# food = raw_input(prompt)

# print "That's pretty good. Now, what's your favorite drink?"
# drink = raw_input(prompt)

# print "Almost done, now I'd like to know your favorite restaurant."
# restaurant = raw_input(prompt)

# print "All finished!"
# print "So you like to eat %s and drink %s?" % (food, drink)
# print "And your favorite place to eat at is %s?" % (restaurant)

answer1 = ("yes")
answer2 = ("Yes")
answer3 = ("y")
answer4 = ("Y")

question = str(raw_input("Is all of this information correct?\n"))

if (question == answer1) or (question == answer2) or (question == answer3) or (question == answer4) is not None:
#Clarifying that if the question is something, it'll run(?)
    print "Great, just making sure everything was correct!"
elif (question != answer1) or (question == answer2) or (question ==answer3) or (question == answer4) is not None:
    print "Uh oh, please retry the program, something went wrong!"
else:
    print "Something went wrong!"
    
