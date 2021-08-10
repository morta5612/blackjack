import random

# from enum import Enum

# Setting up deck of cards
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def player_hand():
    return [random.choice(cards), random.choice(cards)]


def dealer_hand():
    return [random.choice(cards), random.choice(cards)]


def total(hand):
    num = 0
    for x in hand:
        num += x
    return num


def hit_or_stand(p_hand):
    if total(p_hand) < 21:
        inp = input("Hit(H) or Stand(S)?: ")
        if inp.upper() == 'H':
            print("Hit")
            p_hand.append(random.choice(cards))
            print(p_hand)
            return True
        else:
            print("Stand")
            return False
    elif total(p_hand) == 21:
        print("Total is 21, Stand")
        return False


def compare(p_hand, d_hand):
    p_total = total(p_hand)
    d_total = total(d_hand)
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
    player = player_hand()
    dealer = dealer_hand()
    print("Player Hand: " + str(player))
    print("Dealer Hand: [" + str(dealer[0]) + ", ?]")
    while True:
        if not hit_or_stand(player):
            break
    compare(player, dealer)


go()
