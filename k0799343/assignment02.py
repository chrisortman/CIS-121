from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)

math = 10*525343424+646436453534+4
print "MATH %d" % math

print "MATH2", 24/2<15

print "###" 

current_number=input("Enter current number:")


sombra= (100.0-current_number)/0.0038*3
print "%d" % sombra,
print "in minutes"

print sombra/60,
print "in hours"

print sombra/60/24,
print "in days"

print "until 100%"