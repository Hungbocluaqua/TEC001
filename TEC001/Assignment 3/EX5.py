String = input("Enter a string: ")
if len(String)%2 == 0:
    print(String[len(String)//2-1],String[len(String)//2] )
else:
    print(String[len(String)//2])
