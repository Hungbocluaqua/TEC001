
def caesar_cipher(filename, shift, direction):
    if direction == "left":
        shift = -shift

    input_file = open(filename, "r")
    output_file = open("ciphertext.txt", "w")

    for line in input_file:
        new_line = ""

        for c in line:

            if c.isupper():
                x = ord(c) - 65
                y = (x + shift) % 26
                new_char = chr(y + 65)
                new_line = new_line + new_char

            elif c.islower():
                x = ord(c) - 97
                y = (x + shift) % 26
                new_char = chr(y + 97)
                new_line = new_line + new_char

            else:
                new_line = new_line + c

        output_file.write(new_line)

    input_file.close()
    output_file.close()