#Quy đổi từ talents, pounds, lots sang kilogram
try:
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
except:
    print("please enter a valid number")