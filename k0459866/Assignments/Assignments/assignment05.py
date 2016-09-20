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

print "Is all of this information correct?"
question = str(raw_input(">"))

if (question == "yes") and not None:
    print "Just making sure everythings correct."
elif (question == "no") and not None:
    print "Uh oh, something went wrong, please restart the program!"
else:
    "Something went wrong"
