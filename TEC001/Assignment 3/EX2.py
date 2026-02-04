
#inch to cm
num = 1
while num > 0:
    num = float(input("Enter a number of inches to convert to cm: "))
    if num < 0:
        break
    print(num*2.54)
    