from MC import *
from E import *
from inventory import *
def enter_game():
    game = True
    while game == True:
        user = input("What is your name?").strip()
        if user == (""):
            print("that is not a name idiot")
            user = input("enter a name again:")
        user_class = input(f"What class do you want to be {user}?   (mage, tank, healer): ").lower()
        if user_class not in ["mage", "tank" , "healer"]:
            user_class=input("Invalid action. Please choose a correct class.").lower()
        game = False
    

enter_game()

