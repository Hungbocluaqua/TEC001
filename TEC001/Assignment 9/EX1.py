
def count_lines(filename):
    file = open(filename, "r")
    count = 0

    for line in file:
        if line.strip() != "":
            count = count + 1

    file.close()
    return count

