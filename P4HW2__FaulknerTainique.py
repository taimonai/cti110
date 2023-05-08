# CTI-110

# P4HW2 - Salary Calculator

# Tainique Faulkner

# 04/27/2023

#

overtime_total = 0.0
reg_pay_total = 0.00
gross_pay_total = 0
employee_count = 0


while True:
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    if employee_name.lower() == 'done':
        break
    
   
    hours = float(input("How many hours worked? "))
    pay_rate = float(input("What is the pay rate? "))
    
    
    
    overtime_pay = 0.00
    overtime_hours = 0
    if hours > 40:
        reg_pay = pay_rate * 40
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        gross_pay = overtime_pay + reg_pay
    else:
        reg_pay = hours * pay_rate
        gross_pay = reg_pay + overtime_pay
    
    overtime_total += overtime_pay
    reg_pay_total += reg_pay
    gross_pay_total += gross_pay
    employee_count += 1
    
    print(' ')
    print('Employee name: ', employee_name)
    print(' ')
    print('Hours Worked ', '\t', 'Pay Rate ', '\t', 'OverTime', '\t', 'OverTime Pay', '\t', 'RegHour Pay', '\t', 'Gross Pay',)
    print('-------------------------------------------------------------------------------------------------')
    print(hours,'\t', '\t', pay_rate, '\t', '\t', overtime_hours, '\t', '\t', overtime_pay, '\t', '\t', reg_pay, '\t', '\t', gross_pay)
    print(' ')
    print(' ')

print(' ')
print('Total number of employees entered:', employee_count)
print('Total amount paid for overtime:', overtime_total)
print('Total amount paid for regular hours:', reg_pay_total)
print('Total gross pay:', gross_pay_total)
