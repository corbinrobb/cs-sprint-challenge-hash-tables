def has_negatives(a):
    result = []
    d = {}

    for n in a:
        desired = n * (-1)
        if desired in d:
            if n > desired:
                result.append(n)
            else:
                result.append(desired)
        else:
            d[n] = desired

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
