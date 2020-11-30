from collections import deque
NUM_OF_PLAYERS = 404
NUM_MARBLES = 71852 * 100
player_score = [0] * NUM_OF_PLAYERS
circle = deque([0])

for marble in range(1,NUM_MARBLES+1):
    if marble % 23 == 0:
        circle.rotate(7)
        player = marble % NUM_OF_PLAYERS
        player_score[player] += marble + circle.popleft()
    else:
        circle.rotate(-2)
        circle.appendleft(marble)
print(max(player_score))