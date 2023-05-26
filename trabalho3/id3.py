import csv
import math
from collections import Counter


# Class representing an edge in the decision tree
class Edge:
    def __init__(self, val):
        self.value = val
        self.child = None
        self.total = 0


# Class representing a node in the decision tree
class Node:
    def __init__(self, attribute):
        self.attribute = attribute
        self.edges = []
        self.final = False
        self.result = None


# Class representing the decision tree
class Tree:
    def __init__(self, data, target):
        self.discretize(data)  # Discretize float attributes
        self.root = self.treeBuild(data, target)

    # Build the decision tree recursively
    def treeBuild(self, data, target):
        root = Node(None)
        
        # If all instances have the same target value, make the node a leaf node
        if self.homogeneity(data, target):
            root.final = True
            root.result = data[0][target]
            return root
        
        # If there are no more attributes to split on, make the node a leaf node with the most common target value
        if len(data[0]) == 1:
            root.final = True
            root.result = self.mostCommon(data, target)
            return root
        
        best_attribute = self.selectAttribute(data, target)
        root.attribute = best_attribute
        attribute_values = self.getValue(data, best_attribute)
        
        # Recursively build the tree for each attribute value
        for value in attribute_values:
            sub_data = self.getSubData(data, best_attribute, value)
            child_node = self.treeBuild(sub_data, target)
            edge = Edge(value)
            edge.child = child_node
            root.edges.append(edge)
        
        return root

    # Predict the target value for a given instance
    def predict(self, data, float_attributes):
        return self.predictRecursive(self.root, data, float_attributes)

    def predictRecursive(self, node, data, float_attributes):
        # If the current node is a leaf node, return the result
        if node.final:
            return node.result
        
        # Traverse the tree based on the attribute values
        for edge in node.edges:
            if node.attribute in float_attributes:
                # Discretized attribute
                attribute_range = edge.value
                value = float(data[node.attribute])
                if self.is_in_range(attribute_range, value):
                    edge.total += 1
                    return self.predictRecursive(edge.child, data, float_attributes)
            else:
                if data[node.attribute] == edge.value:
                    edge.total += 1
                    return self.predictRecursive(edge.child, data, float_attributes)
    
    # Check if a given value is within the specified attribute range
    def is_in_range(self, attribute_range, value):
        lower, upper = map(float, attribute_range.split("-"))
        return lower <= value < upper

    # Discretize the float attributes in the dataset
    def discretize(self, data):
        numeric_attributes = self.getFloatAttributes(data)
        
        # Apply discretization for each float attribute
        for attribute in numeric_attributes:
            self.applyDiscretization(data, attribute)

    # Get the list of float attributes in the dataset
    def getFloatAttributes(self, data):
        float_attributes = []
        
        # Iterate over the attributes of the first record and check if they can be converted to float
        for attribute in data[0]:
            try:
                if attribute != list(data[0].keys())[0]:
                    float(data[0][attribute])
                    float_attributes.append(attribute)
            except ValueError:
                pass
        
        return float_attributes

    # Apply discretization for a specific attribute in the dataset
    def applyDiscretization(self, data, attribute):
        attribute_values = [float(record[attribute]) for record in data]
        min_value = min(attribute_values)
        max_value = max(attribute_values)
        
        # If all values are the same, no need to discretize
        if min_value == max_value:
            return
        
        num_bins = min(10, int(math.sqrt(len(data))))
        bin_size = (max_value - min_value) / num_bins
        
        # Discretize each record in the dataset based on the attribute bins
        for record in data:
            value = float(record[attribute])
            bin_index = int((value - min_value) / bin_size)
            record[attribute] = f"{min_value + bin_index * bin_size:.2f}-{min_value + (bin_index + 1) * bin_size:.2f}"

    # Check if the data instances have the same target value
    def homogeneity(self, data, target):
        counter = Counter([record[target] for record in data])
        return len(counter.keys()) == 1

    # Get the most common target value in the data instances
    def mostCommon(self, data, target):
        counter = Counter([record[target] for record in data])
        return counter.most_common(1)[0][0]

    # Get the distinct attribute values in the data for a specific attribute
    def getValue(self, data, attribute):
        return list(set([record[attribute] for record in data]))

    # Get the subset of data instances that have a specific attribute value
    def getSubData(self, data, best_attribute, value):
        return [record for record in data if record[best_attribute] == value]

    # Calculate the entropy of the data instances based on the target attribute
    def entropy(self, data, target):
        entropy = 0
        counter = Counter([record[target] for record in data])
        for value in counter.values():
            p = value / len(data)
            entropy -= p * math.log2(p)
        return entropy

    # Calculate the information gain of an attribute based on the data instances and the target attribute
    def gain(self, data, attribute, target):
        total_entropy = self.entropy(data, target)
        values = self.getValue(data, attribute)
        sub_entropy = 0
        for value in values:
            sub_data = self.getSubData(data, attribute, value)
            p = len(sub_data) / len(data)
            sub_entropy += p * self.entropy(sub_data, target)
        return total_entropy - sub_entropy

    # Select the attribute with the highest information gain
    def selectAttribute(self, data, target):
        attributes = [a for a in data[0].keys() if a != target]
        
        # If the first attribute is present in the attributes list, remove it (assumed to be an ID or index)
        if list(data[0].keys())[0] in attributes:
            attributes.remove(list(data[0].keys())[0])
        
        information_gains = {}
        
        # Calculate the information gain for each attribute
        for attribute in attributes:
            information_gains[attribute] = self.gain(data, attribute, target)
        
        # Return the attribute with the highest information gain
        return max(information_gains, key=information_gains.get)


# Helper function to convert CSV file to a list of dictionaries
def csvToDict(csvFilePath):
    jsonArray = []

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for row in csvReader:
            jsonArray.append(row)
    
    return jsonArray


# Generate the output string representation of the decision tree
def genOutput(root, indentation=''):
    output = ''
    
    # Recursively traverse the tree and generate the output string
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


# Helper function to get the float attributes in the dataset
def getFloatAttributes(data):
    float_attributes = []
    
    for attribute in data[0]:
        try:
            if attribute != list(data[0].keys())[0]:
                if data[0][attribute] is not None:
                    float(data[0][attribute])
                    float_attributes.append(attribute)
        except ValueError:
            pass
    
    return float_attributes

def run(file):
    # Path to the CSV file containing the training data
    csvFilePath = './'+file+'.csv'

    # Path to the CSV file containing the test data
    csvTestFilePath = './'+file+'_test.csv'

    # Convert the CSV files to dictionaries
    data = csvToDict(csvFilePath)
    test_data = csvToDict(csvTestFilePath)

    # Get the headers (attribute names) from the training data
    headers = list(data[0].keys())

    # Get the target attribute (the last header)
    key_value = headers[-1]

    # Create the decision tree
    tree = Tree(data, key_value)

    # Get the float attributes in the test data
    float_attributes = getFloatAttributes(test_data)

    # Predict the target value for each instance in the test data using the decision tree
    for instance in test_data:
        prediction = tree.predict(instance, float_attributes)
        instance[key_value] = prediction

    # Generate the output string representation of the decision tree
    output = genOutput(tree.root)

    # Print the decision tree output
    print(output)

    # Write the test data with predicted target values to a CSV file
    with open(file+'_result.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers, lineterminator='\n')
        writer.writeheader()
        writer.writerows(test_data)
