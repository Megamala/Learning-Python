def main():
    try:
        for line in readfile('xlines.doc'):
            print(line.strip())
    except IOError as e:
        print("cannot read file", e)
    except ValueError as e:
        print("bad filename", e)


def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else:
        raise ValueError('Filename must end with .txt')

# http://docs.python.org/library/exceptions.html
# for list of exceptions usable in python

if __name__ == "__main__":
    main()
