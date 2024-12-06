class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.image = f"assets/{self.rank}_of_{self.suit}.png"

    def get_value(self):
        # Returns the Value of the Card that was passed
        if self.rank == "None":
            return 0  
        
        # For cards 2-10
        if self.rank.isdigit():
            return int(self.rank)

        #  face cards (J, Q, K)
        if self.rank in ["J", "Q", "K"]:
            return 10

        # Handle Aces
        if self.rank == "A":
            return 11  # Ace value can also be 1, but we use 11 for simplicity here

        
        return 0
