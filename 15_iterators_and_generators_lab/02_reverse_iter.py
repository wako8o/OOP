class reverse_iter:

    def __init__(self, iterable: list):
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        if not self.iterable:
            raise StopIteration
        num = self.iterable.pop()
        return num

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)