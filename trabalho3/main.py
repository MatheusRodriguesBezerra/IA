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

def transform_dict(data):
    dict = {}
    for key in data:
        dict[key] = {}
        total_count_general = 0
        for value in data[key]:
            dict[key][value] = {}
            total_count_general += data[key][value]["total_count"]
            for class_key in data[key][value]:
                if(class_key != "total_count"):
                    probability = data[key][value][class_key]/data[key][value]["total_count"]
                    dict[key][value][class_key] = probability
            dict[key][value]["total_count"]=data[key][value]["total_count"] 
        dict[key]["total_count"] = total_count_general
    return dict

def entropy(data):
    dict = {}
    for key in data:
        total_entropy = 0
        for value in data[key]:
            if(value!="total_count"):
                partial_entropy = 0
                for class_key in data[key][value]:
                    if(class_key != "total_count"):
                        prob = data[key][value][class_key]
                        entropy = -(prob * math.log2(prob))
                        partial_entropy += entropy
                partial_entropy = partial_entropy * (data[key][value]["total_count"]/data[key]["total_count"])
                total_entropy+=partial_entropy
        dict[key] = total_entropy
    # print(dict)
    return min(dict, key=dict.get)

def get_value_counts(data):
    keys = list(data[0].keys())[1:-1]
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

print(dict)
# print(entropy(transform_dict(result)))
# def ID3(examples, target_attribute, atributtes):
#     # for item in examples:

#     return



# result = get_value_counts(dict)
# print(dict)
# ID3(dict, "Class", list(dict[0].keys())[1:-1])



    



