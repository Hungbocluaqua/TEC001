import math
#Nhập tên và in lời chào
print("HELLOOOOOOOO ", f"{input("Enter your name: ")} \n")

#Tính chu vi hình tròn
circumference = 2 * math.pi * float(input("Enter the radius of the circle: "))
print("The circumference of the circle: ", f"{circumference: .2f} \n" )

#Tính chu vi và diện tích hình chữ nhật
Rong = float(input("Width: "))
Dai = float(input("Length: "))
print("Perimeter of the rectangle: ", f"{2 * (Rong + Dai): .2f}")
print("Area of the rectangle: ", f"{Rong * Dai: .2f} \n")

#Tính tổng, tích, trung bình cộng của 3 số nguyên tố
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))
print("Sum: ", x+y+z)
print("Product: ", x*y*z)
print("Average: ", f"{(x+y+z)/3: .2f} \n")

#Quy đổi từ talents, pounds, lots sang kilogram
talents = input("Enter numbers of talents: ")
pounds = input("Enter numbers of pounds: ")
lots = input("Enter numbers of lots: ")
if talents:
    print("Kilograms from talents: ", f"{float(talents)*8.512: .2f}")
else:
    print("You didn't enter any talents.")
if pounds:
    print("Kilograms from pounds: ", f"{float(pounds)*0.4256: .2f}")
else:
    print("You didn't enter any pounds.")
if lots:
    print("Kilograms from lots : ", f"{float(lots)*0.0133: .2f}")
else:
    print("You didn't enter any lots.")
