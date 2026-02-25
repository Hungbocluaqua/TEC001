def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total



my_list=[4, 7, 1, 9, 3]
result=sum_of_list(my_list)

print("List:", my_list)
print("Sum:", result)