numbers = []

while True:
    value = input("Nhập một số (nhấn Enter để kết thúc): ")
    if value == "":
        break
    numbers.append(float(value))

numbers.sort(reverse=True)

print("5 số lớn nhất:")
for num in numbers[:5]:
    print(num)
