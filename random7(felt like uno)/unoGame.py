import random

# Globals:
players = {}
table=[]
eligible_moves = []

deck=['R 0', 'R 1', 'R 2', 'R 3', 'R 4', 'R 5', 'R 6', 'R 7', 'R 8', 'R 9','R skip', 'R reverse', 'R 2+',
      'B 0', 'B 1', 'B 2', 'B 3', 'B 4', 'B 5', 'B 6', 'B 7', 'B 8', 'B 9', 'B skip', 'B reverse', 'B 2+',
      'G 0', 'G 1', 'G 2', 'G 3', 'G 4', 'G 5', 'G 6', 'G 7', 'G 8', 'G 9', 'G skip', 'G reverse', 'G 2+',
      'Y 0', 'Y 1', 'Y 2', 'Y 3', 'Y 4', 'Y 5', 'Y 6', 'Y 7', 'Y 8', 'Y 9', 'Y skip', 'Y reverse', 'Y 2+',
      'wild*', 'wild*', 'wild*', 'wild*', 'shuffle*hands', 'wild+4*', 'wild+4*', 'wild+4*', 'wild+4*']
    
def create_players(num_players):
    for i in range(num_players):
        players[f"Player {i + 1}"] = []

def turn_order():
    global turns
    turns = list(players.keys())
    
def draw_card(person=list):
    drawn_card = deck.pop(0)
    person.append(drawn_card)
    print(f"{person} drew a card: {drawn_card}")

def played_wild():
    global deck, table
    if "wild*" in table[-1]:
        color = input("Choose a color (R, B, G, Y) for the wild card: ").upper()
        print(f"Wild card played! Color changed to {color}.")
        
    else:
        return 
    
def played_skip():
    global deck, table
    if "skip" in table[-1]:
        print(f"{turns[-1]} played a skip card! The next player is skipped.")
        turns.append(turns.pop(0))  # Move the next player to the end of the turn order
    else:
        return
    
def played_wild_plus4():
    global deck, table
    if "wild+4*" in table[-1]:
        color = input("Choose a color (R, B, G, Y) for the wild +4 card: ").upper()
        print(f"Wild +4 card played! Color changed to {color}.")
        for player in turns:
            if player != turns[-1]:  # Skip the player who played the card
                draw_card(players[player])
    else:
        return
    
def game():
    while True:
        if not deck:
            # shuffle the table except the last card before adding to deck
            deck = table[:-1]
            table = table[-1]  # keep the last card on the table
        
        for player in turns:
            if not players[player]:
                print(f"{player} has no cards left. They win!")
                return
            print(f"{player}'s turn. Current hand: {players[player]}")
            # Here you would implement the logic for the player's turn
            if "*"not in table[-1]:
                eligible_moves = [card for card in player if '*' in card or card.startswith(table[-1][0]) or card.endswith(table[-1][-1])]
            else:
                eligible_moves = [card for card in player if card.startswith(table[-1][0]) or "*"in card])]

            if not eligible_moves:
                print(f"{player} has no valid moves and must draw a card.")
                draw_card(player)
            else:
                print(f"{player} can play: {eligible_moves}")
                # Here you would implement the logic for the player to choose a card to play
                move = input(f"{player}, choose a card to play or type 'draw' to draw a card: ")
                # For simplicity, let's assume they play the first eligible card
                if move.lower() == 'draw':
                    draw_card(player)
                else:
                    if move in eligible_moves:
                        played_card = move
                    else:
                        print(f"{move} is not a valid move. drawing a card instead.")
                        draw_card(player)
                table.append(played_card)
                player.remove(played_card)
                print(f"{player} played: {played_card}")
                
            # For example, drawing a card, playing a card, etc.
            # This is a placeholder for the game logic.
            input("Press Enter to continue to the next player's turn...")
    
    
def main():
    
    pass


main()