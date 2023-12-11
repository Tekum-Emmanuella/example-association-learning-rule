itemset_type = list[object]
dataset_type = list[list[object]]


def support(itemsets: dataset_type, data_set: itemset_type) -> float:
    """
    To find the frequency of itemsets in the dataset.
    """

        # Mock dataset
dataset = [
            ['top', 'milk', 'home'],
            ['top', 'fanta', 'beer', 'fish'],
            ['milk', 'fanta', 'beer', 'cola'],
            ['top', 'milk', 'fanta', 'beer'],
            ['top', 'milk', 'fanta', 'cola']
        ]
itemset = ['top', 'milk']

support_value = support(itemset, dataset)
print("Support value for itemset:", support_value)