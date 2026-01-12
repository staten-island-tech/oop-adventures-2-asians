import random

ran = random.randint(1, 10)


user_input = []

guess_history= []

while user_input != ran:
    guess_history.append(user_input)
    user_input = int(input("Please guess the random number selected from 1 to 10: "))
    if user_input < ran:
        print("Wrong number! Try again. Your number is less than the correct number.")
    elif user_input > ran:
        print ("Wrong number Try again. Your number is greater than the correct number.")



print("Thank you for guessing the correct number!")
print (f"Your guess history is below: {guess_history}")
