from Deck import Deck


class ThreeCardPoker:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.deck = Deck()
        self.playerHand = []
        self.dealerHand = []
        self.winner = ''

    def play(self):
        self.winner = ''
        self.deck.reset()
        self.deck.shuffle()
        self.playerHand = []
        self.dealerHand = []
        self.playerHand = self.deck.deal(3)
        self.dealerHand = self.deck.deal(3)
        print(f"$Dealer hand: {self.dealerHand}")
        print(f"Player hand: {self.playerHand}")
        if self.playerHand == None:
            print("Failure to deal player hand")
        else:
            self.compare_hands()
        return

    def compare_hands(self):
        dealerValue = self.find_highest_value(self.dealerHand)
        playerValue = self.find_highest_value(self.playerHand)

        if dealerValue < playerValue:
            self.winner = 'dealer'
        elif playerValue < dealerValue:
            self.winner = 'player'
        elif playerValue == dealerValue:
            if playerValue < 2:
                self.high_rank_compare()
            elif playerValue < 4:
                self.set_compare()
            else:
                self.high_card_compare()
        return

    def find_highest_value(self, hand):
        if self.flush_check(hand) and self.straight_check(hand):
            return 0
        if self.triple_check(hand):
            return 1
        if self.flush_check(hand):
            return 2
        if self.straight_check(hand):
            return 3
        if self.pair_check(hand):
            return 4
        return 5

    def pair_check(self, hand):
        return len(set([self.deck.deck[card]['number'] for card in hand])) == 2

    def set_compare(self):
        playerIndexes = self.find_number_matches(self.playerHand)
        dealerIndexes = self.find_number_matches(self.dealerHand)
        playerValue = self.scale_card(self.playerHand[playerIndexes[0]])
        dealerValue = self.scale_card(self.dealerHand[dealerIndexes[0]])
        if playerValue > dealerValue:
            self.winner = 'player'
        elif dealerValue > playerValue:
            self.winner = 'dealer'
        else:
            self.winner = 'push'
        return

    def triple_check(self, hand):
        return len(set([self.deck.deck[card]['number'] for card in hand])) == 1

    def find_number_matches(self, hand):
        cardNumbers = [self.deck.deck[card]['number'] for card in hand]
        matches = {}
        for i, value in enumerate(cardNumbers):
            if value in matches:
                matches[value].append(i)
            else:
                matches[value] = [i]
        for indexes in matches.values():
            if len(indexes) > 1:
                return indexes
        return []

    def flush_check(self, hand):
        cardSuits = [self.deck.deck[card]['suit'] for card in hand]
        return len(set(cardSuits)) == 1

    def straight_check(self, hand):
        cardValues = [self.scale_card(card) for card in hand]
        cardValues.sort()
        for i, value in enumerate(cardValues[1:]):
            if value != cardValues[i] + 1:
                return False
        return True

    def high_rank_compare(self):
        playerHighCard = max([self.scale_card(card)
                              for card in self.playerHand])
        dealerHighCard = max([self.scale_card(card)
                              for card in self.dealerHand])

        if playerHighCard > dealerHighCard:
            self.winner = 'player'
        elif dealerHighCard > playerHighCard:
            self.winner = 'dealer'
        else:
            self.winner = 'push'
        return

    def high_card(self, hand):
        cardValues = [self.scale_card(card) for card in hand]
        return hand[cardValues.index(max(cardValues))]

    def high_card_compare(self):
        playerCards = sorted([self.scale_card(card)
                              for card in self.playerHand])
        dealerCards = sorted([self.scale_card(card)
                              for card in self.dealerHand])

        for i, card in enumerate(playerCards):
            if card > dealerCards[i]:
                self.winner = 'player'
                return
            elif card < dealerCards[i]:
                self.winner = 'dealer'
                return

        self.winner = 'push'
        return

    def scale_card(self, card):
        scaledCard = (self.deck.deck[card]['card_number'] + 1) % 13
        if scaledCard == 0:
            scaledCard = 13
        if scaledCard == 1:
            scaledCard = 14
        return scaledCard

    def print_hands(self):
        print('Player: ', self.playerHand)
        print('Dealer: ', self.dealerHand)
        return
