number = input("What's your favorite number?\n")

if number < 100:
    print "That's a reasonable number."
else:
    if 100 > number < 1000:
        print "Large numbers are also cool."
    else:
        if number >= 1000:
            print "That's a bit much, isn't it?"
            
