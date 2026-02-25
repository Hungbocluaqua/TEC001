number = int(input("Enter an integer: "))

if number <= 1:
    print("Not a prime number")
else:
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")