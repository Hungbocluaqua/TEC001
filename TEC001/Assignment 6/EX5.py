def remove_odds(numbers):
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    result = remove_odds(numbers)

    print("Danh sách ban đầu:", numbers)
    print("Danh sách sau khi bỏ số lẻ:", result)


main()