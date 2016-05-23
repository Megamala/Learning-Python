class Duck:
    def quack(self):
        print("Quaaaack!")

    def walk(self):
        print("Walks like a duck.")


def main():
    donald = Duck()
    print(donald)
    donald.quack()
    donald.walk()


if __name__ == "__main__":
    main()
