from Game.Card import Card


class Vasa:
    def __init__(self):
        self._cards = []

    def add_cards_to_vasa(self, cards):
        '''
        Adds cards to vasa after they have been played by each player
        :param cards: list of cards
        :type cards: list
        :return: None
        :rtype: None
        '''
        self._cards.extend(cards)