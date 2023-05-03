# CTI-110

# P5HW - Math Quiz

# Tainique Faulkner

# 5/2/2023

#


print("Welcome to the Math Quiz")
print("")
print("")
print("MAIN MENU")
print("-"*20)
print("1. Adding Random Numbers")
print("2. Subtracting Random Numbers")
print("3. Exit")
print("")
print("Please choose one of the menu options: ", end='')
choice = int(input())



def menu():
    choice = 0
    while choice != 3:
        print("Welcome to the Math Quiz")
        print("")
        print("")
        print("MAIN MENU")
        print("-"*20)
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        print("")
        print("Please choose one of the menu options: ", end='')
        choice = int(input())


        if choice == 1:
            add()
            print("")
        elif choice == 2:
            subtract()
            print("")
        elif choice == 3:
            print("Thank you for playing...")
            print("Bye!!")
        else:
            print("Bad choice. Try again! ")
            print("")
            
    
def add():
    print("Addition Function")

def subtract():
    print("Subtraction Function")
    

import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
correct_answer = num1 + num2
guesses = 0

print(f"{num1}".rjust(4))
print(f"+ {num2}")
print("")
print("Enter answer.")
while True:
    answer = int(input())
    guesses += 1
    if answer == correct_answer:
        print(f"Congratulations!!!! Your answer is correct.")
        print(f"Number of guesses: {guesses}")
        break
    elif answer < correct_answer:
        print("Sorry, guess is too low.")
        print("")
        print("Try again: ", end='')
    else:
        print("Sorry, guess is too high.")
        print("")
        print("Try again: ", end='')
        
        
print("")
print("MAIN MENU")
print("-"*20)
print("1. Adding Random Numbers")
print("2. Subtracting Random Numbers")
print("3. Exit")
print("")
print("Please choose one of the menu options: ", end='')
choice = int(input())



if choice == 1:
    add()
    print("")
elif choice == 2:
    subtract()
    print("")
elif choice == 3:
    print("Thank you for playing...")
    print("Bye!!")
else:
    print("Bad choice. Try again! ")
    print("")

