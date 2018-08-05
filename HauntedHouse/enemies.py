class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class Zombie(Enemy):
    def __init__(self):
        super().__init__(name = "Zombie", hp = 10, damage = 2)

class Vampire(Enemy):
    def __init__(self):
        super().__init__(name = "Vampire", hp = 10, damage = 3)

class Mickey(Enemy):
    def __init__(self):
        super().__init__(name = "Evil Mickey", hp = 10, damage = 2)

class Snoopy(Enemy):
    def __init__(self):
        super().__init__(name = "Evil Snoopy", hp = 10, damage = 2)

class Clown(Enemy):
    def __init__(self):
        super().__init__(name = "Clown", hp = 10, damage = 4)
