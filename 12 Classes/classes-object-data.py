class Duck:
    def __init__(self, **kwargs):
        self.variables = kwargs

    def quack(self):
        print("Quaaaack!")

    def walk(self):
        print("Walks like a duck.")

    def set_color(self, color):
        self.variables['color'] = color

    def get_color(self):
        return self.variables.get('color', None)

    def set_variable(self, k, v):
        self.variables[k] = v

    def get_variables(self, k):
        return self.variables.get(k, None)


def main():
    donald = Duck(feet=2)
    print(donald.get_color())
    donald.set_color('blue')
    print(donald.get_color())

    donald.set_variable('color', 'orange')
    print(donald.get_variables('color'))
    print(donald.get_variables('feet'))



if __name__ == "__main__":
    main()
