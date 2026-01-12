
class Tank:
        
    def __init__(self, name, earthquake):
        self.name = name
        self.health = 130
        self.attack = 20
        self.armor = 80
        self.level = 1
        self.exp = 0
        self.maxhealth = 130
        self.ability = earthquake
        self.damage_type = "physical"
        self.coin = 100

    def takedamage(self, damage, damage_type):
        if damage_type == 'magical':
            damage_after_armor = damage * 0.75
        else:
            damage_after_armor = max(0, damage - self.armor)
            
        self.health -= damage_after_armor
        self.health = max(0, self.health)
    def attack_dmg(self, target):

        target.takedamage(self.attack, self.damage_type)
    def gain_exp(self, amount):
        self.exp += amount
        print(f"{self.name} gained {amount} EXP!")

        while self.exp >= self.exp_to_next_level():
            self.exp -= self.exp_to_next_level()
            self.level_up()

    def exp_to_next_level(self):
        return self.level * 100

    def level_up(self):
        self.level += 1
        self.maxhealth += 20
        self.attack += 5
        self.armor += 2
        self.health = self.maxhealth

        print(f"{self.name} leveled up to Level {self.level}!")


class Mage:
    def __init__(self, name, strike):
        self.name = name
        self.health = 100
        self.maxhealth = 100
        self.attack = 35
        self.armor = 2
        self.level = 1
        self.exp = 0
        self.ability = strike
        self.damage_type = "magical"
        self.coin = 100
    def takedamage(self, damage, damage_type):
        if damage_type == "magical":
            damage_after_armor = damage * 0.7
        else:
            damage_after_armor = damage

        self.health = max(0, self.health - damage_after_armor)

    def attack_dmg(self, target):
        target.takedamage(self.attack, self.damage_type)
    
    def gain_exp(self, amount):
        self.exp += amount
        print(f"{self.name} gained {amount} EXP!")

        while self.exp >= self.exp_to_next_level():
            self.exp -= self.exp_to_next_level()
            self.level_up()

    def exp_to_next_level(self):
        return self.level * 100

    def level_up(self):
        self.level += 1
        self.maxhealth += 20
        self.attack += 5
        self.armor += 2
        self.health = self.maxhealth

        print(f"{self.name} leveled up to Level {self.level}!")



class Healer:
    def __init__(self, name, fullheal):
        self.name = name
        self.health = 85
        self.maxhealth = 85
        self.attack = 10
        self.armor = 3
        self.level = 1
        self.exp = 0
        self.ability = fullheal
        self.damage_type = "magical"
        self.coin = 100
    def heal(self, target):
        heal_amount = 20
        target.health = min(target.maxhealth, target.health + heal_amount)

    def takedamage(self, damage, ):
        self.health = max(0, self.health - damage)

    def attack_dmg(self, target):
        target.takedamage(self.attack, self.damage_type)

    def gain_exp(self, amount):
        self.exp += amount
        print(f"{self.name} gained {amount} EXP!")

        while self.exp >= self.exp_to_next_level():
            self.exp -= self.exp_to_next_level()
            self.level_up()

    def exp_to_next_level(self):
        return self.level * 100

    def level_up(self):
        self.level += 1
        self.maxhealth += 20
        self.attack += 5
        self.armor += 2
        self.health = self.maxhealth

        print(f"{self.name} leveled up to Level {self.level}!")

class Warrior:
    def __init__(self, name, power_strike):
        self.name = name
        self.health = 100
        self.maxhealth = 100
        self.attack = 15
        self.armor = 5
        self.level = 1
        self.exp = 0
        self.ability = power_strike
        self.damage_type = "physical"

    def takedamage(self, damage):
        reduced_damage = max(0, damage - self.armor)
        self.health = max(0, self.health - reduced_damage)

    def attack_dmg(self, target):
        target.takedamage(self.attack)

    def gain_exp(self, amount):
        self.exp += amount
        print(f"{self.name} gained {amount} EXP!")

        while self.exp >= self.exp_to_next_level():
            self.exp -= self.exp_to_next_level()
            self.level_up()

    def exp_to_next_level(self):
        return self.level * 100

    def level_up(self):
        self.level += 1
        self.maxhealth += 25
        self.attack += 5
        self.armor += 2
        self.health = self.maxhealth

        print(f"{self.name} leveled up to Level {self.level}!")

