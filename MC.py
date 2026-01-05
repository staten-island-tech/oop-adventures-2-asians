
class Tank:
    def __init__(self, name, health, attack, armor, level, exp, maxhealth, ability, damage_type):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor 
        self.level = level
        self.exp = exp
        self.maxhealth = maxhealth
        self.defense_ability = ability
        self.damage_type = damage_type

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