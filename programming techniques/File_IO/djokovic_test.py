f = open("djokovic_file.txt","rt")
data = f.read()
f.close()
print(data)

for line in data:
    print(line)

f = open("output.txt","wt")
f.write(data)
f.close()

f = open("output.txt","wt")
print(data, file=f)
f.close()
