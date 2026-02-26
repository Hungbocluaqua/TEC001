import math
#Calculate the money value of two pizza
dia1 = float(input("Enter the diameter of pizza 1 (m): "))
dia2 = float(input("Enter the diameter of pizza 2 (m): "))
prc1 = float(input("Enter the price of pizza 1 (USD): "))
prc2 = float(input("Enter the price of pizza 2 (USD): "))
piz1va = prc1/(math.pi*(dia1/2)**2)
piz2va = prc2/(math.pi*(dia2/2)**2)
if (piz1va) > (piz2va):
    print("pizza 1 provides better value than the pizza 2")
else:
    print("pizza 2 provides better value than the pizza 1")
