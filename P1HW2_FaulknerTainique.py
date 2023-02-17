# This program calculates and displays travel expenses

# Feburary 16 2023

# CTI-110 P1HW2 - Travel Expense

# Tainique Faulkner

#

print('Enter Budget:', end=' ')
user_budget = int(input())

print('Enter your travel destination:', end=' ')
user_travel = (input())

print('How much do you think you will spend on gas?', end=' ')
user_gas = int(input())

print('Approximately, how much will you need for accomodation/hotel?', end=' ')
user_accommodation = int(input())

print('Last, how much do you need for food?', end=' ')
user_food = int(input())

print('------------Travel Expenses------------')
print('Location:', user_travel)
print('Initial Budget:', user_budget)
print('Fuel:', user_gas)
print('Accomodation:', user_accommodation)
print('Food:', user_food)

print('Remaining Balance:',user_budget - user_gas - user_accommodation - user_food)

