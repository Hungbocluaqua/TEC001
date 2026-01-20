import math
#Fish length checker
Length = int(input("Enter the length of the zander: "))
if Length < 42:
    print("Fish is not big enough pls throw it back into the lake")
    print("Length of fish is ", 42-Length,"cm short")
else:
    print("Fish is big enough you can keep it \n")

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

#Hemoglobin value checker
gender = input("Enter your biological sex (M/F): ")
hemo = float(input("Enter your hemoglobin value (g/l): "))
if gender == "M":
    if hemo >= 117 and hemo <= 155:
        print("Your hemoglobin value is normal")
    elif hemo < 117:
        print("Your hemoglobin value is low")
    elif hemo > 155:
        print("Your hemoglobin value is high")
if gender == "F":
    if hemo >= 134 and hemo <= 155:
        print("Your hemoglobin value is normal")
    elif hemo < 134:
        print("Your hemoglobin value is low")
    elif hemo > 155:
        print("Your hemoglobin value is high")

#Leap year checker
year = int(input("Enter a year: "))
if year%4 == 0 or (year%100 == 0 and year%400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

#Calculate the money value of two pizza
dia1 = float(input("Enter the diameter of pizza 1: "))
dia2 = float(input("Enter the diameter of pizza 2: "))
prc1 = float(input("Enter the price of pizza 1: "))
prc2 = float(input("Enter the price of pizza 2: "))
piz1va = prc1/(math.pi*(dia1/2)**2)
piz2va = prc2/(math.pi*(dia2/2)**2)
if (piz1va) > (piz2va):
    print("pizza 1 provides better value than the pizza 2")
else:
    print("pizza 2 provides better value than the pizza 1")