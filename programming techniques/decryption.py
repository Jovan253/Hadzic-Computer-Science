## Decryption
import enchant
d = enchant.Dict("en_US")

key = 'abcdefghijklmnopqrstuvwxyz'
text = input("enter text to be decrypted in caps: ")

for n in range(26):
    result = ""
    for l in text:
        shift = ord(l) - n
        if shift < 65:
            shift = ord(l) + (26 - n)
        #print(shift)
        x = chr(shift)
        result += x
    #print(n, result)
    if d.check(result) == True:
        print(n, "is the key to decrypt to get the message", result)


        
    
