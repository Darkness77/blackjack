import random

# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    value = 0
    num_aces = 0

    for card in hand:
        if card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A':
            value += 11
            num_aces += 1
        else:
            value += int(card)

    # Adjust the value if there are aces and the total value is greater than 21
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1

    return value

# Function to deal a card from the deck
def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

# Function to play the Blackjack game
def play_blackjack():
    print("Welcome to Blackjack!")

    # Initialize the deck and the player's and dealer's hands
    deck = []
    player_hand = []
    dealer_hand = []

    # Create a new deck of cards
    for _ in range(4):
        deck.extend(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])

    # Shuffle the deck
    random.shuffle(deck)

    # Deal the initial two cards to the player and the dealer
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())

    # Show the player's hand and the dealer's upcard
    print("Your hand:", player_hand)
    print("Dealer's upcard:", dealer_hand[0])

    # Player's turn
    while True:
        choice = input("Do you want to hit or stand? (h/s) ").lower()

        if choice == 'h':
            # Deal a new card to the player
            new_card = deal_card()
            player_hand.append(new_card)
            print("You drew a", new_card)
            
            # Check if the player busts
            if calculate_hand_value(player_hand) > 21:
                print("Bust! You lose.")
                return
        elif choice == 's':
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    # Dealer's turn
    print("Dealer's hand:", dealer_hand)

    # Deal cards to the dealer until their hand value is at least 17
    while calculate_hand_value(dealer_hand) < 17:
        new_card = deal_card()
        dealer_hand.append(new_card)
        print("Dealer drew a", new_card)

        # Check if the dealer busts
        if calculate_hand_value(dealer_hand) > 21:
            print("Dealer busts! You win.")
            return

    # Compare the final hands of the player and the dealer
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    print("Your hand:", player_hand, "Value:", player_value)
    print("Dealer's hand:", dealer_hand, "Value:", dealer_value)

    if player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

# Play the game
play_blackjack()
