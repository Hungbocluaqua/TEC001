
def find_keyword(filename, keyword):
    file = open(filename, "r")
    line_numbers = []
    line_number = 1

    for line in file:
        if keyword in line:
            line_numbers.append(line_number)

        line_number = line_number + 1

    file.close()
    return line_numbers

