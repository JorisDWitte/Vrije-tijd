import pokergame

# nodig om v pokergame.py andere map te gebruiken: A is 11 en K,Q,J is 10, geeft meteen som van hele hand
def evaluate_bj(cards_val) -> int:
    card_val = []
    for i in cards_val:
        if i == 14:
            card_val.append(11)
        elif i > 10:
            card_val.append(10)
        else:
            card_val.append(i)
    return sum(card_val)


class BlackJackGame:
    # gebruik deck en player v poker.py
    # overall game game_of_bj runt per keer (als genoeg gelt en wilt) one_round_bj waar
    # gebruiker 1-4 spelers per ronde maakt om mee te spelen
    # in een ronde krijgt kaarten, dan host en wordt dan geevalueert
    def __init__(self):
        self.deck = pokergame.Deck()  # Create a shuffled deck
        self.host = pokergame.Player(99)
        self.players = []
        self.current_player = 0

    def game_of_bj(self):
        wants_to_play = True
        has_the_money = True
        while wants_to_play and has_the_money:
            bets = input(f"How many bets do you want to place? (1-4) ")
            self.players = [pokergame.Player(i) for i in range(int(bets))]
            self.deck.reset()
            self.deck.shuffle()
            self.host.hand = []
            self.one_round_bj()
            want_moreq = input(f"Do you want to play another round? (y/n) ")
            if not want_moreq == "y":
                wants_to_play = False

    def one_round_bj(self):
        for player in self.players:
            card = self.deck.deal_card()
            player.receive_card(card)
            card = self.deck.deal_card()
            player.receive_card(card)
        self.host.receive_card(self.deck.deal_card())
        for player in self.players:
            print(f"Player's hand: {player.show_hand()}")
        print(f"Host's hand: {self.host.show_hand()}")
        for player in self.players:
            want_new = True
            while want_new:
                bet = input(f"Do you want another card? (y/n) ")
                if bet == "y":
                    card = self.deck.deal_card()
                    player.receive_card(card)
                    print(f"Player's hand: {player.show_hand()}")
                else:
                    want_new = False
        self.host.receive_card(self.deck.deal_card())
        to_beat = evaluate_bj(self.host.string_hand()[0])
        while to_beat<16:
            self.host.receive_card(self.deck.deal_card())
            to_beat = evaluate_bj(self.host.string_hand()[0])
        print(f"Host's hand: {self.host.show_hand()}")
        if to_beat>21:
            to_beat=0
        for player in self.players:
            ev_bj = evaluate_bj(player.string_hand()[0])
            print(to_beat, ev_bj)
            if to_beat < ev_bj < 22:
                print("Yee, you won")
            else:
                print("You lost")


if __name__ == "__main__":
    game = BlackJackGame() #2)
    game.game_of_bj()
