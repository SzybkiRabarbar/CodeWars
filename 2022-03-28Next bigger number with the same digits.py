from itertools import permutations
def next_bigger(n):
    perm = sorted(permutations(n))
    return perm

print(next_bigger(21))