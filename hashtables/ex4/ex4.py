def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    #loop through the list
        #add each number to the cache
    #loop through the cache
        #if a number is positive
            #and has a negative match in the cache
                #add it to the result list
    cache = {}
    result = []
    for item in a:
        cache[item] = None

    for key in cache:
        if (key * -1) in cache and key > 0:
            result.append(key)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
