primes = [3,5,7,11,13,17,19]
 
def readcode():
    x=input() # blank line
    vals = []
    for line in range(3):
        x=input().split(' ')
        vals.extend( list(map(int, x[:3])))
    return tuple(vals)
 
def validswap(board, a, b):
    t = int(board[a])+int(board[b])
    return (t in primes)
 
def swapels(board, a, b):
    t = list(board)
    t[a],t[b] = t[b],t[a]
    return tuple(t)
 
swappos = [[0,1],[1,2],[3,4],[4,5],[6,7],[7,8],[0,3],[3,6],[1,4],[4,7],[2,5],[5,8]]
target = (1,2,3,4,5,6,7,8,9)
 
buffer = [target]
moves = {target : 0} 
 
# Map out distance to target
# step through positions in order of reaching them
tpos = 0
while tpos<len(buffer):
    board = buffer[tpos]
    move = moves[board]
    for s in swappos:
        if validswap(board, *s):
            bboard = swapels(board, *s)
            if not bboard in moves:
                buffer.append(bboard)
                moves[bboard] = move + 1
    tpos += 1
 
n = int(input())
for _ in range(n):
    board = readcode()
    # report move count to target
    if board in moves:
        print(moves[board])
    else:
        print(-1)
