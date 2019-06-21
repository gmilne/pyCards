import random
import copy


class Deck:
    def __init__(self):
        self.suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        self.faceCards = ["Jack", "Queen", "King"]
        self.deck = {}
        self.cards = []
        for j, suit in enumerate(self.suits):
            suffix = " of " + suit
            for i in range(1, 14):
                if i == 1:
                    self.deck["Ace" + suffix] = {'card_number': i-1 + j*13,
                                                 'value': 1,
                                                 'number': "Ace",
                                                 'suit': suit}
                    self.cards.append("Ace" + suffix)
                elif i < 11:
                    self.deck[f'{i}' + suffix] = {'card_number': i-1 + j * 13,
                                                  'value': i,
                                                  'number': f"{i}",
                                                  'suit': suit}
                    self.cards.append(f'{i}' + suffix)
                else:
                    self.deck[self.faceCards[i-11] + suffix] = {'card_number': i-1 + j*13,
                                                                'value': 10,
                                                                'number': self.faceCards[i-11],
                                                                'suit': suit}
                    self.cards.append(self.faceCards[i-11] + suffix)
        self.card_id = [(i, card) for i, card in enumerate(self.cards)]

    def shuffle(self):
        random.shuffle(self.cards)
        return

    def deal(self, num):
        dealt = self.cards[:num]
        self.cards = self.cards[num:]
        return dealt

    def reset(self):
        # self.cards = copy.deepcopy(list(self.deck.values()))
        self.shuffle()
        return
