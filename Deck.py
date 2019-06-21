import random
import copy


class Deck:
    def __init__(self):
        self.suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        self.faceCards = ["Jack", "Queen", "King"]
        self.deck = {}
        self.cards = []
        self.card_id = [(i, card) for i, card in enumerate(self.cards)]
        self.m_initializeDeck()
        return

    def deal(self, num):
        '''
        Deal num many cards from the head of the cards list
        @param int num -> number of cards to remove
        @return -> list of strings containing dealt card
        '''
        dealt = self.cards[:num]
        self.cards = self.cards[num:]
        return dealt

    def m_initializeDeck(self):
        '''
        Initialize the hash table storing information on the cards. 

        The hash table keys are in the shape of "<Number/Name on card> of <suit>"
            eg. King of Hearts / 8 of Spades. 
            Note: suit is plural. 

        Values in the hash table are:
            'card_number': unique number of card in [1,52],
            'value': number -> value of card with face cards = 10 and Ace = 1,
            'number': string -> of the numerical face of the card including King, Queen, Jack, Ace,
            'suit': string ->suit of the card - plural   
        '''
        for j, suit in enumerate(self.suits):
            suffix = " of " + suit
            for i in range(1, 14):
                if i == 1:
                    self.deck["Ace" + suffix] = {
                        'card_number': i-1 + j*13,
                        'value': 1,
                        'number': "Ace",
                        'suit': suit
                    }

                    self.cards.append("Ace" + suffix)
                elif i < 11:
                    self.deck[f'{i}' + suffix] = {
                        'card_number': i-1 + j * 13,
                        'value': i,
                        'number': f"{i}",
                        'suit': suit
                    }

                    self.cards.append(f'{i}' + suffix)
                else:
                    self.deck[self.faceCards[i-11] + suffix] = {
                        'card_number': i-1 + j*13,
                        'value': 10,
                        'number': self.faceCards[i-11],
                        'suit': suit
                    }

                    self.cards.append(self.faceCards[i-11] + suffix)
        return

    def reset(self, shuffle=True):
        '''
        Resets the cards list to full
        @param boolean shuffle -> shuffles the list default:True 
        '''
        self.cards = copy.deepcopy(list(self.deck.keys()))
        if shuffle:
            self.shuffle()
        return

    def shuffle(self):
        '''
        Randomizes the cards list
        '''
        random.shuffle(self.cards)
        return
