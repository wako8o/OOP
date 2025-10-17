def read_next(*args):

    for arg in args:
       yield from arg

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)


