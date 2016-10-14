import random

def passcode():
    right = 0
    x = 0
    a = random.randint(1,10)
    b = random.randint(1,10)
    c = random.randint(1,10)
    
    d = a + b
    e = a + c
    f = b + c
    
    if d >= 10:
        d = d - 10
    
    if e >= 10:
        e = e - 10
    
    if f >= 10:
        f = f - 10
    
    numbers = [a,b,c,d,e,f]
    
    num_one = random.choice(numbers)
    
    guesses_one = 0
    
    
    print "[-]"
    print "You try and turn the dials and only the first one turns"
    while guesses_one < 10:
        first_digit = raw_input(">")
        print num_one
        if first_digit == str(num_one):
            print "You got the first number right"
            guesses_one = 10
            right = 1
        elif first_digit >= str(num_one):
            print "You have a rising suspision that you are to high"
        elif first_digit <= str(num_one):
            print " You have a sinking feeling that you are to low"
        guesses_one = guesses_one + 1
    return right