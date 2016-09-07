from sys import argv

script, filename = argv

txt = open(filename)
print "Here's yout file %s:" % filename
print txt.read()

print "Typle the filename again: "
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
txt.close()
txt_again.close()