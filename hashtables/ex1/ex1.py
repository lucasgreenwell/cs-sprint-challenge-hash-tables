def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    #assume that only one thing is gonna do it or that the first one is enough
    #they shouldn't call it limit when it's actually an exact match
    #set up a cache
    # loop through the list of weights
        #add each weight to the cache as a key with a value of the weight needed to reach the match
        #if the weight you need is in the cache already then return the tuple of the two
    cache = {}
    for index,weight in enumerate(weights):
        match_needed = limit - weight
        if match_needed is weight:
            if match_needed in cache:
                return (index, cache[weight])
        if match_needed is not weight:
            if match_needed in cache:
                if cache[match_needed] >= index:
                    return (cache[match_needed], index)
                else:
                    return (index, cache[match_needed])
        cache[weight] = index
    return None
