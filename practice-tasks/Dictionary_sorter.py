def dictionary_sorter(data_dict):
    # Convert the dictionary items to a list of tuples
    items = list(data_dict.items())
    
    # Manually sort the list of tuples by the second element (value)
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i][1] > items[j][1]:  # Compare values
                items[i], items[j] = items[j], items[i]  # Swap if out of order

    # Reconstruct the sorted dictionary
    sorted_dict = {}
    for key, value in items:
        sorted_dict[key] = value

    return sorted_dict
