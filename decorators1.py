def args_logger(f):
    def inner(*args, **kwargs):
        print 'arguments were: ', args, kwargs
        f(*args, **kwargs)
    return inner


@args_logger
def fun1(x):
    return x + 1

@args_logger
def fun2(x, y):
    return x + y



fun1(10)

fun2(20, 30)

fun2(y = 1, x = 2)
