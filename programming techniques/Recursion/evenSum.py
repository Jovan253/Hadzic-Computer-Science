def evenSum(n):
        if n % 2 == 0 and n > 0:
            return n + evenSum(n + 2)
        else:
            return 0
        #endif
    #next
#endfunction
number = int(input("Enter a number"))
result = evenSum(number)
