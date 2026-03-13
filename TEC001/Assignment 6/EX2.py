seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Nhập số tháng (1-12): "))

if month == 12 or month == 1 or month == 2:
    season = seasons[0]
elif 3 <= month <= 5:
    season = seasons[1]
elif 6 <= month <= 8:
    season = seasons[2]
else:
    season = seasons[3]

print("Mùa:", season)