def main():
    testfunc(42)
    # all function arguments must have values
    testfunc2()


def testfunc(number, another=None, onemore=5):
    if another is None:
        another = 1122
    print("this is a test function", number, another, onemore)


def testfunc2():
    pass


# passes code and lets a stub (no code in a function) exist

# calls main at the top to allow code written after main
# able to be used in main
if __name__ == "__main__":
    main()
