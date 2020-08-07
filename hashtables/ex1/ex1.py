def get_indices_of_item_weights(weights, length, limit):

    d = {}

    for i, w in enumerate(weights):
        desired_weight = limit - w
        
        if desired_weight in d:
            return (i, d[desired_weight])
        d[w] = i
    return None
