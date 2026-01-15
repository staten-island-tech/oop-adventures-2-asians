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
        user_class = input(f"What class do you want to be {user}?   (mage, tank, healer, warrior): ").lower()
        if user_class not in ["mage", "tank" , "healer", "warrior"]:
            user_class=input("Invalid action. Please choose a correct class.").lower()
            if input == "mage":
                print(f"Congrats, {user} your are a mage")
            elif input == "tank":
                print(f"Congrats, {user} your are a tank")
            elif input == "healer":
                print(f"Congrats, {user} your are a healer")
            elif input == "warrior":
                print(f"Congrats, {user} your are a warrior")
        game = False


enter_game()

