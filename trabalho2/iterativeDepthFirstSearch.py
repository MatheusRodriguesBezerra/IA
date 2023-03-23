from board import Board
from shared import *

def __DFSLimRec(board: Board, path: list, depth:int, limit:int, num_nodes_gen:int):
    path.append(board.getTable())
    if(checkIfSolution(board)):
        return path, True, num_nodes_gen
    
    right:Board = moveRight(board)
    left:Board = moveLeft(board)
    up:Board = moveUp(board)
    down:Board = moveDown(board)

    if(depth==limit):
        if(right is not None or left is not None or up is not None or down is not None):
            return None, False, num_nodes_gen
        return None, True, num_nodes_gen

    children = []
    end = True
    if(right is not None and right.getTable() not in path):
        children.append(right)
        
    if(left is not None and left.getTable() not in path):
        children.append(left)
    
    if(up is not None and up.getTable() not in path):
        children.append(up)
    
    if(down is not None and down.getTable() not in path):
        children.append(down)

    for child in children:
        num_nodes_gen +=1
        result, rec_call_child, n_nodes = __DFSLimRec(child, list(map(list, path)), depth + 1, limit, num_nodes_gen)
        if result is not None:
            return result, True, n_nodes
        end = end and rec_call_child
    return None, end, num_nodes_gen

def __DFSLim(initial_board, limit, num_nodes_gen):
    visited = []
    return __DFSLimRec(initial_board,visited,0, limit, num_nodes_gen)

def IDFS(initial_board):
    limit = 0
    dfslim = False
    num_nodes_gen = 0
    while not dfslim:
        result, dfslim, n_nodes = __DFSLim(initial_board, limit,0)
        num_nodes_gen += n_nodes
        if result is not None:
            return result, num_nodes_gen, limit
        print("NO SOLUTION FOUND IN LIMIT " + str(limit))
        limit+=1
    return None