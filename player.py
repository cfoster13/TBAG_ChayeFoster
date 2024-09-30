class Player():
    def __init__(self, name, player_lives = 3):
        self.name = name
        self.player_lives = player_lives

    def set_player_lives(self, player_lives):
        self.player_lives = player_lives

    def get_player_lives(self):
        return self.player_lives