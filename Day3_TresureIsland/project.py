print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
      ''')

print("Welcome to Treasure Island. \nYour mission is to find the treasure.")
print("You're at cross road. Where do you want to go?")
decision = input ("Type -left- or -right-\n")
if decision == "left":
    print("You've come to a lake. There is an island in the middle of the lake")
    decision = input("Type -wait- to wait for a boat. Type -swim- to swim across.\n")
    if decision == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors")
        decision = input("One red, one yellow, one blue. Which colour ypu choose\n")
        if decision == "red":
            print("Burned by fire. Game Over!")
        if decision == "blue":
            print("Eaten by beast. Game Over!")
        if decision == "yellow":
            print("You win!")
        else:
            print("Game Over!")
    else: 
        print("Attacked by trout. Game Over!")
else:
    print("Fall into a hole. Game Over!")