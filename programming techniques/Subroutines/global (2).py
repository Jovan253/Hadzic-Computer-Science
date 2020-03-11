def f():
    global s
    s = "I Love London!"
    print(s)

s = "I Love Paris!"
f()
print(s)
