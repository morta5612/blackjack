import random

# setting up deck of cards
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# generates initial hand for the player
def player_hand():
    return [random.choice(cards), random.choice(cards)]


# generates initial hand for the dealer (cpu)
def dealer_hand():
    return [random.choice(cards), random.choice(cards)]


# gets the total point value for the given hand
def total(hand):
    num = 0
    for x in hand:
        num += x
    return num


# asks the player for input to hit (pick another card) or stand (stop drawing)
# if the player reaches 21 exactly, automatic stand. If the player goes over 21,
# player will lose.
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


# compares the player and dealer hands to determine a winner
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


# driver for the project
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
