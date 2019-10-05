## Conversion of upper and lower case
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
    print(char, end='')
