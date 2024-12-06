class Dealer:
    def __init__(self):
        """
        Initializes a Dealer object. 
        Hand: list - List of cards the dealer holds
        Total: int - total value of the dealers hand
        """
        self.hand = []  
        self.total = 0  
    
    def add_card(self, card):
        #Add a card to the dealer's hand and update total.
        self.hand.append(card)
        self.total = self.calculate_total()

    def calculate_total(self):
        #Calculate the total value of the dealer's hand.
        total = 0
        aces = 0  # Keep track of aces because they can be worth 1 or 11

        for card in self.hand:
            if card is None:
                continue
            if card.rank in ['J', 'Q', 'K']:
                total += 10
            elif card.rank == 'A':
                aces += 1
                total += 11
            else:
                total += int(card.rank)
        
        # Adjust for aces: if the total is over 21, make aces worth 1 instead of 11
        while total > 21 and aces:
            total -= 10
            aces -= 1

        return total

    def reset(self):
        """Reset the dealer's hand for a new round."""
        self.hand = []
        self.total = 0
    
    def update_total(self):
        
        self.total = sum(card.get_value() for card in self.hand)  