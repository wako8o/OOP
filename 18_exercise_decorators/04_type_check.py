def type_check(function):
    def decor(func):
        def wrapper(*args, **kwargs):
            for n in args:

                if not isinstance(n, function):
                    return "Bad Type"

            return func(*args, **kwargs)

        return wrapper
    return decor

@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
