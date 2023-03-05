from threading import Thread
from time import sleep
from random import random


class CountingThread(Thread):
    def __init__(self, n):
        Thread.__init__(self)
        self.n = n

    def run(self):
        print(f'Starting thread {self.n}')
        for m in range(10):
            sleep(random())
            print(f'Thread {self.n}, {m}\'th iteration')
        print(f'Thread {self.n} exiting')

threads = [CountingThread(n) for n in range(5)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print('All threads finished')

#-----------------------------------------------------------------

from threading import Thread

counter = 0

def count():
    global counter
    counter = counter + 1

threads = [Thread(target=count) for i in range(20)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f'Threads finished, counter={counter}')

#------------------------------------------------------

from threading import Thread
from time import sleep
from random import random

counter = 0

def count():
    global counter
    sleep(5*random())
    x = counter + 1
    sleep(random())
    counter = x
    print(x)

threads = [Thread(target=count) for i in range(20)]
for t in threads:
    t.start()

for t in threads:
    t.join()

print(f'Threads finished, counter={counter}')

#----------------------

from threading import Thread, RLock
from time import sleep
from random import random

counter = 0
lock = RLock()

def count():
    global counter
    sleep(5*random())
    #lock.acquire() # we acquire lock before modifying the counter
    with lock:
        x = counter + 1
        sleep(random())
        counter = x
    #lock.release() # we release the lock after modifying the counter
    print(x)

threads = [Thread(target=count) for i in range(20)]
for t in threads:
    t.start()

for t in threads:
    t.join()

print(f'Threads finished, counter={counter}')
