class countdown_iterator:

    def __init__(self, count):
        self.count = count + 1
        self. current = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.current == self.count:
            raise StopIteration

        self.count -= 1
        return self.count

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")