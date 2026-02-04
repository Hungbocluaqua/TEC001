phrase = input("Enter a phrase: ").split(" ")
acronym = "Acronym: "
for i in range(len(phrase)):
    acronym = acronym + phrase[i][0].upper()
print(acronym)

