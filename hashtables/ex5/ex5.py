# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    #loop through the list of paths
        #grab the filename from the end of the path
        #if it's in the cache already then just append the path to the list of paths
        #if it's not, then add it
    #loop through the list of queries
        #append the value of the query in the cache to the result
    possible_queries = {}
    result = []

    for path in files:
        partial_paths = path.split("/")
        possible_query = partial_paths[-1]

        if possible_query in possible_queries:
            possible_queries[possible_query].append(path)
        else:
            possible_queries[possible_query] = [path]

    for query in queries:
        if query in possible_queries:
            for item in possible_queries[query]:
                result.append(item)

    print(result)
    return result
















if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
