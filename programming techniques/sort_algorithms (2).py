import time
import random


num = 100
a = []

for i in range(0, num - 1):
    rnd = random.randint(0,100)
    f = open("numbers.txt", "wt")
    f.write(str(rnd))
    f.close()

for i in range(0, num - 1):
    f = open("numbers.txt", "rt")
    a.append(int(f.read()))
f.close()

n = len(a)
temp = 0
flag = False

b_start = time.clock()
while n!= 1 or flag == True:
    flag = False	
    for count in range(1, n-1):
        if a[count] > a[(count + 1)]:
            temp = a[count]
            a[count] = a[count + 1]
            a[count + 1] = temp
            flag = True
        #endif        
        count += 1
    #next
    n = n-1
#endwhile    
b_end = time.clock()
print("bubble sort time elapsed = ", b_end - b_start)


i_start = time.clock()
for i in range (1, n - 1):
    currentvalue = a[i]
    pointer = i - 1
    while pointer >= 0 and a[pointer] > currentvalue:
        a[pointer + 1] = a[pointer]
        pointer = pointer - 1
    #endwhile
    a[pointer + 1] = currentvalue
    i = i + 1
    print("insertion complete")
i_end = time.clock()
print("insertion sort time elapsed = ", i_end - i_start)
