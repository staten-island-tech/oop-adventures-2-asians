import random
class Shop:
    selected_items_cart = []
    total = 0
    def __init__(self, uncommon, epic, mythic):
        self.uncommon = uncommon
        self.epic = epic
        self.mythic = mythic 
    


    
    def buy(self, coin, price, selected_items_cart, inv):
        if coin >= price:
            selected_items_cart.append(inv)
        
    def sell(self, items):
      return  

class Potions():
    def __init__(self,title, price, rarity, stats, stock):
        self.title = title
        self.price = price
        self.rarity = rarity
        self.stats = stats
        self.stock = stock
Heal = Potions()
Charm = Potions()
Luck = Potions()
Stength = Potions()



class Weapons:
    def __init__(self, title, price, rarity, stats, stock):
        self.title = title
        self.price = price
        self.rarity = rarity
        self.stats = stats
        self.stock = stock


Sword = Weapons()
Bow = Weapons()
OffhandShield = Weapons()
Dagger = Weapons()
Battleaxe = Weapons()
MajicStaff = Weapons()
Wand = Weapons()





class Armor():
    def __init__(self, title, price, rarity, stats, stock, weight):
        self.title = title
        self.price = price
        self.rarity = rarity
        self.stats = stats
        self.stock = stock
        self.weight = weight


# light uncommon armor
Helmet = Armor("Light_Uncommon_Helmet", 10, "uncommon", )
Chestplate = Armor("Light_Uncommon_Chestplate",)
Pants = Armor("Light_Uncommon_Pants",)
Boots = Armor("Light_Uncommon_Boots",)

# light epic armor
Helmet = Armor("Light_Epic_Helmet")
Chestplate = Armor("Light_Epic_Chestplate")
Pants = Armor("Light_Epic_Pants")
Boots = Armor("Light_Epic_Boots")

# light mythic armor
Helmet = Armor("Light_Mythic_Helmet")
Chestplate = Armor("Light_Mythic_Chestplate")
Pants = Armor("Light_Mythic_Pants")
Boots = Armor("Light_Mythic_Boots")

# medium uncommon armor
Helmet = Armor("Medium_Uncommon_Helmet")
Chestplate = Armor("Medium_Uncommon_Chestplate")
Pants = Armor("Medium_Uncommon_Pants")
Boots = Armor("Medium_Uncommon_Boots")

# medium epic armor
Helmet = Armor("Medium_Epic_Helmet")
Chestplate = Armor("Medium_Epic_Chestplate")
Pants = Armor("Medium_Epic_Pants")
Boots = Armor("Medium_Epic_Boots")

# medium mythic armor
Helmet = Armor("Medium_Mythic_Helmet")
Chestplate = Armor("Medium_Mythic_Chestplate")
Pants = Armor("Medium_Mythic_Pants")
Boots = Armor("Medium_Mythic_Boots")

# heavy uncommon armor
Helmet = Armor("Heavy_Uncommon_Helmet")
Chestplate = Armor("Heavy_Uncommon_Chestplate")
Pants = Armor("Heavy_Uncommon_Pants")
Boots = Armor("Heavy_Uncommon_Boots")

# heavy epic armor
Helmet = Armor("Heavy_Epic_Helmet")
Chestplate = Armor("Heavy_Epic_Chestplate")
Pants = Armor("Heavy_Epic_Pants")
Boots = Armor("Heavy_Epic_Boots")

# heavy mythic armor
Helmet = Armor("Heavy_Mythic_Helmet")
Chestplate = Armor("Heavy_Mythic_Chestplate")
Pants = Armor("Heavy_Mythic_Pants")
Boots = Armor("Heavy_Mythic_Boots")




