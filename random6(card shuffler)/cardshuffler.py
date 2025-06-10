# Imports
import random

# Globals:
detailed_deck = {}
hands = {}
deck=[]

def create_cards():
    """Create a standard deck of 52 playing cards."""
    
    global detailed_deck, deck
    
    suits = ['♥', '♦', '♣', '♠']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    for suit in suits:
        for rank in ranks:
            card = f"{suit} {rank}"
            detailed_deck[card] = "color"
            
    for card in detailed_deck:
        if 'J'or 'Q'or 'K'or 'A' in card:
            detailed_deck[card] = [{"face" : "true"}]
            if "J" in card:
                detailed_deck[card].append({"value" : 11})
            elif "Q" in card:
                detailed_deck[card].append({"value" : 12})
            elif "K" in card:
                detailed_deck[card].append({"value" : 13})
            elif "A" in card:
                detailed_deck[card].append({"value" : 14})
        else:
            detailed_deck[card] = [{"face" : "false"}]
            detailed_deck[card].append({"value" : int(card.split()[1])})
        
        if '♥' in card or '♦' in card:
            detailed_deck[card].append({"color" : "red"})
        elif '♣' in card or '♠' in card:
            detailed_deck[card].append({"color" : "black"})
    
    deck= list(detailed_deck.keys())
    
            
    
def riffle_shuffle():
    global deck
    left_half = deck[:len(deck)//2]
    right_half = deck[len(deck)//2:]
    shuffled_deck= []
    for i in range(len(deck)):
        if i % 2 == 0:
            shuffled_deck.append(left_half[i // 2])

        else:
            shuffled_deck.append(right_half[(i-1)// 2])
            
    left_half = []
    right_half = []
    deck = shuffled_deck
    print("The deck was riffle shuffled")

    
def strip_shuffle():
    global deck
    num_of_strip_shuffles = random.randint(4, 7)
    
    while num_of_strip_shuffles > 0:
        num_of_strip_shuffles -= 1
        cut_point = random.randint(1, len(deck) - 1)
        cut_cards = deck[cut_point:2*cut_point]
        deck = deck[:cut_point] + deck[2*cut_point:]
        deck = cut_cards + deck
 
    print("The deck was strip shuffled")
    
def random_shuffle():
    global deck
    for num in list(range(random.randint(5,7))):
        if random.randint(0,6) == 0 or 2 or 4:
            riffle_shuffle()
        else:
            strip_shuffle()
    
def distribute_cards(num_players,cards_per_player):
    if cards_per_player//3 != 0 and 0 > cards_per_player >15 :
        raise ValueError("Cards per player must be a multiple of 3 and less than 15.")
        return 
    global deck, hands
    if num_players <= 0 or cards_per_player <= 0:
        raise ValueError("Number of players and cards per player must be greater than zero.")
        return
    if num_players * cards_per_player > len(deck):
        raise ValueError("Not enough cards in the deck to distribute and continue the game.")
        return
    hands = {f"Player {i}": [] for i in range(num_players)}
    card_in_hand = 0
    while card_in_hand < cards_per_player:
        for player in hands:
            hands[player].append(deck.pop(0))
        card_in_hand += 1

def main():
    create_cards()
    
    riffle_shuffle()
    
    strip_shuffle()
    
    riffle_shuffle()
    
    strip_shuffle()
    
    random_shuffle()
    
    players = int(input("Enter the number of players: "))
    cards_per_player = int(input("Enter the number of cards per player: "))
    try:
        distribute_cards(players, cards_per_player)
    except ValueError as e:
        print(e)
        return
    
    print("Distributed hands:")
    for player, hand in hands.items():
        print(f"{player}: {', '.join(hand)}")
        print("\n")
main()