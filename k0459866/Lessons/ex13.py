def foo(x):
    print "HOMER"
    return x % 2 == 1
    
def bar():
    print "MARGE"
    return True
    
x = input("Enter a number\n")
#x = -6

if x > 5 or foo(x):
    print "BART" #bart
    if x % 2 == 0:
        print "LISA"
elif not (x < 0 and bar()):
    print "MAGGIE"
else:
    print "SNOWBALL"