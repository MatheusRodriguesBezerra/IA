import csv
import math

def csv_to_dict(csvFilePath):
    jsonArray = []

    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf) 

        for row in csvReader: 
            jsonArray.append(row)
    return jsonArray
  
csvFilePath = r'./restaurant.csv'
dict = csv_to_dict(csvFilePath)

def entropy(data):
    total_count = sum(data.values())
    if total_count == 0:
        return 0
    entropy = 0
    for count in data.values():
        p_i = count / total_count
        if p_i != 0:
            entropy -= p_i * math.log2(p_i)
    return entropy

def get_value_counts(data):
    keys = list(data[0].keys())[:-1]
    last_key = list(data[0].keys())[-1]
    value_counts = {}
    for key in keys:
        value_counts[key] = {}
        for item in data:
            value = item[key]
            class_value = item[last_key]
            if value not in value_counts[key]:
                value_counts[key][value] = {}
            if class_value not in value_counts[key][value]:
                value_counts[key][value][class_value] = 0
            value_counts[key][value][class_value] += 1

    for key in value_counts:
        for value in value_counts[key]:
            value_counts[key][value]["total_count"] = sum(value_counts[key][value].values())

    return value_counts

result = get_value_counts(dict)

for key in result:
    if(key != "ID"):
        print(key)
        for value in result[key]:
            print("  ", value, entropy(result[key][value]))

# print(result)

# def entropy(data, attribute):
#     total = len(data)
#     counts = {}
#     for item in data:
#         label = item[attribute]
#         if label not in counts:
#             counts[label] = 0
#         counts[label] += 1
#     entropy = 0
#     for label in counts:
#         prob = counts[label] / total
#         entropy -= prob * math.log2(prob)
#     return entropy

# entropy(dict, "Pat")

# max_entropy = 0
# max_attribute = ""
# for i in list(dict[0].keys())[1:]:
#     ent = entropy(dict, i)
#     if ent > max_entropy:
#         max_entropy = ent
#         max_attribute = i
# print(max_attribute, max_entropy)



# def ID3(examples, target_attribute, atributtes):
