from colorama import Fore
from queue import Queue
import random
from time import sleep

class Application():
    def __init__(self, title):
        self.title = title
        self.task = random.randint(1, 10)

class ServiceCenter():
    def __init__(self):
        self.applications = Queue()

    def generate_request(self):
        for i in range(random.randint(1, 10)):
            if i: 
                self.applications.put(Application(f'Application {i}'))
        
    def process_request(self):
        print(Fore.BLUE + 'Exit for simulation CTRL+C')
        if not self.applications.empty():
            application = self.applications.get()
            for i in range(1, application.task):
                print(Fore.WHITE + f'Processing application {application.title} with Task{i}')
                sleep(random.randint(1,3))
        else:
            print(Fore.BLUE + 'Queue is empty')

def task1():
    service_center = ServiceCenter()
    try:
        while True:
            service_center.generate_request()
            service_center.process_request()
    except KeyboardInterrupt:
        print(Fore.YELLOW + 'Exiting...')
        sleep(2)
        

if __name__ =='__main__':
    task1()