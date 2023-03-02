# CTI-110
# P2HW2 - List
# Tainiqur Faulkner
# Date: 3/2/2023
#

#create a list
grade_list = []
grade = float(input("Enter a grade for Module 1: "))
grade_list.append(grade)
grade = float(input("Enter a grade for Module 2: "))
grade_list.append(grade)
grade = float(input("Enter a grade for Module 3: "))
grade_list.append(grade)
grade = float(input("Enter a grade for Module 4: "))
grade_list.append(grade)
grade = float(input("Enter a grade for Module 5: "))
grade_list.append(grade)
grade = float(input("Enter a grade for Module 6: "))
grade_list.append(grade)

#print(grade_list)

print('-'*12, 'Results', '-'*12)

print('Lowest Grade:', str(min(grade_list)).rjust(16))
print('Highest Grade:', str(max(grade_list)).rjust(15))
print('Sum of Grades:', str(sum(grade_list)).rjust(15))
print('Average:', str(format(sum(grade_list)/len(grade_list),',.2f')).rjust(25))

print('-'*40)
