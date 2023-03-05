from threading import Thread, RLock
from time import sleep
from random import random, choice

locks = [RLock(), RLock()]

def f(n):
    def h():
        for i in range(10):
            sleep(random())
            c = choice([0, 1])
            print(f'{n}, {i} Acquiring {c}')
            with locks[c]:
                sleep(random())
                print(f'{n}, {i} Acquiring {1-c}')
                with locks[1-c]:
                    print(f'{n}, {i} Crirical section')
                    sleep(random())
            print(f'{n}, {i} released')
    return h

threads = [Thread(target=f(i))
           for i in range(5)]
for t in threads:
    t.start()


    #---------------------------\

locks = [RLock(), RLock()]

def f(n):
    def h():
        for i in range(10):
            sleep(random())
            print(f'{n}, {i} Acquiring {0}')
            with locks[0]:
                sleep(random())
                print(f'{n}, {i} Acquiring {1}')
                with locks[1]:
                    print(f'{n}, {i} Crirical section')
                    sleep(random())
            print(f'{n}, {i} released')
    return h


threads = [Thread(target=f(i))
           for i in range(5)]
for t in threads:
    t.start()
