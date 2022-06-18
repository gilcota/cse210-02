from game.card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card: A card with a value between 1-13.
        prev_card: The last card played.
        is_playing (boolean): Whether or not the game is being played.
        hilo: Wether the player predicts the next card to be higher or lower than the actual displayed.
        total_score (int): The score for the entire game, starts with 300.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = Card()
        self.prev_card = 0
        self.is_playing = True
        self.hilo = ""
        self.total_score = 300

        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.prev_card = self.card.value
            self.show_card()
            self.choose_hilo()
            self.calculate_score()
            self.show_results()

    def show_card(self):
        """Takes the initial card and shows it with its value.
        
        Args:
           self (Director): an instance of Director. 
        """

        if self.prev_card == 0:
            self.prev_card = self.card.card_value()
            print(f"\nThe card is: {self.card.value}")
        else:
            print(f"\nThe card is: {self.prev_card}")

    def choose_hilo(self):
        """Asks the player to guess if next card will be higher or lower than the previously shown.
        
        Args:
           self (Director): an instance of Director. 
        """

        self.hilo = input("Higher or lower? [h/l] ")

    def calculate_score(self):
        """Compares previous card with new card and depending on the previous hilo guess from the player, gives 100 points if guessed and subtracts 75 points if not
        and sums/deducts from actual score.
        
        Args:
           self (Director): an instance of Director. 
        """

        while self.prev_card == self.card.value:
            self.card.card_value()

        if self.hilo == "h":
            if self.card.value > self.prev_card:
                self.total_score += 100
            else:
                self.total_score -= 75
        
        if self.hilo == "l":
            if self.card.value < self.prev_card:
                self.total_score += 100
            else:
                self.total_score -= 75
    
    def show_results(self):
        """Shows next card and the score due to player's guess; if it is over 0, asks to the player if he/she wants to play again.
        
        Args:
           self (Director): an instance of Director. 
        """

        print(f"Next card was: {self.card.value}")
        if self.total_score <= 0:
            print(f"Your score is: 0")
            self.is_playing = False
        else:
            print(f"Your score is: {self.total_score}")
            new_card = input("Play again? [y/n] ")
            self.is_playing = (new_card == "y")


        
    
        
