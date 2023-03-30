from tabuleiro import Tabuleiro
from connectFour import getActionsBot, getActionsPlayer, playerPlays
import random
import math
import time

class TreeNode:
    def __init__(self, state:Tabuleiro,next_player:str, parent=None ):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0.0
        self.next_player = next_player

    def expand(self):
        if(self.next_player == "BOT"):
            for child in getActionsBot(self.state):
                new_node = TreeNode(child, "PLAYER", self)
                self.children.append(new_node)
        else:
            for child in getActionsPlayer(self.state):
                new_node = TreeNode(child, "BOT", self)
                self.children.append(new_node)

    def is_fully_expanded(self):
        return len(self.children) == len(self.state.getColumnsDone())

class MCTS:
    def __init__(self, root_state):
        self.root = TreeNode(root_state, "BOT")

    def run(self, iterations):
        for i in range(iterations):
            node = self.select_node()
            if not node.is_fully_expanded():
                node.expand()
                self.simulate(node.children[-1])
            else:
                self.simulate(node)
        
        return self.get_best_move()

    def select_node(self):
        node = self.root
        while node.children:
            best_child = None
            best_value = float("-inf")
            for child in node.children:
                if child.visits == 0:
                    UCT_value = float("inf")
                else:
                    UCT_value = child.value / child.visits + 2*math.sqrt((math.log(node.visits) / child.visits))
                if UCT_value > best_value:
                    best_child = child
                    best_value = UCT_value
            node = best_child
        return node

    def simulate(self, node):
        state = node.state
        player = node.next_player
        while not state.gameFinished():
            if(player =="BOT"):
                state = random.choice(getActionsBot(state))
                player = "PLAYER"
            else:
                state = random.choice(getActionsPlayer(state))
                player = "BOT"
        reward = state.getPoints()
        self.backpropagate(node, reward)

    def backpropagate(self, node, reward):
        while node is not None:
            node.visits += 1
            node.value += reward
            node = node.parent

    def get_best_move(self):
        best_value = float("-inf")
        best_moves = []
        for child in self.root.children:
            value = child.value / child.visits
            if value > best_value:
                best_value = value
                best_moves = [child.state]
            elif value == best_value:
                best_moves.append(child.state)
        print(len(best_moves))
        return random.choice(best_moves)
    
tab = [
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-']
]

tab = Tabuleiro(tab)
while not tab.gameFinished():
    tab = playerPlays(tab)
    print(tab)
    mcts = MCTS(tab)    
    tab = mcts.run(10000)
    print(tab)
