def main():
    print("This is the functions.py file.")
    for i in inclusive_range(0, 25, 1):
        print(i, end=" ")
    for i in inclusive_range2(5, 25):
        print(i, end=" ")


def inclusive_range(start, stop, step):
    i = start
    while i <= stop:
        yield i
        i += step


def inclusive_range2(*args):
    numargs = len(args)
    if numargs < 1:
        raise TypeError('requires at least one argument')
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError('inclusive_range2 expected at most 3 arguments, got {}'.format(numargs))
    i = start
    while i <= stop:
        yield i
        i += step


if __name__ == "__main__":
    main()
