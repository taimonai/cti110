# Define your function here.
def days_in_feb(entered_year):
    days = 28                   
    if ((entered_year % 4 == 0) and (entered_year % 100 != 0)) or (entered_year % 400 == 0):
        days = 29               
    return days

if __name__ == '__main__':
    while True:
        user_year = int(input(""))
        if user_year == 9999:
            break
        print(f'{user_year} has {days_in_feb(user_year)} days in February.')
    # Type your code here. Your code must call the function.