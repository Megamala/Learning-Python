class Duck:
    def quack(self):
        print("Quaaaack!")

    def walk(self):
        print("Walks like a duck.")

    def bark(self):
        print("The duck cannot bark")

    def fur(self):
        print("The duck has feathers")


class Dog:
    def quack(self):
        print("The dog cannot quack")

    def walk(self):
        print("Walks like a dog")

    def bark(self):
        print("Woof")

    def fur(self):
        print("I have brown and white fur")


def main():
    donald = Duck()
    fido = Dog()
    in_the_forest(donald)
    in_the_pond(fido)

    for o in (donald, fido):
        o.quack()
        o.walk()
        o.fur()
        o.bark()


def in_the_forest(dog):
    dog.bark()
    dog.fur()


def in_the_pond(duck):
    duck.quack()
    duck.walk()


if __name__ == "__main__":
    main()
