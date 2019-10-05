
def add_one(a_number):
    a_number += 1
    return a_number
#endfunction

def add_s(name): 
    name = name + "s"
    return name
#endfunction

def append_s(name):
    name.append("s")
    print(name)
#endprocedure    

num = 3
name = "Dave"
name_list = ["D","a","v","e"]

print(add_one(num)) #will print 4
print(num)  # will print 3

num = add_one(num) # now num will be 4
print(num) # will print 4

print(add_s(name))
print(name)

append_s(name_list)
print(name_list)


