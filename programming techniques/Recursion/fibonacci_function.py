import time

def fib(n):
    #print("n=", n)
    if n <= 1:
        return n
    else:
        #print("recursing...")                    ## used prints to check for errors
        return fib(n-1) + fib(n-2)
    #endif                           
#endfunction

def fib2(n):
    fibNumbers = [0,1]
    for i in range(2,n):
        #print("i=", i)
        f1 = fibNumbers[i-1]
        #print("f1=", f1)
        f2 = fibNumbers[i-2]
        #print("f2=", f2)
        fibNumbers.append(f1 + f2)
        #print("fib[",i,"]=",fibNumbers)
    #next i
    return fibNumbers[n-1]
#endfunction

def measure_time(n, r_or_i) :   ## n is the entry, r_or_i is the variable relating to what routine we want to use; "r" or "i"
    start = time.clock()
    if r_or_i == "r":       ##calculating recursive
        result = fib(n)
    else:                   ##calculating iterative
        result = fib2(n)
    #endif

    print(r_or_i, " result = ",result)
    end = time.clock()
    if n == 20 or n == 10:                       ## time is shown if our entry is 10 or 20 
        print(r_or_i, " time elapsed = ", end - start)
    #endif    
#endfunction

val = "False"
entry = int(input("Enter a number between 3 and 30 "))
while val == "False":                                         ## Validation
    if entry > 2 or entry < 31:
        val == "True"
        break
    else:
        print("Error, try again")
        entry = int(input("Enter a number between 3 and 30 "))
    #endif
#endwhile        


measure_time(entry -1, "r")
measure_time(entry, "i")

