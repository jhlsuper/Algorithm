import sys

a = (sys.stdin.readline().rstrip())

board = input()

ans = []
i = 0
while i < len(board):
    if board[i:i+4] == 'XXXX':
        ans.append('AAAA')
        i += 4
    elif board[i:i+2] == 'XX':
        ans.append('BB')
        i += 2
    elif board[i] == '.':
        ans.append('.')
        i += 1
    else:
        break

ans = ''.join(ans)
if len(board) == len(ans):
    print(ans)
else:
    print(-1)

