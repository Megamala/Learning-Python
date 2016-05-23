def main():
    testfunc(5, 6, 7, 8, 9, 10, one=1, two=2, four=42)


# named arguments first, arbitrary tuple after, and keyword args after
def testfunc(this, that, other, *args, **kwargs):
    print("this is a test function",
          this, that, other, args,
          kwargs['one'], kwargs['two'], kwargs['four'])

    for k in kwargs:
        print(k, kwargs[k])

    for n in args:
        print(n)


if __name__ == "__main__":
    main()
