# class store_results:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         with open("results.txt", "a+") as file:
#             result = self.func(*args, **kwargs)
#             file.write(f'Function "{self.func.__name__}" was called. Result: {result}\n')
#
#         return result

class store_results:

    def __init__(self, filename):
        self.filename = filename

    def __call__(self, func):
        def wraperr(*args, **kwargs):
            with open(self.filename, "a+") as file:
                result = func(*args, **kwargs)
                file.write(f'Function "{func.__name__}" was called. Result: {result}\n')
            return result
        return wraperr


@store_results('result.txt')
def add(a, b):
    return a + b

@store_results('result.txt')
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
