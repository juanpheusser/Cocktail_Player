from Game.Card import Card
import random

class Deck:

    '''
    Represents a deck of cards
    '''

    RANKS = [str(n) for n in range(2, 11)] + list('JQKA')
    SUITS = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.SUITS
                       for rank in self.RANKS]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def shuffle_deck(self):
        random.shuffle(self._cards)

    def reorder_deck(self):
        self.__init__()

    def hand_out_cards(self, num_players):
        player_cards = {'player_' + str(i): [] for i in range(num_players)}
        amount_of_cards_per_player = self.__len__() // num_players
        self.shuffle_deck()

        for i in range(amount_of_cards_per_player):
            for k in range (num_players):
                player_cards['player_' + str(k)].append(self._cards.pop(0))
                self.shuffle_deck()

        return player_cards


deck = Deck()

players_cards = deck.hand_out_cards(4)

print(players_cards)



