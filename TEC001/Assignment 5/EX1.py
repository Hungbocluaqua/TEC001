import re
def course_check(code):
    pattern = r'^[A-Z]{2,3}\d{3}$'
    return bool(re.match(pattern, code))
code = input("Enter course code: ")
print(course_check(code))
