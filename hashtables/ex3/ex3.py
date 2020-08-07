def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    counts = {}
    for list in arrays:
        for number in list:
            if number in counts:
                counts[number] += 1
            else:
                counts[number] = 1
    for number in counts:
        if counts[number] == len(arrays):
            result.append(number)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
