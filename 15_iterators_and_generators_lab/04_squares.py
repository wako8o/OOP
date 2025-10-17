def squares(n):
    number = 0
    while n > number:
        number += 1
        yield number * number

num = squares(5)
print(list(squares(5)))