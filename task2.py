from colorama import Fore
from collections import deque
from time import sleep

def init_deque(queue):
    print(Fore.BLUE + 'Exit for task2 press CTRL+C')
    word = input(Fore.BLUE + 'Enter word: ')
    for ch in word:
        queue.append(ch)
    return word

def check_palindrome(queue):
    while len(queue):
        if queue.pop().lower() != queue.popleft().lower():
            return False
        if len(queue) == 1:
            break
    return True

def task2():
    try:
        while True:
            palindrome_queue = deque()
            word = init_deque(palindrome_queue)
            print(Fore.GREEN + f'\'{word}\' is a palindrome') if check_palindrome(palindrome_queue) else print(Fore.LIGHTMAGENTA_EX + f'\'{word}\' is not a palindrome')
    except KeyboardInterrupt:
        print(Fore.YELLOW + 'Exiting...')
        sleep(2)

if __name__ == '__main__':
    task2()