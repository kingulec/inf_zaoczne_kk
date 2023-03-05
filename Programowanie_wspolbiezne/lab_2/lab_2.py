from threading import Thread, Condition
from time import sleep
from random import random, choice
cond = Condition()
N = 0
def inc(n, i):
    global N
    with cond:
        print(f'Thread {n}, {i}\'th increment, N = {N}')
        N = N + 1
        cond.notify()
def dec(n, i):
    global N
    with cond:
        print(f'Thread {n} tries {i}\'th decrement, N = {N}. Waiting ...')
        cond.wait_for(lambda:N>0)
        print(f'Thread {n}, {i}\'th decrement, N = {N}')
        N = N - 1
def get(n):
    f = choice([inc, dec, inc, inc])
    def h():
        for i in range(10):
            sleep(random())
            f(n,i)
    return h
threads = [Thread(target = get(n)) for n in range(10)]
for t in threads:
    t.start()