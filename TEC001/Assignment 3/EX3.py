i = True
smllnum = 0
bgnum = 0
while i:
    n = (input("Enter a number: "))
    if n == "":
        break
    n = int(n)
    if n > bgnum:
        bgnum = n
    if n < smllnum:
        smllnum = n
print(f"Smallest number: {smllnum}")
print(f"Biggest number: {bgnum}")