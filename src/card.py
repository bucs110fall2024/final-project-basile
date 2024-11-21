class CardB:
    def __init__(self, img_file,suit,number, name="" , worth= 0):
        """"
        Initializes a card object
        img_file : str - path to image file
        suit: str, contains the specific suit of the card
        number: int, the exact number that is read on the card
        name: string, f.e  "eight" or the queen card "queen"
        worth: int, the numerical value of a card
        """
        self.img_file = img_file
        self.number = number
        self.suit = suit
        self.name = name
        self.worth = worth
    def assign_value(self):
        """
        Assigns the playing value to each card
        Is necessary before any further action is taking by user
        When the card is an ace, it is up to the Player to choose the value
        """
        if self.name in ["queen", "king", "jack"]:
            self.worth = 10
        elif self.value == "ace":
            if True:
                self.worth = 11
            else:
                self.worth = 1
        else:
            self.worth = self.number