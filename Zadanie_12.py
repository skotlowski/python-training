import time 
def whats_my_name(function):
     def wrapped(*args, **kwargs):
         # przed wykonaniem funkcji
        print('You are currently executing:', function.__name__)
        result = function(*args, **kwargs)
         #po wykonaniu funkcji
        print('Executing is over:', function.__name__)
        return result
     return wrapped


@whats_my_name
def foo(x):
    print('Witaj x')


foo('Paweł')


@whats_my_name
def xxx():
    pass

xxx()


