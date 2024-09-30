import random
from player import Player

class Character():
    # Creating a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.enemy_combat_item = None

    # Describe the character
    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    # Set what this character will say when talked to

    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")
    
    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")

        return True
    
class Enemy(Character):
    def __init__(self, char_name, char_description): #identical to constructor for superclass
        super().__init__(char_name, char_description) # To make an enemy make a character first and then customise it
        self.weakness = None
    # Adding weaknesses to the enemy
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness
    
    def get_weakness(self):
        return self.weakness
    
    
        
    def set_enemy_combat_item(self, enemy_combat_item):
        self.enemy_combat_item = enemy_combat_item

    def get_enemy_combat_item(self, enemy_combat_item):
        return self.enemy_combat_item
        
    def steal(self, player):
        rand_steal_chance = random.randint(1, 100)
        if rand_steal_chance >= 5: # chance of stealing
            print(f"You successfully stole, {self.enemy_combat_item}")
            self.set_weakness(self.enemy_combat_item) # Changing weakness to enemy weapon so player can defeat enemy
            return self.enemy_combat_item
        
        elif self.enemy_combat_item is None:
            print(f"{self.name} doesn't have a combat weapon")
            return None
        else:
            # After a failed attempt player loses a live
            player.set_player_lives(player.get_player_lives() - 1)
            print(f"{self.name} prevented you from stealing, and attacks you in return")
            print(f"You now have {Player.get_player_lives(player)} remaining")

    #Overriding the previous fight method
    def fight(self, combat_item, player):
        if combat_item == self.weakness:
            print(f"You fend {self.name} off with the {combat_item}") #Delete enemy from the room
            return True
        else:
            if player.get_player_lives() > 0: # Check player lives
                player.set_player_lives(player.get_player_lives() - 1)
                print(f"{self.name} attacks you, {Player.get_player_lives(player)} lives remaining")
                return True
            else:
                print(f"{self.name} crushes you, puny adventurer") #ELIF STATEMENT IF HEARTS IS MORE THAN 0 TAKE A HEART, OTHERWISE GAME OVER
                return False
