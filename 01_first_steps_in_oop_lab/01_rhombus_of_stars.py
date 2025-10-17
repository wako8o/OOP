def print_current(space, stars):
    print(' ' * space, '* ' * stars)

def for_loop(num):
    for n in range(1, num + 1):
        print_current(num - n, n)

def revers_loop(num):
    for n in range(1, num):
        print_current(n , num - n)

number = int(input())
for_loop(number)
revers_loop(number)
