#Fish length checker
Length = int(input("Enter the length of the zander: "))
if Length < 42:
    print("Fish is not big enough pls throw it back into the lake")
    print("Length of fish is ", 42-Length,"cm short")
else:
    print("Fish is big enough you can keep it \n")
