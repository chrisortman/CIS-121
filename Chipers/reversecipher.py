def reverse_cypher():
    print "What is the message that you would like to cypher."
    msg = raw_input(">")
    translated = ''
        
    i = len(msg) - 1
    while i >= 0:
        translated = translated + msg[i]
        i = i - 1
            
    print translated

while True:
    reverse_cypher()