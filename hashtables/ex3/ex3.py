# WORKS BUT SUPER SLOW
# TRY AGIAN LATER

# def intersection(arrays):
#     d = {}
#     count = 0
#     looking = len(arrays)

#     for x in arrays:
#         count += 1
#         d[count] = []
#         for y in x:
#             if (count - 1) in d:
#                 if y in d[count - 1]:
#                     d[count].append(y)
#             elif count == 1:
#                 d[count].append(y)

#     return d[looking]



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
