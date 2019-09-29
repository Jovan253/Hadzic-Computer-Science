def fact(num):
    if num == 0:
        factorial = 1
    else:
         factorial = num * fact(num - 1)        
     #endif
    return factorial
#endfunction

number = int(input("Enter a number for factorial "))
result = fact(number)
print("The factorial of ", number, "is ", result)








#With Iteration

n = int(input("Enter the number of terms "))
fact = 1
  
for i in range(1,n+1): 
    fact = fact * i 
#next      
print ("The factorial of ", n, "is", fact) 
