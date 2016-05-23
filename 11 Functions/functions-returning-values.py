def main():
    print(testfunc())
    print(testfunc2())
    print(testfunc3())

    for n in testfunc3():
        print(n, end=' ')


def testfunc():
    return "this is a test function"


def testfunc2():
    return 42


def testfunc3():
    return range(25)

if __name__ == "__main__":
    main()
