import random
LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\] ^_`abcdefghijklmnopqrstuvwxyz{|}~'
translated = ''
encrypt_mode = 1
decrypt_mode = 0

def encrypt():
    global translated
    mode = encrypt_mode
    key = random.randint(1,13)
    print "The key is: %s" %key
    msg = raw_input("What is the message: ")
    for symbol in msg:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode == 1:
                num = num + key
            else:
                print "ERROR: MODE NOT FOUND"
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)
            else:
                print "ERROR: NUM NOT NUMBER"
        else:
            translated = translated + symbol
    print translated
    
    
def decrypt():
    print(" ")

def set_mode():
    print "Would you like to encrypt or decrypt"
    mode = raw_input(">")
    if mode == 'e':
        encrypt()
    elif mode == 'd':
        decrypt()
    else:
        print "Enter d or e to decrypt or encrypt"
        
set_mode()
    