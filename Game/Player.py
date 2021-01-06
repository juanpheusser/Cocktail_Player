from Game.Hand import Hand

class Player:
    def __init__(self, player_number):
        self.player_number = player_number
        self.player_score = 0
        self.hand = Hand()

    
