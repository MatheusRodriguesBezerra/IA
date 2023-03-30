from tabuleiro import Tabuleiro
from connectFour import getActionsBot, getActionsPlayer, playerPlays
import random
import math
import time

class TreeNode:
    def __init__(self, state:Tabuleiro,next_player:str, parent:Tabuleiro=None ):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0.0
        self.next_player = next_player

    def expand(self):
        if(self.next_player == "BOT"):
            for child in getActionsBot(self.state):
                new_node = TreeNode(child, "PLAYER", parent=self)
                self.children.append(new_node)
        else:
            for child in getActionsPlayer(self.state):
                new_node = TreeNode(child, "BOT", parent=self)
                self.children.append(new_node)

    def is_fully_expanded(self):
        return len(self.children) == len(self.state.getColumnsDone())

class MCTS:
    def __init__(self, root_state):
        self.root = TreeNode(root_state, "BOT")

    def run(self, iterations):
        for i in range(iterations):
            node = self.select_node()
            # print(node.state)
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
                    UCT_value = child.value / child.visits + (2 * math.log(node.visits) / child.visits)**0.5
                # print(UCT_value)
                if UCT_value > best_value:
                    best_child = child
                    best_value = UCT_value
            node = best_child
        return node

    def simulate(self, node):
        state = node.state
        player = "BOT"
        while not state.gameFinished():
            if(player =="BOT"):
                state = random.choice(getActionsBot(state))
                # print(state)
                player = "PLAYER"
            else:
                state = random.choice(getActionsPlayer(state))
                # print(state)
                player = "BOT"
        reward = state.getPoints()
        self.backpropagate(node, reward)

    def backpropagate(self, node, reward):
        while node is not None:
            node.visits += 1
            node.value += reward
            # print(node.state)
            # print(node.visits)
            # print(node.value)
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
    tab = mcts.run(1000)
    print(tab)
