# Travel expenses cost

# 3/1/23

# CTI-110 P2HW1 - Travel

# Tainique Faulkner

#

print('This program calculates and displays travel expenses')

print(' ')

print('Enter Budget:', end=' ')
user_budget = int(input())
print(' ')

print('Enter your travel destination:', end=' ')
user_travel = (input())
print(' ')

print('How much do you think you will spend on gas?', end=' ')
user_gas = int(input())
print(' ')

print('Approximately, how much will you need for accomodation/hotel?', end=' ')
user_accommodation = int(input())
print(' ')

print('Last, how much do you need for food?', end=' ')
user_food = int(input())
print(' ')

print('------------Travel Expenses------------')
print('Location:', str(user_travel).rjust(18))
print('Initial Budget:', '$'.rjust(5),str(user_budget))
print('Fuel:', '$'.rjust(15), str(user_gas))
print('Accomodation:', '$'.rjust(7), str(user_accommodation))
print('Food:', '$'.rjust(15), str(user_food))
print('---------------------------------------')

print('Remaining Balance:', '$'.rjust(2),str(user_budget - user_gas - user_accommodation - user_food))
