class Item:
    def __init__(self, name, rarity, stats=None):
        self.name = name
        self.rarity = rarity
        self.stats = stats or {}

    # def rarity_multiplier(self):
    #     if self.rarity == "uncommon":
    #         return 1.1
    #     elif self.rarity == "epic":
    #         return 1.4
    #     elif self.rarity == "mythic":
    #         return 1.8
    #     else:
    #         return 1.0

# change this to the thing in shop.py later``

    def get_scaled_stats(self):
        scaled_stats = {}
        multiplier = self.rarity_multiplier()
        for stat in self.stats:
            scaled_stats[stat] = int(self.stats[stat] * multiplier)
        return scaled_stats
    
'''----------------------------------------------'''

class Armor(Item):
    def __init__(self, name, slot, rarity, stats):
        super().__init__(name, rarity, stats)
        self.slot = slot
        #hel, chest, leg, boot

'''---------------------------------------------------'''

class Weapon(Item):
    def __init__(self, name, rarity, stats):
        super().__init__(name, rarity, stats)

'''---------------------------------------------'''


class Potion:
    def __init__(self, name, effect, value):
        self.name = name
        self.effect = effect
        self.value = value

    def use(self, target):
        if self.effect == "health":
            target.health += self.value
            if target.health > target.maxhealth:
                target.health = target.maxhealth
        elif self.effect == "attack":
            target.attack += self.value
        elif self.effect == "armor":
            target.armor += self.value
        elif self.effect == "maxhealth":
            target.maxhealth += self.value

        #fix this later in main or smth idk


'''------------------------------------------------'''

class multiinv:
    def __init__(self):
        self.helmet = None
        self.chestplate = None
        self.leggings = None
        self.boots = None
        self.weapon = None

        self.potions = []
        #set max 3 

    def equip_armor(self, armor):
        if armor.slot == "helmet":
            self._equip_slot("helmet", armor)
        elif armor.slot == "chest":
            self._equip_slot("chestplate", armor)
        elif armor.slot == "leggings":
            self._equip_slot("leggings", armor)
        elif armor.slot == "boots":
            self._equip_slot("boots", armor)

    def equip_wep(self, weapon):
        self._equip_slot("weapon", weapon)

    def _equip_slot_helmet(self, item):
        if self.helmet is not None:
            self._remove_item_stats(self.helmet)
        self.helmet = item
        self._apply_item_stats(item)

    def _equip_slot_chestplate(self, item):
        if self.chestplate is not None:
            self._remove_item_stats(self.chestplate)
        self.chestplate = item
        self._apply_item_stats(item)

    def _equip_slot_leggings(self, item):
        if self.leggings is not None:
            self._remove_item_stats(self.leggings)
        self.leggings = item
        self._apply_item_stats(item)

    def _equip_slot_boots(self, item):
        if self.boots is not None:
            self._remove_item_stats(self.boots)
        self.boots = item
        self._apply_item_stats(item)

    def _equip_slot_weapon(self, item):
        if self.weapon is not None:
            self._remove_item_stats(self.weapon)
        self.weapon = item
        self._apply_item_stats(item)



    
    def _apply_item_stats(self, item):
        stats = item.get_scaled_stats()
        for stat in stats:
            if stat == "health":
                self.health += stats[stat]
                self.maxhealth += stats[stat]
            elif stat == "attack":
                self.attack += stats[stat]
            elif stat == "armor":
                self.armor += stats[stat]
            elif stat == "maxhealth":
                self.maxhealth += stats[stat]


    def _remove_item_stats(self, item):
        stats = item.get_scaled_stats()
        for stat in stats:
            if stat == "health":
                self.health -= stats[stat]
                self.maxhealth -= stats[stat]
                if self.health < 0:
                    self.health = 0
            elif stat == "attack":
                self.attack -= stats[stat]
            elif stat == "armor":
                self.armor -= stats[stat]
            elif stat == "maxhealth":
                self.maxhealth -= stats[stat]
                if self.health > self.maxhealth:
                    self.health = self.maxhealth


    def add_potion(self, potion):
        if len(self.potions) < 3:
            self.potions.append(potion)

    def use_potion(self, index):
        if index >= 0 and index < len(self.potions):
            potion = self.potions.pop(index)
            potion.use(self)


# fixed version of mc idk

class Tank(multiinv):
    def __init__(self, name, earthquake):
        multiinv.__init__(self)
        self.name = name
        self.health = 130
        self.maxhealth = 130
        self.attack = 20
        self.armor = 80
        self.level = 1
        self.exp = 0
        self.ability = earthquake
        self.damage_type = "physical"

    def takedamage(self, damage, damage_type):
        if damage_type == "magical":
            damage_after_armor = damage * 0.75
        else:
            damage_after_armor = max(0, damage - self.armor)
        self.health -= damage_after_armor
        if self.health < 0:
            self.health = 0

    def attack_dmg(self, target):
        target.takedamage(self.attack, self.damage_type)

    def gain_exp(self, amount):
        self.exp += amount
        print(f"{self.name} gained {amount} exp.")
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
        print(f"{self.name} leveled up to Level {self.level}")

        