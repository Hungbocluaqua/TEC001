#Leap year checker
year = int(input("Enter a year: "))
if year%4 == 0 or (year%100 == 0 and year%400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
