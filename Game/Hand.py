from Game.Card import Card


class Hand:
    def __init__(self):
        self._cards = []

    def receive_handout_of_cards(self, cards):
        '''
        Adds cards to Hand after handout
        :param cards: list of cards
        :type cards: list
        :return: None
        :rtype: None
        '''
        self._cards.extend(cards)

    def __getitem__(self, position):
        return self._cards[position]

    def play_card(self, card_position_in_hand):
        return self._cards[card_position_in_hand]

    def show_cards_in_hand(self):
        print(self._cards)