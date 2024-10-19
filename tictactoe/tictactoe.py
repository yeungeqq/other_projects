"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    move = sum([True for row in board for cell in row if cell != EMPTY])
    if move >= 9:
        return None
    if move % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = []
    i, j = [0, 0]
    for row in board:
        for cell in row:
            if cell == EMPTY:
                action.append((i, j))
            j += 1
        i += 1
        j = 0
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_result = copy.deepcopy(board)
    if action in actions(board):
        i, j = [action[0], action[1]]
        board_result[i][j] = player(board)
    elif action != None:
        raise Exception('Invalid Move')
    return board_result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win_X, win_O = [False, False]

    row_X = [True if row == [X, X, X] else False for row in board]
    if any(row_X):
        win_X = True
    row_O = [True if row == [O, O, O] else False for row in board]
    if any(row_O):
        if win_X == True:
            raise Exception("Invalid Board")
        return O
    if win_X == True:
        return X

    for i in range(3):
        column_X = [True if row[i] == X else False for row in board]
        if all(column_X):
            if win_O == True:
                raise Exception("Invalid Board")
            win_X = True
        column_O = [True if row[i] == O else False for row in board]
        if all(column_O):
            if win_X == True:
                raise Exception("Invalid Board")
            win_O = True
    if win_X == True:
        return X
    if win_O == True:
        return O

    i = 0
    dia_X, dia_O, dia2_X, dia2_O = [[], [], [], []]
    for row in board:
        if row[i] == X:
            dia_X.append(True)
        if row[i] == O:
            dia_O.append(True)
        if row[2-i] == X:
            dia2_X.append(True)
        if row[2-i] == O:
            dia2_O.append(True)
        i += 1
    if sum(dia_X) == 3 or sum(dia2_X) == 3:
        return X
    if sum(dia_O) == 3 or sum(dia2_O) == 3:
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empt = [True if cell == EMPTY else False for row in board for cell in row]
    if not any(empt):
        return True
    if winner(board) != None:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if len(actions(board)) == 1:
        return actions(board)[0]

    euX, euO = [{}, {}]

    if player(board) == X:

        for move in actions(board):
            if winner(result(board, move)) == X:
                return move

            sub_euO = []
            for op_move in actions(result(board, move)):
                set = utility(result(result(board, move), op_move))
                sub_euO.append(set)
            min_euO = {move: min(sub_euO)}
            euX.update(min_euO)
        return max(euX, key=euX.get)

    elif player(board) == O:

        for move in actions(board):
            if winner(result(board, move)) == O:
                return move

            sub_euX = []
            for op_move in actions(result(board, move)):
                set = utility(result(result(board, move), op_move))
                sub_euX.append(set)
            max_euX = {move: max(sub_euX)}
            euO.update(max_euX)
        return min(euO, key=euO.get)
