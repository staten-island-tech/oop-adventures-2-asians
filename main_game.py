from MC import *
from E import *
from inventory import *
def enter_game():
    game = True
    while game:
        user = input("What is your name? ").strip()
        if user == "":
            print("That is not a name, idiot.")
            user = input("Enter a name again: ")
        
        user_class = input(f"What class do you want to be, {user}? (mage, tank, healer, warrior): ").lower()
        
        while user_class not in ["mage", "tank", "healer", "warrior"]:
            user_class = input("Invalid action. Please choose a correct class: ").lower()
        
        if user_class == "mage":
            print(f"Congrats, {user}, you are a mage!")
        elif user_class == "tank":
            print(f"Congrats, {user}, you are a tank!")
        elif user_class == "healer":
            print(f"Congrats, {user}, you are a healer!")
        elif user_class == "warrior":
            print(f"Congrats, {user}, you are a warrior!")
        
        game = False
enter_game()
