from character import Enemy

zombie = Enemy("Zombie", "A scary loud bloodthirsty zombie")
zombie.set_weakness("fire")

fight_with = input("What will you fight with: ")
zombie.fight(fight_with)