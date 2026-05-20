from itertools import permutations
a = 459
perm = permutations(str(a))
perm_list = [''.join(p) for p in perm]
print(perm_list)