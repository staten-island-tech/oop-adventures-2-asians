
class Tank:
    def __init__(self, name, health, attack, armor, level, exp, maxhealth, ability, damage_type):
        self.name = name
        self.health = 130
        self.attack = 20
        self.armor = 80
        self.level = 1
        self.exp = 0
        self.maxhealth = 130
        self.defense_ability = ability
        self.damage_type = "physical"

    def takedamage(self, damage, damage_type):
        if damage_type == 'magical':
            damage_after_armor = damage * 0.75
        else:
            damage_after_armor = max(0, damage - self.armor)
            
        self.health -= damage_after_armor
        self.health = max(0, self.health)
    def attack_dmg(self, target):
        """Attack another character"""
        target.takedamage(self.attack, self.damage_type)


class Mage:
    def __init__(self, name):
        self.name = name
        self.health = 80
        self.maxhealth = 80
        self.attack = 35
        self.armor = 2
        self.level = 1
        self.exp = 0
        self.damage_type = "magical"

    def takedamage(self, damage, damage_type):
        if damage_type == "magical":
            damage_after_armor = damage * 0.7
        else:
            damage_after_armor = damage

        self.health = max(0, self.health - damage_after_armor)

    def attack_dmg(self, target):
        target.takedamage(self.attack, self.damage_type)



class Healer:
    def __init__(self, name):
        self.name = name
        self.health = 85
        self.maxhealth = 85
        self.attack = 10
        self.armor = 3
        self.level = 1
        self.exp = 0
        self.damage_type = "magical"

    def heal(self, target):
        heal_amount = 20
        target.health = min(target.maxhealth, target.health + heal_amount)

    def takedamage(self, damage, ):
        self.health = max(0, self.health - damage)

    def attack_dmg(self, target):
        target.takedamage(self.attack, self.damage_type)

    def levelup(self,)