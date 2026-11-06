# what do we do??

player = {"health": 100, "damage": 5, "mana": 50}
entity = ""
encounter = True

if encounter:
    choice = input(f"You have encountered an {entity}!\nWhat do you do? (1/2/3)\nAttack      Ability       Flee\n--> ")
    if choice  == "1":
        print("You chose to attack.")
    elif choice == "2":
        print("You chose to use your ability.")
    elif choice == "3":
        print("You chose to flee.")
    else:
        print("Invalid option.")

