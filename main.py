from room import Room
from character import Enemy
from character import Friendly
from player import Player
from item import Key

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")
storage_room = Room("Storage Room")

kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall.set_description("A large room with ornate golden decorations")
storage_room.set_description("A small storage room, that needs a key to be unlocked")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
storage_room.link_room(kitchen, "south")
kitchen.link_room(storage_room, "north")

zombie = Enemy("Zombie", "A scary loud bloodthirsty zombie")
zombie.set_conversation("Ugggghhhhh, aarrrughhhhh")
zombie.set_weakness("fire")
zombie.set_enemy_combat_item("axe")



max = Friendly("Max", "A nice man that seems willing to help")
max.set_conversation("Why are you wondering around here... there are scary monsters around")
friendly_item = max.set_friendly_item("sword")

dining_hall.set_character(zombie)
ballroom.set_character(max)

current_room = kitchen
player_has_enemy_item = False # Becomes true once player has successfully stolen an item from an enemy
player_has_key = False # Becomes true once player has stolen a key from a friendly enemy

storage_room_key = Key


player = Player("player1", 3) # Creating a player class for number of 3 lives

while True:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        if isinstance(inhabitant, Enemy):
            print("------------------")
            print("What will you do? ")
            print("Fight")
            print("Steal") 
            print("Talk")
            print("To move rooms enter: north, east, south, west")
        
        elif isinstance(inhabitant, Friendly):
            print("------------------")
            print("What will you do? ")
            print("Hug")
            print("Talk")
            print("Steal")
            print("To move rooms enter: north, east, south, west")

        
        
    
    command = input("> ")

    # Check if a direction was typed
    if command in {"north", "east", "south", "west"}:
        current_room = current_room.move(command)
        if current_room == storage_room and player_has_key == False:
            print("You need a key to access this room...")
            print("You remain in the kitchen...")
            current_room = kitchen
        elif current_room == storage_room and player_has_key == True:
            print("You use your key to open the door...")
            print("Well done, you have found the escape route.")
            exit()
    elif command == "talk":
        # add code
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There isn't anyone in this room.")
        #zombie.talk()
    elif command == "fight":
        if player_has_enemy_item == False and inhabitant is not None:
            fight_with = input("What would you like to fight with: ")
            inhabitant.fight(fight_with, player)
            if inhabitant.get_weakness != fight_with and player.get_player_lives() <= 0: # Losing all lives will cause game to end
                print("You have died, game over...")
                exit()
        elif inhabitant is not None:
            inhabitant.fight(enemy_weapon, player)
            current_room.set_character = None # deleting a character from a room 
            

    elif command == "steal":
        if isinstance(inhabitant, Enemy): #Checking if instance is Enemy
            print("Stealing...")
            enemy_weapon = inhabitant.steal(player) 
            player_has_enemy_item = True # player now has the enemy weapon = can now attack with this
            if player.get_player_lives() <= 0:
                print("You have died, game over...")
                exit()
        elif isinstance(inhabitant, Friendly):
            player_has_key = True
            print("You have obtained a key, which can open a locked door.")
        else:
            print("No enemy to steal from")

    elif command == "hug":
        if isinstance(inhabitant, Friendly): # checking for friendly character
            inhabitant.hug(friendly_item, player, zombie)
        else:
            print("No friendly person around to hug.")
    
    
    
    
    else:
        print("Not a valid input")

    # MAKE A RUN OPTION

    

