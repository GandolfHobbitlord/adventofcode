from pathlib import Path
def get_player_deck(inp):
    return [int(card) for card in inp.splitlines()[1:]]

def parse_input(inp):
    players_raw = inp.split('\n\n')
    return [get_player_deck(p) for p in players_raw]

def combat(deck0,deck1):
    while deck0 and deck1:
        card0 = deck0.pop(0)
        card1 = deck1.pop(0)
        if card0 > card1:
            deck0.extend([card0,card1])
        else:
            deck1.extend([card1,card0])
        # print(f"{deck0}")
        # print(f"{deck1}")
    if deck0:
        return (deck0)
    else:
        return (deck1)

def recursive_combat(deck0,deck1, game = 1):
    g = game
    seen_decks = []

    rond = 0
    while deck0 and deck1:
        if str(deck0) + str(deck1) in seen_decks:
            # print(f"{deck0}")
            # print(f"{deck1}")
            # print("DECK ALREADY SEEN PLAYER 1 wins")
            #player one wins
            return 0, deck0
        else:
            seen_decks.append(str(deck0) + str(deck1))

        rond +=1
        # print(f"Round {rond}")
        # print(f"{deck0}")
        # print(f"{deck1}")
        card0 = deck0.pop(0)
        card1 = deck1.pop(0)
        # print(f'Player 1 plays {card0}')
        # print(f'Player 2 plays {card1}')
        if card0 <= len(deck0) and card1 <= len(deck1):
            g = g+1
            winner, _ = recursive_combat(deck0[:card0],deck1[:card1], g)
        else:
            winner = int(card1>card0)
        # print(f"Player {winner+1} wins round {rond},  game {game}")
        if winner == 0:
            deck0.extend([card0,card1])
        else:
            deck1.extend([card1,card0])
    if deck0:
        return (winner, deck0)
    else:
        return (winner, deck1)



def score(deck):
    return sum([i * card for i, card in enumerate(reversed(deck),1)])
def run_test():
#     inp = """Player 1:
# 9
# 2
# 6
# 3
# 1

# Player 2:
# 5
# 8
# 4
# 7
# 10"""
#     deck0, deck1 = parse_input(inp)
#     winning_deck = combat(deck0.copy(),deck1.copy())
#     assert winning_deck == [3, 2, 10, 6, 8, 5, 9, 4, 7, 1]
#     assert score(winning_deck) == 306
#     _, winning_deck = recursive_combat(deck0,deck1)
#     assert winning_deck == [7, 5, 6, 2, 4, 1, 10, 8, 9, 3]
    inp = """Player 1:
43
19

Player 2:
2
29
14"""
    deck0, deck1 = parse_input(inp)
    recursive_combat(deck0,deck1)
    print("WOHOWHOWHAODSJGHNAIDGAEIOGUHDAOGUIN")

run_test()

with open(Path("2020") / "day22" / "day22_input.txt") as f:
    inp = f.read()
deck0, deck1 = parse_input(inp)
print(score(combat(deck0.copy(),deck1.copy())))
_, winning_deck = recursive_combat(deck0.copy(),deck1.copy())
print(score(winning_deck))