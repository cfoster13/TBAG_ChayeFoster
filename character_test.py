from character import Character

dave = Character("Dave", "A smelly zombie")
dave.describe()
dave.set_conversation("I'm going to bite you!")
dave.talk()

ben = Character("Ben", "A knight")
ben.talk() # Ben doesn't want to talk
ben.fight("sword")