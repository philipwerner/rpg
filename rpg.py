import random


class RPG(object):
    """."""
    
    def __init__(self):
        """."""
        self.health = 10
        self.stamina = 15
        self.strength = 10
        self.intelligence = 5
        self.dex = 5
        self.luck = 2
        self.hp = 0
        self.attack = None
        self.bonus = None
        self.mp = 5

class Fighter(RPG):
        """."""
        self.health = random.randint(10, 25)
        self.hp = self.health * 1.5
        self.stamina = self.stamin + self.health
        self.dex = 5 * random.randint(1, 4)
        moves = ['Slam', 'Rage', 'Slash']
        x = random.randit(0, 2)
        self.attack = moves[x]

class Mage(RPG):
        """."""
        self.hp = self.health * 1.5
        self.stamina = self.stamin + self.health
        self.mp = random.randint(10, 25)
        self.intelligence = self.mp * .9
        moves = ['Fireball', 'Ice Orb', 'Tornado', 'Static', 'Heal']
        x = random.randit(0, 3)
        self.attack = moves[x]
        if self.mp > 24:
            self.bonus = moves[4]
