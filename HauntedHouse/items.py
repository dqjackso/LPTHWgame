
class Item():
    def __init__(self, name, description, quantity):
        self.name = name
        self.description = description
        self.quantity = quantity

    def __str__(self):
        return ("{}\n=====\n{}\nQuantity:{}").format(self.name, self.description, self.quantity)

class Weapon(Item):
    def __init__(self, name, description, quantity, damage):
        self.damage = damage
        super().__init__(name, description, quantity)

    def __str__(self):
        return ("{}\n=====\n{}\nQuantity:{}\nDamage:{}").format(self.name, self.description, self.quantity, self.damage)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name = "Rock", description = "A small rock with some sharp edges.", quantity = 1, damage = 2)

class Flashlight(Weapon):
    def __init__(self):
        super().__init__(name = "Flashlight", description = "A large police maglight with almost dead batteries.", quantity = 1, damage = 4)

class Cable(Weapon):
    def __init__(self):
        super().__init__(name = "Phone Charging Cable", description = "A 36 inch long phone charging cable.", quantity = 1, damage = 5)

class Phone(Weapon):
    def __init__(self):
        super().__init__(name = "Phone", description = "An iPhone X, you richy rich.", quantity = 1, damage = 1)

class Wallet(Weapon):
    def __init__(self):
        super().__init__(name = "Wallet", description = "Your black leather wallet.", quantity = 1, damage = 0)

class HydroFlask(Weapon):
    def __init__(self):
        super().__init__(name = "HydroFlask", description = "Your 64oz almost-bullet proof bottle that is full of some delicious beer.", quantity = 1, damage = 6)

class Vase(Weapon):
    def __init__(self):
        super().__init__(name = "Vase", description = "A white geometric glass vase.", quantity = 1, damage = 3)

class Knife(Weapon):
    def __init__(self):
        super().__init__(name = "Knife", description = "A large chef's knife.", quantity = 1, damage = 7)

class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         quantity=self.amt)
