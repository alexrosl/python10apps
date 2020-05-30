def area(a, b=10):
    return a * b


print(area(a=5))


def mean(*args):
    return sum(args) / len(args)


print(mean(1, 3, 413, 11))

def foo(*args):
    return sorted([value.upper() for value in args])


a = foo('bbb', 'aaa', 'ccc')


def mean2(**kwargs):
    max(kwargs, key=kwargs.get())
    return kwargs


print(mean2(a=1, b=2, c=3))
