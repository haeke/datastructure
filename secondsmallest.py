"""
    second lowest element in an array
    
"""

def secondlow(students):
    grades = []
    for student in students:
        grades.append(student[1])
    sortgrades = sorted(grades)
    lowest_grade = sortgrades[0]
    for grade in sortgrades:
        if grade != lowest_grade:
            lowest_grade = grade
            break
    seclow_stu = []
    for student in students:
        if student[1] == lowest_grade:
            seclow_stu.append(student[0])

    for name in sorted(seclow_stu):
        print name

students = []
for items in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())

    new_stud = [name, score]
    students.append(new_stud)
secondlow(students)
