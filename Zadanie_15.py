import threading
import time


def zrob_drzemke(x):
    time.sleep(x)
    print('Obudziłem się')


print("Start programu")
#zrob_drzemke()
thread_obj = threading.Thread(target=zrob_drzemke, args=[3])
thread_obj.start()
print('Hello')
thread_obj.join()
print("Koniec programu")
