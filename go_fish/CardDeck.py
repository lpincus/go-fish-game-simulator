"""
Use the knowledge you have gained to write a python simulation for the game of go fish. 
In go fish each person gets 5 cards with the remainder of the deck left as a draw pile or ‘pond’.  
At each turn one player asks another player if they have any cards of a given rank, such as 2, 10, King, Ace. 
If the opponent is holding such a card or many cards of the requested rank, regardless of the suit (diamonds, clubs, hearts, spades) they must give the card to the requestor. This is a ‘win’ for the requesting player, and they remove the cards from play. 
This increases the point count for the winning player’s score. If the requestor does not have a card they respond ‘go fish’ and the requestor must draw from the pond. Play continues until either all the cards are exhausted or there are no additional plays that can be made (e.g. each remaining card in play is of unique rank). 

Some considerations for your game:
-	Start simple - just two players, a single deck of cards, each person gets a turn in alternating fashion
-	Gradually get more complex - move to three and up to 4 players, change the rules to let a win result in an additional turn for that player until they don’t get a win, choose randomly for the starting player.
-	Run the simulation many times (1000) and see if any one player wins more than the others.

"""
import random


class CardDeck:
    def __init__(self):
        self.nos = "A 2 3 4 5 6 7 8 9 10 J Q K".split(" ")
        self.suits = ['spades', 'diamonds','clubs','hearts']
        self.cards = self.get_card_deck()
    
    def __len__(self):
        return len(self.cards)

    def append(self, card):
        self.cards.append(card)

    def get_card_deck(self):
        cards = []
        for i in self.nos:
            for j in self.suits:
                cards.append(i + ' ' + j)
        return cards

    def give_card(self):
        """ gives single card or throws error """
        if len(self.cards) > 0:
            card = self.cards.pop()
            return card
        else:
            raise Exception("Error. No Cards in Deck.")
    
    def give_n_cards(self, n):
        """ gives n cards """
        cards = []
        for i in range(n):
            cards.append(self.give_card())
        return cards
    
    def shuffle(self):
        random.shuffle(self.cards)

    def get_deck(self, cards):
        self.cards = cards

    def add_card(self, card):
        self.cards.append(card)
    
    def add_cards(self, cards):
        self.cards = self.cards + cards

    def get_cards_of_rank(self, rank):
        cards_of_rank = []
        for card in set(self.cards):
            try:
                if rank in card:
                    cards_of_rank.append(card)
            except:
                print("error")
            
        return cards_of_rank

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)

    def remove_cards(self, cards):
        for card in cards:
            self.remove_card(card)

    def random_suit(self):
        suits = list(self.suits)
        random.shuffle(suits)
        random_suit = suits.pop()
        return random_suit
    
