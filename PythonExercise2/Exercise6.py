student_1 = [40,35,70,90,56]
student_2 = [57,35,80,98,46]

student_1.sort()
student_2.sort()

sum = 0
for x in student_1:
    if x <40:
        print('Student 1: FAILED')
        break
    else:
        sum += x
    average = sum/len(student_1)
    print('Average number of student 1:', average)

for x in student_2:
    if x <40:
        print('Student 2: FAILED')
        break
    else:
        sum += x
    average = sum/len(student_2)
    print('Average number of student 2:', average)
