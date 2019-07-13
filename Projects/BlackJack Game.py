import random

'''Represents the standard playing deck of 52 cards'''
rank_list = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King','Ace']
color_list = ['Hearts', 'Diamonds', 'Clubs', 'Spade']
value_list = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

game_on = True

class Card:

    def __init__(self, color, rank):
        self.color = color
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.color

class Deck:
    def __init__(self):
        self.deck_list = []
        for color in color_list:
            for rank in rank_list:
                self.deck_list.append(Card(color, rank))

    def __str__(self):
        deck = ''
        for card in self.deck_list:
            deck += '\n' + card.__str__()
        return 'Deck has following cards: ' + deck

    def shuffle(self):
        '''shuffle method for shuffling the deck_list'''
        random.shuffle(self.deck_list)

    def deal(self):
        '''deal method for grabbing a card from the deck_list'''
        return self.deck_list.pop()

class Hand():
    '''A hand class with methods for adding cards and to adjust the ace value'''
    def __init__(self):
        self.cards_in_hand = []
        self.value = 0
        self.ace = 0

    def add_card(self, card):
        '''add cards to cards_in_hand'''
        self.cards_in_hand.append(card)
        self.value += value_list[card.rank]
        #ace track
        if card.rank == 'Ace':
            self.ace += 1

    def adjust_for_ace(self):
        ''' While value is greater than 21, and have an ace, subtract 10 from that and reduce ace by the value of 1'''
        while self.value > 21 and self.ace > 0:
            self.value -= 10
            self.ace -= 1

class Chips():
    ''' A Class with methods for keeping track of chips that player have, adding or subtracting from the total amount of chips'''
    def __init__(self):
        self.total_chips = 100
        self.bet = 0

    def win_bet(self):
       ''' If a player wins a bet, add that amount to the total chips'''
       self.total_chips += self.bet

    def lose_bet(self):
        ''' If a player lose a bet, subtract that amount from the total chips'''
        self.total_chips -= self.bet

def make_bet(chips):
    '''method for making a bet in game'''
    while True:
        try:
            chips.bet = int(input('Please make a bet'))
        except:
            print('Sorry but give me an integer')
        else:
            if chips.bet > chips.total_chips:
                print('Please place another ber that is not greater than ', chips.total_chips)
            else:
                break

def hit(deck, hand):
    '''a method for getting another card'''
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    '''Asking player to get a card or stand back if he had enough'''
    global game_on
    while game_on:
        card_hit = input('Would you like a card, press y for Yes ')
        if card_hit == 'y'.lower():
            hit(deck, hand)
        elif card_hit != 'y':
            print('Player has enough cards, dealer plays now')
            game_on = False
        else:
            print('Please provide a proper answer')

def show_some_cards(player, dealer):
    '''A function to show all the player cards and dealer cards except the first one'''
    print('Delaer has: ')
    print(dealer.cards_in_hand[1])
    print()
    print('Player has: ')
    for card in player.cards_in_hand:
        print(card)

def show_all_cards(player, dealer):
    '''Show all cards'''
    print('Player has: ')
    for card in player.cards_in_hand:
        print(card)
    print()
    print('And dealer has:')
    for card in dealer.cards_in_hand:
        print(card)

# Functions to control the end of the game
def player_busts(player, dealer, chips):
        print('You are busted, dealer wins')
        chips.lose_bet()

def player_wins(player, dealer, chips):
        print('Wohoo, player rocks')
        chips.win_bet()

def dealer_busts(player, dealer, chips):
        print('You are busted, player wins')
        chips.win_bet()

def dealer_wins(player, dealer, chips):
        print('Wohoo, dealer wins')
        chips.lose_bet()

def push(player,dealer):
    print('It is a tie')

# Lets play the game!!
while True:
    print('Welcome to Blackjack Game!!!')
    deck = Deck()
    deck.shuffle()

    player = Hand()
    dealer = Hand()

    counter = 0
    while counter < 2:
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())
        counter += 1

    # Player chips
    player_chips = Chips()
    # Player places a bet
    make_bet(player_chips)
    print('Your bet is: ', player_chips.bet)

    # Show some cards
    show_some_cards(player, dealer)

    while game_on:

        # Hit or Stand
        hit_or_stand(deck, player)
        show_some_cards(player, dealer)
        if player.value > 21:
            player_busts(player, dealer, player_chips)
            break

    # Soft 17 rule
    if player.value <= 21:
        while dealer.value < 17:
            hit(deck, dealer)
        show_all_cards(player, dealer)
        # All possible scenarios
        if player.value > dealer.value:
            player_wins(player ,dealer, player_chips)
        elif player.value < dealer.value and dealer.value <= 21:
            dealer_wins(player, dealer, player_chips)
        elif dealer.value > 21:
            dealer_busts(player, dealer, player_chips)
        else:
            push(player, dealer)
        # Inform Player of their total chips
        print()
        print('Player total chips value is: ', player_chips.total_chips)

    # Would you like to play again??
    play_again = input('Would you like to play again? Press y for yes or n for no:')
    if play_again.lower() == 'n':
        print('Thank you for playing this lovely game')
        break
    else:
        game_on = True
