'''
Consider a game, in which you have two types of powers, A and B and there are 3 types of
 Areas X, Y and Z. Every second you have to switch between these areas, 
 each area has specific properties by which your power A and power B increase or decrease. 
 We need to keep choosing areas in such a way that our survival time is maximized. 
 Survival time ends when any of the powers, A or B reaches less than 0.
 
'''


moves = []

def PowerMove(A, B, X, Y, Z):
    global moves

    if A <= 0 or B <= 0:
        return

    last_move = moves[-1]
    if last_move == 'X':
        A1, B1 = A+Y[0], B+Y[1]
        A2, B2 = A+Z[0], B+Z[1]

        if A1 <= 0 or B1 <= 0:
            moves.append('Z')
            # print(A2, B2)
            PowerMove(A2, B2, X, Y, Z)
        elif A2 <= 0 or B2 <= 0:
            moves.append('Y')
            PowerMove(A1, B1, X, Y, Z)
        elif (A1+B1) >= (A2+B2):
            moves.append('Y')
            PowerMove(A1, B1, X, Y, Z)
        else:
            moves.append('Z')
            PowerMove(A2, B2, X, Y, Z)

    elif last_move == 'Y':
        A1, B1 = A+X[0], B+X[1]
        A2, B2 = A+Z[0], B+Z[1]

        if A1 <= 0 or B1 <= 0:
            moves.append('Z')
            PowerMove(A2, B2, X, Y, Z)
        elif A2 <= 0 or B2 <= 0:
            moves.append('X')
            PowerMove(A1, B1, X, Y, Z)
        elif (A1+B1) >= (A2+B2):
            moves.append('X')
            PowerMove(A1, B1, X, Y, Z)
        else:
            moves.append('Z')
            PowerMove(A2, B2, X, Y, Z)

    elif last_move == 'Z':
        A1, B1 = A+Y[0], B+Y[1]
        A2, B2 = A+X[0], B+X[1]

        if A1 <= 0 or B1 <= 0:
            moves.append('X')
            PowerMove(A2, B2, X, Y, Z)
        elif A2 <= 0 or B2 <= 0:
            moves.append('Y')
            PowerMove(A1, B1, X, Y, Z)
        elif (A1+B1) >= (A2+B2):
            moves.append('Y')
            PowerMove(A1, B1, X, Y, Z)
        else:
            moves.append('X')
            PowerMove(A2, B2, X, Y, Z)

    return 
    


def fill_first_move(X, Y, Z):
    global moves
    x = sum(X)
    y = sum(Y)
    z = sum(Z)

    maxm = max(x,y,z)

    if maxm == x:
        moves.append('X')

    elif maxm == y:
        moves.append('Y')
    else:
        moves.append('Z')

A = 23
B = 10
X = [3,2]
Y = [-5,-10]
Z = [-20,5]

fill_first_move(X, Y, Z)
PowerMove(A, B, X, Y, Z)
print(moves[:-1])