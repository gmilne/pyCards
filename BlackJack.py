from Deck import Deck


class BlackJack:
    def __init__(self):
        self.table = {'Dealer': {'hand': [], 'bet': 0}}
        self.dealer = 0
        self.deck = Deck()
        self.deck.shuffle()
        self.faceup_dealer = False
        self.currentPlayer = ""
        self.playOrder = []
        self.playing = False

    def add_player(self, name):
        '''
        Add a player to the table
        @param string -> name key in table hashtable
        '''
        self.table[name] = {'hand': [], 'bet': 0}
        self.currentPlayer = name
        return

    def add_players(self, names):
        '''
        Add a list of players to the table
        @param list of strings -> names to be key in table hashtable
        '''
        [self.add_player(name) for name in names]
        return

    def deal(self):
        '''
        Deal cards to players with dealer last. Consists of two loops to simulate the dealing of actual cards.
        '''
        self.playing = True
        for _, player in list(self.table.items())[::-1]:
            player['hand'].append(self.deck.deal(1)[0])
        for _, player in self.table.items():
            player['hand'].append(self.deck.deal(1)[0])

    def getNextPlayer(self):
        '''
        Pop the next player off the play order stack, update the currentPlayer to next player
        @return string -> next player
        '''
        player = self.playOrder[0]
        if len(self.playOrder) > 1:
            self.playOrder = self.playOrder[1:]
        else:
            self.playOrder = []
        self.currentPlayer = player
        return player

    def hit(self):
        '''
        Add a card to the current players hand. If the sum of the hand 
        is over 21 player automatically busts and calls stay()
        '''
        self.table[self.currentPlayer]['hand'].append(self.deck.deal(1)[0])
        if self.sum_hand(self.table[self.currentPlayer]['hand'][1:]) > 21:
            # print(f'{self.currentPlayer} Bust')
            self.stay()

    def resetGame(self):
        """
        Reset hands and bets for all current players
        """
        for key in self.table.keys():
            self.table[key] = {'hand': [], 'bet': 0}
        return

    def start(self):
        """
        Initialize the play order and deal cards
        """
        if not self.playing:
            self.deck.reset()
            self.resetGame()
            self.deal()
            self.playing = True
            self.playOrder = list(self.table.keys())[::-1]
            self.getNextPlayer()
        else:
            print("Game in progress")

        return

    def stay(self):
        '''
        Change current player to next player in the order, if Dealer end round
        '''

        if len(self.playOrder) == 0:
            self.playing = False
        else:
            self.getNextPlayer()

        return

    def show_dealer(self):
        self.faceup_dealer = True
        return

    def show_table(self):
        '''
        Print the player and theirs hands to show the state of the table
        '''
        for key, player in self.table.items():
            print(f'{key}:  \n')
            if key == 'Dealer' and self.faceup_dealer:
                [print(card) for card in player['hand']]
            elif key == 'Dealer':
                print("#### ######")
                print(self.table[key]['hand'][1])
            else:
                [print(card) for card in player['hand']]

            print("------")
        return

    def sum_hand(self, hand):
        """
        Sum the cards in a given hand
        @param list ->  list of strings representing cards
        @return number -> numerical value of the hand
        """
        total = 0
        for card in hand:
            if "Ace" in card:
                if total + 11 > 21:
                    total += 1
                else:
                    total += 11
            total += self.deck.deck[card]['value']
        return total
