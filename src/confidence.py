from typing import List
dataset_type = list[list[object]]
rule_type = tuple[list[object], list[object]]


def confidence(data_set: dataset_type, rule: rule_type) -> float:
    """
    To measure the likelihood of occurrence of an itemset given another itemset.
    """
    # Mock dataset
def calculate_support(dataset, itemset):
    count = 0
    for transaction in dataset:
        if set(itemset).issubset(transaction):
            count += 1
    return count

def calculate_confidence(dataset, rule):
    antecedent = rule[0]
    consequent = rule[1]
    
    support_XY = calculate_support(dataset, antecedent + consequent)
    support_X = calculate_support(dataset, antecedent)
    
    if support_X != 0:
        confidence = support_XY / support_X
    else:
        confidence = 0
    
    return confidence

dataset = [
    ["oil", "fish", "yam"],
    ["oil", "fish"],
    ["oil", "yam"],
    ["fish", "yam"],
    ["fish"]
]
rule = (["oil", "fish"], ["yam"])

confidence = calculate_confidence(dataset, rule)
print("Confidence:", confidence)