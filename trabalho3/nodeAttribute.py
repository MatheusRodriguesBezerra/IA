class NodeAttribute:
    def __init__(self, name, edges, father = None):
        self.father = father
        self.name = name
        self.edges = edges

    