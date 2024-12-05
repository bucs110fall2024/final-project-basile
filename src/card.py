class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.image = f"assets/{self.rank}_of_{self.suit}.png"

    def get_value(self):
        # If the card is face-down, don't return a value
        if self.rank == "None":
            return 0  # A face-down card doesn't contribute to the score
        
        # Handle numeric cards
        if self.rank.isdigit():
            return int(self.rank)

        # Handle face cards (J, Q, K)
        if self.rank in ["J", "Q", "K"]:
            return 10

        # Handle Aces
        if self.rank == "A":
            return 11  # Ace value can also be 1, but we use 11 for simplicity here

        # If we reach here, it's an invalid rank (shouldn't happen if used properly)
        return 0
