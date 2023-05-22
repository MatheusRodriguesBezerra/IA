import csv
import math
from collections import Counter

class Edge:
    def __init__(self, val):
        self.value = val
        self.child = None
        self.total = 0

class Node:
    def __init__(self, attribute):
        self.attribute = attribute
        self.edges = []
        self.final = False
        self.result = None

class Tree:
    def __init__(self, data, target):
        self.root = self.treeBuild(data, target)

    def treeBuild(self, data, target):
        root = Node(None)
        if self.homogenity(data, target):
            root.final = True
            root.result = data[0][target]
            return root
        if len(data[0]) == 1:
            root.final = True
            root.result = self.mostCommon(data, target)
            return root
        best_attribute = self.selectAttribute(data, target)
        root.attribute = best_attribute
        attribute_values = self.getValue(data, best_attribute)
        for value in attribute_values:
            sub_data = self.getSubData(data, best_attribute, value)
            child_node = self.treeBuild(sub_data, target)
            edge = Edge(value)
            edge.child = child_node
            root.edges.append(edge)
        return root

    def predict(self, data):
        return self.predictRecursive(self.root, data)

    def predictRecursive(self, node, data):
        if node.final:
            return node.result
        for edge in node.edges:
            if data[node.attribute] == edge.value:
                edge.total +=1
                return self.predictRecursive(edge.child, data)

    def homogenity(self, data, target):
        counter = Counter([record[target] for record in data])
        return len(counter.keys()) == 1

    def mostCommon(self, data, target):
        counter = Counter([record[target] for record in data])
        return counter.mostCommon(1)[0][0]

    def getValue(self, data, attribute):
        return list(set([record[attribute] for record in data]))

    def getSubData(self, data, best_attribute, value):
        return [record for record in data if record[best_attribute] == value]

    def entropy(self, data, target):
        entropy = 0
        counter = Counter([record[target] for record in data])
        for value in counter.values():
            p = value / len(data)
            entropy -= p * math.log2(p)
        return entropy

    def gain(self, data, attribute, target):
        total_entropy = self.entropy(data, target)
        values = self.getValue(data, attribute)
        sub_entropy = 0
        for value in values:
            sub_data = self.getSubData(data, attribute, value)
            p = len(sub_data) / len(data)
            sub_entropy += p * self.entropy(sub_data, target)
        return total_entropy - sub_entropy

    def selectAttribute(self, data, target):
        attributes = [a for a in data[0].keys() if a != target]
        if list(data[0].keys())[0] in attributes:
            attributes.remove(list(data[0].keys())[0])
        information_gains = {}
        for attribute in attributes:
            information_gains[attribute] = self.gain(data, attribute, target)
        return max(information_gains, key=information_gains.get)


def csvToDict(csvFilePath):
    jsonArray = []

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for row in csvReader:
            jsonArray.append(row)
    return jsonArray

def genOutput(root, indentation=''):
    output = ''
    if root.attribute is None:
        return ''
    for edge in root.edges:
        output += indentation + '<' + root.attribute + '>\n'
        if edge.child.final:
            output += indentation + ' ' + edge.value + ': '
            output += edge.child.result + ' (total: ' + str(edge.total) + ')\n'
        else:
            output += indentation + ' ' + edge.value + ':\n'
            output += genOutput(edge.child, indentation + '    ')
    return output

csvFilePath = r'./weather.csv'
csvTestFilePath = r'./weather_test.csv'
data = csvToDict(csvFilePath)
test_data = csvToDict(csvTestFilePath)
headers = list(data[0].keys())
key_value = headers[-1]
tree = Tree(data, key_value)


for instance in test_data:
    prediction = tree.predict(instance)
    instance[key_value] = prediction

output = genOutput(tree.root)
print(output)

#Escrever para csv
with open('weather_result.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=headers, lineterminator = '\n')
    writer.writeheader()
    writer.writerows(test_data)