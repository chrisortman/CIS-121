from prancercise import prancercise

# check argv len(argv) will give back number of arguments ... so len(argv) 

# if any argv use them for prancercise

# otherwise ask user to input string and character

string = raw_input ("Enter a string ")
character = raw_input("Enter a character ")

def prancercise(string, character):
    big_string = upper(string)
    characters = character*10
    
print prancercise(big_string, characters)