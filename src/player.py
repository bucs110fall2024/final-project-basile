class Player:
    def __init__(self, name="Player", coins= 20):
        """
        Initializes a Player object: name: string hand: list total:int coins: int
        """
        self.name = name
        self.hand = []
        self.total = 0
        self.coins = 20  # Start with 20 coins

    def reset(self):
        # Restes the Players hand and total for the next game
        self.hand = []
        self.total = 0

    def add_card(self, card):
        #Adds a card to the Players hand
        self.hand.append(card)
        self.total += card.get_value()

        # Handle Ace value adjustment
        if self.total > 21:
            for card in self.hand:
                if card.rank == "A" and card.get_value() == 11:
                    card.rank = 1
                    self.total -= 10
                    break

   
