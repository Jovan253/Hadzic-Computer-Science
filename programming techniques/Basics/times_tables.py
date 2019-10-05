rows = int(input("How many rows? "))

answer == "n"
while answer == "n":

### SRC - Too much indentation here (everything can go back 4 spaces
        table = -1
        while table < 1 or table > 20:
 ### SRC - Too much indentation here (everything can go back 4 spaces
               
                table = input("What Table [1-20]")
                if table.isdigit():
                        table = int(table)
                else:
                        table = -1
                        print("Not an integer")

        answer = input("Did you mean Y/N: " , str(table).lower())

   



  
