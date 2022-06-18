import random


class Card:
    """A card that can have a value between 1-13
    
    The responsibility of Card is to have a value between 1-13 and show it 
   
    Attributes:
        value (int): The value of the card between 1-13
    """

    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0

    def card_value(self):
        """Gives the card a value between 1 and 13, and returns that card.
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1, 13)
        return self.value