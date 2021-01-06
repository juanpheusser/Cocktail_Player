from Game.Card import Card

class Pit:

    '''
    It is the Card pit after they have been used
    '''

    def __init__(self):
        self._cards = []

    def add_cards_to_pit(self, cards):
        '''
        Adds cards to pit after they have been used in game
        :param cards: list of cards
        :type cards: list
        :return: None
        :rtype: None
        '''
        self._cards.extend(cards)

