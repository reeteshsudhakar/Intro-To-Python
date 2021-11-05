import random

suits = ('Spades', 'Hearts', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit



class Deck:
    
    def __init__(self):
        self.deck = []  # starting out with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_composition = ''
        for card in self.deck:
            deck_composition += '\n' + card.__str__()
        return "The deck contains: " + deck_composition

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = [] 
        self.value = 0   # start with zero value to count number of aces 
        self.aces = 0    # keeps track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1 
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    
    def __init__(self):
        self.total = 100  # can change the bet - maybe allow the user to input the bet? 
        self.bet = 0      # maybe set up a minimum bet? 
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
    
    def dealer_busts(self):
        self.total += (self.bet * 1.5)


def take_bet(chips):
    
    while True: 
        try:
            chips.bet = int(input("How much do you want to bet? "))
        except ValueError:
            print("Sorry, that is not a valid bet. Please enter a proper integer.")
        else: 
            if chips.bet > chips.total:
                print("Sorry, that is not a valid bet. You do not have sufficient funds for that bet. You can bet up to ", chips.total)
            else: 
                break
           

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing  
    
    while True: 
        a = input("Hit or Stand? Enter 'h' or 's'. ")
        
        if a[0].lower() == 'h':
            hit(deck,hand)
        
        elif a[0].lower() == 's':
            print("Player stands.")
            playing = False
        
        else: 
            print("Sorry, please try another input.")
            continue
        break 


def show_some(player,dealer):
    print("\n Dealer's Hand:")
    print("<card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep = '\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep = '\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep = '\n ')
    print("Player's Hand =", player.value)



def player_busts(player, dealer, chips):
    print("That's a bust!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.dealer_busts()
    
def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player, dealer):
    print("Dealer and Player tie! It's a push.")



while True:

    print('Welcome to Blackjack! Your goal is to get as close to 21 with your card ranks without going over!\n\
    Dealer hits until they reaches 17. Aces can count as 1 or 11.')
    
    # Creating & shuffling deck
    # dealing 2 cards to the players
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # setting up chips   
    player_chips = Chips()
    
    # betting
    take_bet(player_chips)
    
    # showing cards 
    show_some(player_hand,dealer_hand)
    
    while playing:  
        
        hit_or_stand(deck, player_hand)
        
        show_some(player_hand,dealer_hand)  
        
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    

        show_all(player_hand,dealer_hand)


        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        

    print("\nPlayer's winnings are a total of: ",player_chips.total)


    another_game = input("Would you like to play another hand? Enter 'y' or 'n'. ")
    
    if another_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing Blackjack!")
        break
