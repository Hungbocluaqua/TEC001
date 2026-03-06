import re
def sum_numbers(text):
    numbers = re.findall(r'\d+', text)
    return sum(int(n) for n in numbers)