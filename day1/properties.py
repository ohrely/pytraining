class Wine:
    def __init__(self):
        self._age = 33

    @property
    def age(self):
        return self._age

drink = Wine()

print(drink.age)

# will fail:
# drink.age = 34
# del drink.age