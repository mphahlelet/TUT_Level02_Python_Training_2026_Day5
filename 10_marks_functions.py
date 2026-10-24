######### LISTS
import sys

#List and Function
def get_marks():
    marks = []
    mark = int(input("Enter mark (or -1 to stop): "))

    while mark != -1:
        marks.append(mark)
        mark = int(input("Enter mark (or -1 to stop): "))

    return marks

def print_list_size(marks):
    print('')
    print(f'Our list has {len(marks)} elements.')

def print_marks():
    for x in range(len(marks)):
        print(f'Mark {x+1} is {marks[x]}')
    
def get_sum_of_marks(marks):
    sum = 0
    for x in range(len(marks)):
        mark = marks[x]
        sum = sum + mark
    return sum

def get_average():
    total = 0
    for x in range(len(marks)):
        mark = marks[x]
        total = total + mark
    
    avg = total / len(marks)
    print(f'The average of all marks ={avg:.2f}')

def determine_highest(marks):
    highest = 0
    for i in range(len(marks)):
        current_mark = marks[i]
        if current_mark > highest:
            highest = current_mark
            
    print(f'The highest mark is {highest}')
        
menu = 'Press 1: To capture marks\n'
menu += 'Press 2: To check number of marks\n'
menu += 'Press 3: To calculate average of marks\n'
menu += 'Press 4: To find highest mark\n'
menu += 'Press -1: To exit\n'

print(menu)
choice = int(input('Make your choice: '))

entered_marks = []
if choice == 1:
    entered_marks = get_marks()
    print(entered_marks)
elif choice == 2:
    print_list_size(entered_marks)
elif choice == 3:
    calc_sum = get_sum_of_marks(entered_marks)
    print(f'Sum of all marks = {calc_sum}')
elif choice == 4:
    determine_highest(entered_marks)
elif choice == -1:
    sys.exit(0)
else:
    print('Wrong choice entered!')


