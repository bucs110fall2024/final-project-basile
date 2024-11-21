class Currency:
    def __init__(self, total, img_file, color,x,y):
        """
        Initializes a Currency object
        total: int, the total amount of currency that the player has
        img_file: str - path to file image
        color: str - color of the currency
        x: int - x coordinate of the currency display
        y: int - y coordinate of the currency display
        """
        self.total = total
        self.img_file = img_file
        self.color = color
        self.x = x
        self.y = y
    def checkFunds(self, bet_amount):
        """
        Checks the Players total amount of money to see if they have enough money to make a bet
        bet_amount: int - The desired bet the Player wants to make
        """
        if self.total >= bet_amount:
            return True
        else:
            return False
    def addFunds(self,amount):
        """
        Adds funds into the Players account
        amount: int - the amount being added to the total variable
        """
        self.total += amount
            