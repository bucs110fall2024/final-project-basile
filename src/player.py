class Player:
    def __init__(self, name="Player", coins= 20):
        self.name = name
        self.hand = []
        self.total = 0
        self.coins = 20  # Start with 20 coins

    def reset(self):
        self.hand = []
        self.total = 0

    def add_card(self, card):
        self.hand.append(card)
        self.total += card.get_value()

        # Handle Ace value adjustment
        if self.total > 21:
            for card in self.hand:
                if card.rank == "A" and card.get_value() == 11:
                    card.rank = 1
                    self.total -= 10
                    break

    def place_bet(self, bet_amount):
        if self.coins >= bet_amount:
            self.coins -= bet_amount
            return True
        return False

    def win_bet(self, bet_amount):
        self.coins += bet_amount

    def lose_bet(self, bet_amount):
        self.coins -= bet_amount
