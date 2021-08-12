import random
from cards import *

# setting up deck of cards
deck = Deck()


# generates initial hand for the player and cpu
def hand():
    # pick 2 random cards from the deck
    c1, c2 = random.choice(deck.d), random.choice(deck.d)
    # add those cards to the hand
    p_hand = [c1, c2]
    # remove both the cards from the deck so they cannot be drawn again
    deck.d.remove(c1)
    deck.d.remove(c2)
    return p_hand


# gets the total point value for the given hand
def total(deck_hand):
    num = 0
    for x in deck_hand:
        num += x.points
    return num


# a printer that displays the player's hand in a nice format
def print_player_hand(p_hand):
    hand_str = "["
    x = 0
    while x < len(p_hand) - 1:
        hand_str += str(p_hand[x]) + " (" + str(p_hand[x].points) + ") , "
        x += 1
    hand_str += str(p_hand[-1]) + " (" + str(p_hand[-1].points) + ")]"
    return hand_str


# asks the player for input to hit (pick another card) or stand (stop drawing)
# if the player reaches 21 exactly, automatic stand. If the player goes over 21,
# player will lose.
def hit_or_stand(p_hand):
    if total(p_hand) < 21:
        # loop until valid input is received
        loop_var = True
        while loop_var:
            inp = input("Hit(H) or Stand(S)?: ")
            if inp.upper() == 'H':
                print("Hit")
                # pick a random card from the deck, add it to the hand and remove
                # it from the deck so it cannot be picked again
                c = random.choice(deck.d)
                p_hand.append(c)
                deck.d.remove(c)
                print(print_player_hand(p_hand))
                loop_var = False
                return True
            elif inp.upper() == 'S':
                print("Stand")
                loop_var = False
                return False
            else:
                loop_var = True

    elif total(p_hand) == 21:
        print("Total is 21, Stand")
        return False


def compare(p_hand, d_hand):
    # total point values for each hand
    p_total = total(p_hand)
    d_total = total(d_hand)
    # finding the difference from 21 of each hand
    p_difference = 21 - p_total
    d_difference = 21 - d_total

    print("Player total: " + str(p_total))
    print("Dealer total: " + str(d_total))

    if p_total > 21:
        print("Player busted, Dealer wins")
    elif d_total > 21:
        print("Dealer busted, Player wins")
    elif p_difference < d_difference:
        print("Player is closer to 21, Player wins")
    elif p_difference > d_difference:
        print("Dealer is closer to 21, Dealer wins")


def go():
    player = hand()
    dealer = hand()
    print("Player Hand: ", end="")
    print(print_player_hand(player))
    print("Dealer Hand: [" + str(dealer[0]) + " (" + str(dealer[0].points) + "), ?]")
    while True:
        if not hit_or_stand(player):
            break
    compare(player, dealer)


go()
