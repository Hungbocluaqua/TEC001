#Cabin class description
Class = input("Enter the class of the cabin (LUX, A, B, C): ")
if Class == "LUX":
    print("upper-deck cabin with a balcony")
elif Class == "A":
    print("above the car deck, equipped with a window")
elif Class == "B":
    print("windowless cabin above the car deck")
elif Class == "C":
    print("windowless cabin below the car deck")
else:
    print("Invalid cabin class \n")

