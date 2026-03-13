names = set()

while True:
    name = input("Nhập tên (Enter để kết thúc): ")
    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nDanh sách các tên:")
for name in names:
    print(name)