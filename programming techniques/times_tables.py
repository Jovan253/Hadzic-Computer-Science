rows = int(input("How many rows? "))

answer == "n"
while answer == "n":
        table = -1
        while table < 1 or table > 20:
                table = input("What Table [1-20]")
                if table.isdigit():
                        table = int(table)
                else:
                        table = -1
                        print("Not an integer")

   answer = input("Did you mean Y/N: " , str(table)).lower())



  
