import csv
import math
from collections import Counter
from typing import List

class Edge:
    def __init__(self, val):
        self.value = val
        self.child = None

class Node:
    def __init__(self, attribute):
        self.attribute = attribute
        self.edges = []
        self.terminal = False
        self.result = None

class Tree:
    def __init__(self, data, target):
        self.root = self.build_tree(data, target)

    def build_tree(self, data, target):
        root = Node(None)
        if self.is_homogeneous(data, target):
            root.terminal = True
            root.result = data[0][target]
            return root
        if len(data[0]) == 1:
            root.terminal = True
            root.result = self.most_common(data, target)
            return root
        best_attribute = self.select_attribute(data, target)
        root.attribute = best_attribute
        attribute_values = self.get_attribute_values(data, best_attribute)
        for value in attribute_values:
            sub_data = self.get_sub_data(data, best_attribute, value)
            child_node = self.build_tree(sub_data, target)
            edge = Edge(value)
            edge.child = child_node
            root.edges.append(edge)
        return root

    def predict(self, data):
        return self.predict_rec(self.root, data)

    def predict_rec(self, node, data):
        if node.terminal:
            return node.result
        for edge in node.edges:
            if data[node.attribute] == edge.value:
                return self.predict_rec(edge.child, data)

    def is_homogeneous(self, data, target):
        counter = Counter([record[target] for record in data])
        return len(counter.keys()) == 1

    def most_common(self, data, target):
        counter = Counter([record[target] for record in data])
        return counter.most_common(1)[0][0]

    def get_attribute_values(self, data, attribute):
        return list(set([record[attribute] for record in data]))

    def get_sub_data(self, data, best_attribute, value):
        return [record for record in data if record[best_attribute] == value]

    def entropy(self, data, target):
        entropy = 0
        counter = Counter([record[target] for record in data])
        for value in counter.values():
            p = value / len(data)
            entropy -= p * math.log2(p)
        return entropy

    def information_gain(self, data, attribute, target):
        total_entropy = self.entropy(data, target)
        values = self.get_attribute_values(data, attribute)
        weighted_entropy = 0
        for value in values:
            sub_data = self.get_sub_data(data, attribute, value)
            p = len(sub_data) / len(data)
            weighted_entropy += p * self.entropy(sub_data, target)
        return total_entropy - weighted_entropy

    def select_attribute(self, data, target):
        attributes = [a for a in data[0].keys() if a != target]
        information_gains = {}
        for attribute in attributes:
            information_gains[attribute] = self.information_gain(data, attribute, target)
        return max(information_gains, key=information_gains.get)
    
def csv_to_dict(csvFilePath):
    jsonArray = []

    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf) 

        for row in csvReader:
            jsonArray.append(row)
    return jsonArray
  
csvFilePath = r'./iris.csv'
csvTestFilePath = r'./iris_test.csv'
data = csv_to_dict(csvFilePath)
test_data = csv_to_dict(csvTestFilePath)
tree = Tree(data, 'class')

# Make predictions for each test instance
for instance in test_data:
    prediction = tree.predict(instance)
    instance["class"] = prediction
    # print(prediction)
print(test_data)

