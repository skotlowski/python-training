import time
from threading import Thread
length = 10000000

lista = []
for i in range(length):
    lista.append(i)


def calculation(start, end):
    counter = 0
    for i in range(start,end):
        lista[i] = lista[i] ** 2
        counter += 1
    print(counter)

started = time.time()
calculation(0, length)
elapsed = time.time() - started

print("(single thread) time elapsed: {:.2f}s".format(elapsed))

import threading
threadObj1 = threading.Thread(target=calculation, args=[0, int(length/4)])
threadObj2 = threading.Thread(target=calculation, args=[int(length/4), int(length/2)])
threadObj3 = threading.Thread(target=calculation, args=[int(length/2), int(length/4*3)])
threadObj4 = threading.Thread(target=calculation, args=[int(length/4*3), int(length)])

started = time.time()
threadObj1.start()
threadObj2.start()
threadObj3.start()
threadObj4.start()

threadObj1.join()
threadObj2.join()
threadObj3.join()
threadObj4.join()
elapsed = time.time() - started

print("(multithread) time elapsed: {:.2f}s".format(elapsed))