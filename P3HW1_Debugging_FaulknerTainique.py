# CTI-110

# P3HW1 - Debugging

# Tainiqur Faulkner

# Date: 3/21/2023

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))


grades=(mod_1, mod_2, mod_3, mod_4, mod_5, mod_6)
avg=sum(grades)/len(grades)
print(' ')
print('-'*12, 'Results', '-'*12)

print('Lowest Grade:', str(min(grades)).rjust(16))
print('Highest Grade:', str(max(grades)).rjust(15))
print('Sum of Grades:', str(sum(grades)).rjust(15))
print('Average:', str(format(sum(grades)/len(grades),',.2f')).rjust(22))
print('-'*40)

if avg >= 90:
    print('Your grade is: A')
else:
    if avg >= 80:
        print('Your grade is: B')
    else:
        if avg >= 70:
            print('Your grade is: C')
        else:
            if avg >= 60:
                print('Your grade is: D')
            else:
                print('Your grade is: F')






