import time


def whats_my_name(function):
    def wrapped(*args, **kwargs):
        # przed wykonaniem funkcji
        start = time.time()
        result = function(*args, **kwargs)
        # po wykonaniu funkcji
        print('Execution time:', time.time() - start)
        return result

    return wrapped


@whats_my_name
def foo():
    time.sleep(10)


foo()
