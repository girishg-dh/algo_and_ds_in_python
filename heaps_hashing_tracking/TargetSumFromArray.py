def two_sum(arr: list, t: int)-> list:
    hashmap = dict()
    counter = 0
    for idx, v in enumerate(arr):
        if t - v in hashmap:
            return [hashmap[t-v], idx]
        else:
            hashmap[v] = idx
    return -1


print(two_sum([2,4,6,8,10,19], 21))
print(two_sum([-4,-8,0,-7,-3,-10], -15))
print(two_sum([-1,9,56,12,-13,-6,23,19,71,-56,-14], -44))
