from sys import argv
from os.path import exists

script, one, two = argv

print "Copying from %s to %s" % (one, two)

inside = open(one)
data = inside.read()

print "The input file is %d bytes long" % len(data)

print "Does the output file exist? %r" % exists(two)
print "Ready, hit RETURN to continue, CTR-C to abort."
raw_input()

outside = open(two, "w")
outside.write(data)

print "Alrigth, all done."

outside.close()
inside.close()