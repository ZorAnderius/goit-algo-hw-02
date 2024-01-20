from colorama import Fore
from task1 import task1
from task2 import task2

def main():   
    while True:
        print(Fore.BLUE+ 'Please choose task:')
        print(Fore. WHITE + '    1. Task1: simulation of acceptance and processing of applications (exit for simulation CTRL+C)')
        print(Fore.WHITE + '    2. Task2: work with two-way queue')
        print(Fore.WHITE + '    3. Exit the program')
        user_input = input(Fore.YELLOW + "Task:  ")
        if user_input:
            if user_input == '1':
                task1()
            elif user_input == '2':
                task2()
            elif user_input == '3':
                print(Fore.BLUE + 'Good bye!')
                break
            else:
                print(Fore.RED + 'Wrong input')

if __name__ == '__main__':
    main()