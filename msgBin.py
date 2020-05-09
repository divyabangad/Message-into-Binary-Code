
msg = input("Enter the Message to be converted into Binary:\n")
binCode = ""

for letter in msg:
    if(letter == " "):
        binCode = binCode + " "
    else:
        y = bin(ord(letter))
        #ord function returns ascii value of a character
        #bin converts an integer to its binary format with a prefix '0b'
        x = y[2:]
        binCode = binCode + x + " "

print (binCode)