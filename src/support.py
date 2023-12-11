itemset_type = list[object]
dataset_type = list[list[object]]


def support(itemsets: dataset_type, data_set: itemset_type) -> float:
    """
    To find the frequency of itemsets in the dataset.
    """
    count=0
    for transaction in dataset:
        if set(itemset).issubset(transaction):
             count += 1
    support_value=count/len(dataset)
    return support_value
 
if __name__==('__main__'):        
        # Mock dataset
    dataset = [
                ['top', 'milk', 'home'],
                ['top', 'fanta', 'beer', 'fish'],
                ['milk', 'fanta', 'beer', 'cola'],
                ['top', 'milk', 'fanta', 'beer'],
                ['top', 'milk', 'fanta', 'cola']
            ]
    itemset = ['milk']

    support_value = support(itemset, dataset)
    print("Support value for itemset:", support_value)