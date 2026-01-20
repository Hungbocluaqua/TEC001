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
