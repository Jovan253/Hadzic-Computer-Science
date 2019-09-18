num = 3
name = "Dave"
name_list = ["D","a","v","e"]

def add_one(num):
    num += 1
    return num
#endfunction

def add_s(name): 
    name = name + "s"
    return name
#endfunction

def append_s(name):
    name.append("s")
    print(name)
#endprocedure    

print(add_one(num))
print(num)

print(add_s(name))
print(name)

append_s(name_list)
print(name_list)


