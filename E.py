'''Enemies Classes'''

class goblin:
    def __init__(self, name, health, attack, armor, fast_daggers):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor 
        self.ability = fast_daggers


class skellyton:
    def __init__(self, name, health, attack, armor, arrow_rain):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor      
        self.ability = arrow_rain


class robber:
    def __init__(self, name, health, attack, armor, combat_steal_item):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor      
        self.ability = combat_steal_item


class boss_slime:
    def __init__(self, name, health, attack, armor, combat_steal_item):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor      
        self.ability = combat_steal_item