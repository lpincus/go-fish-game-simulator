"""
Use the knowledge you have gained to write a python simulation for the game of go fish. 
In go fish each person gets 5 cards with the remainder of the deck left as a draw pile or ‘pond’.  
At each turn one player asks another player if they have any cards of a given rank, such as 2, 10, King, Ace. 
If the opponent is holding such a card or many cards of the requested rank, regardless of the suit (diamonds, clubs, hearts, spades) they must give the card to the requestor. 
This is a ‘win’ for the requesting player, and they remove the cards from play. This increases the point count for the winning player’s score. 
If the requestor does not have a card they respond ‘go fish’ and the requestor must draw from the pond. 
Play continues until either all the cards are exhausted or there are no additional plays that can be made (e.g. each remaining card in play is of unique rank). 

Some considerations for your game:
-	Start simple - just two players, a single deck of cards, each person gets a turn in alternating fashion
-	Gradually get more complex - move to three and up to 4 players, change the rules to let a win result in an additional turn for that player until they don’t get a win, choose randomly for the starting player.
-	Run the simulation many times (1000) and see if any one player wins more than the others.

"""
from go_fish.CardDeck import CardDeck

class Player:
    """
    Player of go-fish, can
    - get 5 cards
    - ask other player for card of given rank
    - get asked for card of given rank & give card of given rank (or say go fish)
    - get card of given rank
    """
    def __init__(self, name):
        self.name = name
        self.cards = CardDeck()
        self.cards.get_deck([])
        self.points = 0
    
    def __str__(self):
        return self.name

    def get_card(self, card):
        if type(card) is None:
            raise Exception("asdf")
        self.cards.append(card)
    
    def get_cards(self, cards):
        for card in cards:
            self.get_card(card)

    def win_cards(self, cards):
        for card in cards:
            # print("player", self, "won cards", cards)
            self.points = self.points + 1
    
    def get_asked_for_cards(self, rank):
        cards_of_rank = self.cards.get_cards_of_rank(rank)
        self.cards.remove_cards(cards_of_rank)
        return cards_of_rank
    
    def random_suit(self):
        random_suit = self.cards.random_suit()
        return random_suit

    def out_of_cards(self):
        return not self.has_cards()

    def has_cards(self):
        if len(self.cards) > 0:
            return True
        return False
    
