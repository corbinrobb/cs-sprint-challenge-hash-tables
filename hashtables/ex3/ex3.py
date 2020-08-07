def intersection(arrays):
    d = {}
    looking = len(arrays)
    result = []

    for x in arrays:
        for y in x:
            if y not in d:
                d[y] = 1
            else:
                new_count = d[y] + 1 
                d[y] = new_count
                if new_count == looking:
                    result.append(y)

    return result



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
