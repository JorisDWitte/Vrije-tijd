import random

class Card:
    # most basic property: make a card, holds a rank and suit
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # String representation of a card (for displaying it to the user)
    def __str__(self):
        return f"{self.rank} of {self.suit}"    # define card properties like rank, suit, etc.

class Deck:
    # list of 52 cards: handle deck operations like shuffle, deal cards <= popped
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
        random.shuffle(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def reset(self):
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

class Player:
    # define player properties (hand, balance) and actions (bet, fold)
    def __init__(self, persoon_nmr):
        self.hand = []
        self.score = 0
        self.balance = 3
        self.id = persoon_nmr

    def receive_card(self, card):
        self.hand.append(card)

    def show_hand(self):
        return ', '.join(str(card) for card in self.hand)

    def string_hand(self): # need to be able to go from "King of Diamonds" to "KD"
        card_value1 = []
        card_type1 = []
        if not self.hand:
            return 0
        for stukje in self.hand:
            #val, typ = stukje.split(' of ')
            card_value1.append(stukje.rank)
            card_type1.append(stukje.suit)
        letter_to_number = {'Ace': 14, 'King': 13, 'Queen': 12, 'Jack': 11, 'Ten': 10}
        name_to_letter = {'Hearts': 'H', 'Diamonds': 'D', 'Clubs' : 'C', 'Spades': 'S'}
        card_value1 = list(map(int, [letter_to_number.get(letter, letter) for letter in card_value1]))
        card_type1 = list(map(str, [name_to_letter.get(letter, letter) for letter in card_type1]))
        card_value1.sort(reverse=True)
        return card_value1, card_type1

class Game:
    # makes deck, players
    # handle overall game flow
    def __init__(self, num_players=2):
        self.deck = Deck()  # Create a shuffled deck
        self.players = [Player(i) for i in range(num_players)]  # Initialize players: f"Player {i + 1}"
        self.pot = 0  # The total amount of money in the pot
        self.current_player = 0  # Start with the first player

    def start_game(self):
        print("Starting the Poker Game!\n")

        # Deal initial cards to players (2 cards each)
        for _ in range(5):
            for player in self.players:
                card = self.deck.deal_card()
                player.receive_card(card)
        print("The balance of the players:")
        [print(f"The player {player.id} has a balance of {player.balance}") for player in self.players]
        
        # Show hands for each player
        bet_pool = 0
        for player in self.players:
            print(f"Player's hand: {player.show_hand()}")  # f"{player.name}'s hand: {player.show_hand()}")
            bet = input(f"How much do you want to bet you will win this round? (must be an int>0) ")
            while -1 > int(bet) or int(bet) >= player.balance:
                bet = input(f"Insufficient funds, try again: ")
            player.balance -= int(bet)
            bet_pool += int(bet)

        for player in self.players:
            player.score = _score_result(player.string_hand())
        winner = max(self.players, key=lambda p: p.score)
        winner.balance += bet_pool
        print(f"Winnaar van deze ronde is: {winner.id}")

    def end_game(self):
        for player in self.players:
            print(player.id, player.balance)


# each hand goes to _score_result(), is scored with following functions
def _flush(card_type):
    if len(set(card_type)) == 1:
        return True
    else:
        return False

def _straight(card_val):
    if len(set(card_val)) == 5:
        if card_val[0] - card_val[4] == 4:
            return True
    return False

def _four_o_kind(card_val):
    if len(set(card_val)) == 2:
        if card_val[0] == card_val[3] or card_val[1] == card_val[4]:
            return True
    return False

def _three_o_kind(card_val):
    for ii in card_val:
        if card_val.count(ii) == 3:
            return True
    return False

def _pair_count(card_val):  # full house is 1 pair en 1 three
    pairs_of = []
    for i in card_val:
        if card_val.count(i) == 2:
            pairs_of.append(i)
    if not pairs_of:
        return []
    else:
        return pairs_of

def _score_result(playershand):
    card_val1 = playershand[0]
    card_typ1 = playershand[1]
    hand_1_has = []  # contains: score, with a ... and high card value
    flush_flag1 = _flush(card_typ1)
    straight_flag1 = _straight(card_val1)
    pairs_of = _pair_count(card_val1)
    if flush_flag1 and straight_flag1 and card_val1[5] == 10:
        hand_1_has.append(10)
        hand_1_has.append(card_val1[0])
        hand_1_has.append(card_val1[0])
    elif flush_flag1 and straight_flag1:
        hand_1_has.append(9)
        hand_1_has.append(card_val1[0])
        hand_1_has.append(1)  # suits
    elif _four_o_kind(card_val1):
        hand_1_has.append(8)
        if card_val1[0] == card_val1[3]:
            hand_1_has.append(card_val1[0])
            hand_1_has.append(card_val1[4])
        else:
            hand_1_has.append(card_val1[1])
            hand_1_has.append(card_val1[0])
    elif _three_o_kind(card_val1):
        if not pairs_of:  # geen paren, gewoon three o kind
                hand_1_has.append(4)
                hand_1_has.append(card_val1[2])
                card_val1 = list(filter((card_val1[2]).__ne__, card_val1))
                hand_1_has.append(card_val1[0])
        else:
            hand_1_has.append(7)
            hand_1_has.append(card_val1[2])
            card_val1 = list(filter((card_val1[2]).__ne__, card_val1))
            hand_1_has.append(card_val1[0])
    elif flush_flag1:
        hand_1_has.append(6)
        hand_1_has.append(card_val1[0])
        hand_1_has.append(1)  # suits
    elif straight_flag1:
        hand_1_has.append(5)
        hand_1_has.append(card_val1[0])
        hand_1_has.append(1)  # suits
    elif len(set(pairs_of)) == 2:
        hand_1_has.append(3)
        hand_1_has.append(pairs_of[1])
        hand_1_has.append(pairs_of[0])
    elif len(set(pairs_of)) == 1:
        hand_1_has.append(2)
        hand_1_has.append(pairs_of[0])
        hand_1_has.append(card_val1[0])
    else:
        hand_1_has.append(1)
        hand_1_has.append(card_val1[0])
        hand_1_has.append(card_val1[1])
    return hand_1_has

# create the game and start
if __name__ == "__main__":
    game = Game(2)
    game.start_game()
    game.end_game()
