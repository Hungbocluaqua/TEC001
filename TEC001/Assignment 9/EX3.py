def average_score(filename):
    file = open(filename, "r")

    total = 0
    count = 0

    for line in file:
        line = line.strip()

        if line != "":
            parts = line.split(",")
            score = float(parts[1])

            total = total + score
            count = count + 1

    file.close()

    if count == 0:
        return 0

    return total / count
