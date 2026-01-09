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
    def items(self, Heal, Charm, Luck, Stength):
        return


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
    def __init__(self, title, price, rarity, stats, stock):
        self.title = title
        self.price = price
        self.rarity = rarity
        self.stats = stats
        self.stock = stock
