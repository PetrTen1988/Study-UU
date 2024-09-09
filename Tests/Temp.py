class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        print(self.age)

    def __del__(self):
        return (self.name)

den = Human('123', '22')

print(dir(den))
# del den

# den.birthday()
