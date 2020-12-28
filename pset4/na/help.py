def permut(array):
    if len(array) == 1:
        return [array]
    res = []
    for permutation in permut(array[1:]):
        # for i in range(len(array)):
        #     res.append(permutation[:i] + array[0:1] + permutation[i:])
        pass
    return res

print(permut('aba'))