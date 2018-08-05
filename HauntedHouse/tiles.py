import items, enemies, actions, world

class Maptile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves

class StartingRoom(Maptile):
    def intro_text(self):
        return """
        Right before Halloween, you received an email that invited you to the best haunted house.  The address was way out in the middle of nowhere, but you were excited to take your girlfriend or boyfriend to it to scare the bejeezies out of them.
        They text you and say they will meet you there, so you pack up to head out.

        As you are about to leave your house, you reach down and grab:
        1. A maglight flash light
        2. A 32oz HydroFlask filled with a Kolsch beer
        3. Your iPhone charger cable"""

    def modify_player(self, player):
        pass

class EmptyHallway(Maptile):
    def intro_text(self):
        return"""
        You reached another empty hallway closer to exiting this crazy place.  Continue."""

    def modify_player(self, player):
        pass

class LootRoom(Maptile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, the_player):
        the_player.inventory.append(self.item)

    def modify_player(self, the_player):
        self.add_loot(the_player)

class EnemyRoom(Maptile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("The enemy does {} damage. You have {} hp remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class Doorway(Maptile):
    def intro_text(self):
        return
        """
        You arrive to the haunted house and see your partner's car parked outside.  It's odd that they aren't waiting for you, but you get out and walk towards the door to find them inside, hopefully.
        You reach the doorway to the haunted house, and on your way up the steps you see a clown sitting in a rocking chair.
        He doesn't move, so you open the door and go inside."""

    def modify_player(self, player):
        pass

class LivingRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Vase())

    def intro_text(self):
        return
        """
        You enter the haunted house and see a white vase.
        You are already a little fearful so you pick it up just in case."""


class Kitchen(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Knife())

    def intro_text(self):
        return
        """
        You made it to the kitchen. Lucky you! There is a big sharp butcher knife on the counter.
        You pick it up, and guess what! It's the most powerful weapon!"""


class ZombieRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A Zombie jumps in front of you.  You think it's just a scare prank, but then he slashes you with a knife.
            """
        else:
            return """
            The corpse of that crazy vampire attacker lies still on the ground."""

class VampireRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Vampire())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            This time it's a vampire.  You look for a way out of this bedroom but the door is locked behind you.
            You decide that you have to fight."""
        else:
            return """
            The vampire actor is dead.  He tried to murder you but you won."""


class MickeyRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Mickey())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            What's this? Mickey Mouse?  You didn't go to Disneyworld.  But suddenly you notice the glare in his eyes and the axe in his hands..."""
        else:
            return """
            Phew.  That was close.  Luckily you dodged the blows and got to Mickey first."""

class SnoopyRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Snoopy())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            From the floppy ears and the long nose and the face shaped like a dog, you know it's Snoopy.  But this Snoopy has a katana."""
        else:
            return """
            Maybe this Snoopy had ninja moves, but you had...luck."""

class ClownRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Clown())

    def intro_text(self):
        if enemy.self.is_alive():
            return """
            You enter the bedroom upstairs and realize you are blocked by the same clown you saw on the front porch.
            Suddenly you realize that maybe this was all planned from the beginning.  Your girlfriend never showed up.
            And then there she is, lying dead on the floor in a pool of blood."""
        else:
            return """
            You slam the clown to the ground one last time, and he doesn't move anymore."""

class SnakePitRoom(Maptile):
    def intro_text(self):
        return """
        You have fallen into a pit of deadly snakes!

        You have died!
        """

    def modify_player(self, player):
        player.hp = 0

class LeaveRoom(Maptile):
    def intro_text(self):
        return """
        You see the sun coming up outside and no enemy is in this room...

        You escaped alive and victory is yours!"""

    def modify_player(self, player):
        player.victory = True
