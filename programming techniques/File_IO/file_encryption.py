## Conversion of upper and lower case
### SRC - Please continue with the coding conventions!
f = open("djokovic_file.txt","rt")
while True:
    char = f.read(1)
    if not char:
        break

    if char.isupper():
      char = char.lower()
    else:
      char = char.upper()
    print(char, end='')
    
print()

## Encrypting e.g. Caeser cypher
f = open("djokovic_file.txt","rt")
step = int(input("What step do you want to encrypt by. E.g. 3 (Caesar cypher) "))
while True:
    char = f.read(1)
    if not char:
        break

    shift = ord(char) + step
    char = chr(shift)
    print(char, end='') ### SRC - Write the output to a file

### SRC - This is not a full Caeser Cipher as it would be better if the
### output was all alpha characters
    

    
