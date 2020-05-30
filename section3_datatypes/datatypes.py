import datetime
import math

mynow = datetime.datetime.now()
print(mynow)

x = 10
y = "asdf"
z = 10.1
print(type(x), type(y), type(z))

student_grades = [1.1, 2.4, 3.5, 4.1]
list(range(1, 10))

dir(student_grades)

y.upper()
y.title()

avg = sum(student_grades) / len(student_grades)
print(avg)

student_grades.count(1.1)


student_grades_dict = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
print(student_grades_dict["Marry"])

student_grades_dict.values()
student_grades_dict.keys()

monday_temperature = (1, 4, 5)
