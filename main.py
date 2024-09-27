from room import Room
from character import Enemy

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")

kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall.set_description("A large room with ornate golden decorations")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

zombie = Enemy("Zombie", "A scary loud bloodthirsty zombie")
zombie.set_conversation("Ugggghhhhh, aarrrughhhhh")
zombie.set_weakness("fire")

dining_hall.set_character(zombie)

current_room = kitchen

while True:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()


    command = input("> ")
    current_room = current_room.move(command)

