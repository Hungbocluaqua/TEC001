numbers = []

while True:
    value = input("Enter a number (press Enter to quit): ")
    if value == "":
        break
    numbers.append(float(value))

numbers.sort(reverse=True)

print("Five greatest numbers:")
for number in numbers[:5]:
    print(number)