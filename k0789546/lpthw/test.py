
word = "tree cat"
user_word = []
position_list = []
display = []
for z in word:
    display.append("_")
g = 0
t = 0
b = 0

user = " "
while True:
    user = raw_input("Letter: ")

    for x in word:
        position = word.find(user, t)
        t += 1
        position_list.append(position)
    t = 0
    print position_list
    
    
    for i in position_list:
        if i not in user_word and i >= 0:
            user_word.append(i)
                
            
    print user_word
    for y in position_list:
        if y >= 0:
            display[y] = user
            
    gif = "  ".join(display)
    print gif
    finish = "".join(display)
    
    if finish == word:
        exit()
    
    position_list = []
    g += 1       






