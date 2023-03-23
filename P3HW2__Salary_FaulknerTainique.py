# CTI-110

# P3HW2 - Salary

# Tainique Faulkner

# Date

#

employee_name = (input("Enter employee's name: "))
hours = float(input('Enter number of hours worked: '))
pay_rate = float(input("Enter employee's pay rate: "))
overtime_pay = 0
overtime_hours = 0

if hours > 40:
    reg_pay = pay_rate * 40
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    gross_pay = overtime_pay + reg_pay
else:
    reg_pay = hours * pay_rate
    gross_pay = reg_pay + overtime_pay

print('-------------------------------------')
print('Employee name: ', employee_name)
print(' ')
print('Hours Worked ', '\t', 'Pay Rate ', '\t', 'OverTime', '\t', 'OverTime Pay', '\t', 'RegHour Pay', '\t', 'Gross Pay',)
print('-------------------------------------------------------------------------------------------------')
print(hours,'\t', '\t', pay_rate, '\t', '\t', overtime_hours, '\t', '\t', overtime_pay, '\t', reg_pay, '\t', '\t', gross_pay)

    
 





    
