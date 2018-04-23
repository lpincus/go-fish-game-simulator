"""
Use the knowledge you have gained to write a python simulation for the game of go fish. 
In go fish each person gets 5 cards with the remainder of the deck left as a draw pile or ‘pond’.  
At each turn one player asks another player if they have any cards of a given rank, such as 2, 10, King, Ace. 
If the opponent is holding such a card or many cards of the requested rank, regardless of the suit (diamonds, clubs, hearts, spades) they must give the card to the requestor. This is a ‘win’ for the requesting player, and they remove the cards from play. This increases the point count for the winning player’s score. If the requestor does not have a card they respond ‘go fish’ and the requestor must draw from the pond. Play continues until either all the cards are exhausted or there are no additional plays that can be made (e.g. each remaining card in play is of unique rank). 

Some considerations for your game:
-	Start simple - just two players, a single deck of cards, each person gets a turn in alternating fashion
-	Gradually get more complex 
    - move to three and up to 4 players, 
    - change the rules to let a win result in an additional turn for that player until they don’t get a win, 
    - choose randomly for the starting player.
-	Run the simulation many times (1000) and see if any one player wins more than the others.

"""
import go_fish
from itertools import permutations
import random

class Game:
    def __init__(self, number_of_players=4):
        # get players
        self.players = []
        self.losers = []
        for i in range(number_of_players):
            new_player = go_fish.Player("Player" + str(i))
            self.players.append(new_player)
        # randomize starting player 
        random.shuffle(self.players)
        # get deck and shuffle
        self.carddeck1 = go_fish.CardDeck()
        self.carddeck1.shuffle()

    def get_card_from_deck(self):
        try:
            card = self.carddeck1.give_card()
            return card
        except:
            self.game_over()
        
    def deal_cards(self):
        # deal 5 cards to each player
        for player in self.players:
            cards = self.carddeck1.give_n_cards(5)
            player.get_cards(cards)

    def deadly_duel(self, player1, player2):
        suit = player1.random_suit()
        cards_of_suit = player2.get_asked_for_cards(suit)
        if player2.out_of_cards():
            self.losers.append(player2)
            self.players.remove(player2)
        if len(cards_of_suit) > 0:
            player1.win_cards(cards_of_suit)
            return True
        # GO FISH
        if len(cards_of_suit) > 0:
            card = self.get_card_from_deck()
            player1.get_card(card)
        return False


    def play_game(self):
        # start game
        game_on = True
        self.deal_cards()
        while game_on:
            for player_combo in permutations(self.players, 2):
                # player1 asks
                player1 = player_combo[0]
                player2 = player_combo[1]
                if player1 in self.losers or player2 in self.losers:
                    continue

                win = True
                while win:
                    if player2 in self.players:
                        win = self.deadly_duel(player1, player2)
                    else:
                        win = False


            if len(self.players) < 2:
                game_on = False
        self.game_over()

    def game_over(self):
        pass
        # print("game_over")
        # print("winners, points, cards")
        # for winner in self.players:
        #     print(winner, winner.points, winner.cards.cards)
        # print("other players, points, cards")
        # for player in self.losers:
        #     print(player, player.points, player.cards.cards)
        # print("cards left")
        # print(self.carddeck1.cards)

    def get_winner(self):
        winner = go_fish.Player("zero points")
        for player in self.players:
            if player.points > winner.points:
                winner = player
        return winner
            


if __name__ == "__main__":
    # run simulation n times
    n = 1000
    winners = {}
    for i in range(n):
        print("new game", i)
        game = Game()
        game.play_game()
        winner = game.get_winner()
        try:
            winners[winner.name] += 1
        except:
            winners[winner.name] = 1
    print("SIMULATION OVER")
    print("player name, wins")
    for winner in winners:
        print(winner, winners[winner])