
def print_msg(f):
    def new_f():
        print 'Beginning of function ...'
        f()
    return new_f


def fun1():
    print 'fun1 ...'

@print_msg
def fun2():
    print 'fun2 ...'


def fun3():
    print 'fun3 ...'

@print_msg
def fun4():
    print 'fun4 ...'



fun2()

fun4()
