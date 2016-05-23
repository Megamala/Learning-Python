class Animal:
    def talk(self):
        print('I have something to say!')

    def walk(self):
        print("hey im walking here")

    def clothes(self):
        print("I have nice clothes")


class Duck(Animal):
    def quack(self):
        print("Quaaaack!")

    def walk(self):
        super().walk()
        print("Walks like a duck.")


class Dog(Animal):
    def clothes(self):
        print("I have brown and white fur")


def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    donald.clothes()

    fido = Dog()
    fido.walk()
    fido.clothes()


if __name__ == "__main__":
    main()
