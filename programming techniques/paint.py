height = int(input("Enter height in cm: "))
width = int(input("Enter width in cm: "))
depth = int(input("Enter depth in cm: "))

wall = int(height * width * 2 + height * depth + width * depth)

paint = int(input("Enter the amount of paint in militers: "))

paint_needed = int(wall / paint)

print("We neeed " + str(paint_needed) + " mililitres of paint")

