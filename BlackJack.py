from Deck import Deck


class BlackJack:
    def __init__(self):
        self.table = [["Dealer"]]
        self.dealer = 0
        self.cards = Deck()
        self.cards.shuffle()
        self.faceup_dealer = False
        self.currentPlayer = 0
        self.playing = False

    def add_player(self, name):
        self.table.append([name])
        self.currentPlayer += 1
        return

    def add_players(self, names):
        [self.add_player(name) for name in names]
        return

    def show_table(self):
        print('\t'*len(self.table) + self.table[0][0])
        if len(self.table[0]) > 1:
            if not self.faceup_dealer:
                print('\t'*len(self.table) +
                      '#### ####  ' + self.table[0][1])
            else:
                print('\t'*len(self.table) +
                      self.table[0][1] + ', ' + self.table[0][2])

        print("")
        print("")

        # Print Names
        for i, hand in enumerate(self.table[1:]):
            if i == 0:
                print(hand[0], end='')
            else:
                print('\t'*5 + hand[0], end='')
        print("")

        # Print Cards
        for i, hand in enumerate(self.table[1:]):
            if i == 0:
                [print(card + '| ', end='') for card in hand[1:]]
            else:
                print('\t\t', end='')
                [print(card + '| ', end='') for card in hand[1:]]
        print("")
        print("-"*75)

    def deal(self):
        self.playing = True
        for player in self.table:
            player.append(self.cards.deal(1)[0])
        for player in self.table:
            player.append(self.cards.deal(1)[0])

    def hit(self):
        self.table[self.currentPlayer].append(self.cards.deal(1)[0])
        if self.sum_hand(self.table[self.currentPlayer][1:]) > 21:
            self.stay()

    def stay(self):
        self.currentPlayer -= 1
        if self.currentPlayer == -1:
            self.playing = False
            self.currentPlayer = len(self.table) - 1
        elif self.currentPlayer == 0:
            self.show_dealer()
            # self.show_table()
        return

    def show_dealer(self):
        self.faceup_dealer = True
        return

    def sum_hand(self, hand):
        total = 0
        for card in hand:
            total += self.cards.deck[card]['value']
        return total


bj = BlackJack()
bj.add_players(["A"])
bj.deal()
for i in range(4):
    bj.hit()
    print(bj.table[bj.currentPlayer][0], bj.sum_hand(
        bj.table[bj.currentPlayer][1:]))
    if not bj.playing:
        break
# bj.show_table()
