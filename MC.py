
class Tank:
    def __init__(self, name, health, attack, armor, level, exp, maxhealth, defense_ability):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor 
        self.level = level
        self.exp = exp
        self.maxhealth = maxhealth
        self.defense_ability = defense_ability
    def takedamage(self, damage, damage_type = 'physical'):
        if damage_type == 'magical':
            damage_after_armor = damage * 0.75
        else:
            damage_after_armor = max(0, damage - self.armor)
            
        self.health -= damage_after_armor
        self.health = max(0, self.health)
    def attack_dmg(self, damage):

        


