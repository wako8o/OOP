from itertools import permutations

def possible_permutations(param):
   for i in permutations(param):
      yield list(i)

[print(n) for n in possible_permutations([1, 2, 3])]