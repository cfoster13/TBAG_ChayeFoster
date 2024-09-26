from room import Room

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")

kitchen.set_description("A dank and dirty room buzzing with flies")

print(kitchen.get_description())