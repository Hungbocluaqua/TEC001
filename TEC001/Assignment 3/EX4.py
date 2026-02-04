username = "python"
password = "rules"
i = 0
acctrue = False
while i <= 5:
    if username == input("Enter username: ") and password == input("Enter passwords: "):
        acctrue = True
        break
    else:
        i += 1
if acctrue == True:
    print("Welcome")
else:
    print("Access denied")