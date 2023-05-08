# CTI-110

# P4HW1 - Score List

# Tainique Faulkner

# 4/18/2023

#

# create a list
grade_list = []


num_scores = int(input("How many scores do you want to enter? "))
print("")


for i in range(num_scores):
    grade = float(input(f"Enter score #{i+1}: "))
    
    
    while grade < 0 or grade > 100:
        print("")
        print("INVALID Score Entered!!!!\nScore should be between 0 and 100")
        grade = float(input(f"Enter score #{i+1} again: "))
    
    

    grade_list.append(grade)

average = sum(grade_list) / len(grade_list)


if average >= 90:
    letter_grade = 'A'
elif average >= 80:
    letter_grade = 'B'
elif average >= 70:
    letter_grade = 'C'
elif average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'


print("")
print("")
print('-' * 12, 'Results', '-' * 12)
print('Lowest Score\t:', str(min(grade_list)))
grade_list.remove(min(grade_list))
print('Modified List\t:', grade_list)
average = sum(grade_list) / len(grade_list)
print('Scores Average\t:', str(format(average, ',.2f')))
print('Grade\t\t:', letter_grade)
print('-' * 40)
