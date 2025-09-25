class dictionary_iter:

    def __init__(self, dictionary):
        self.dictionary = list(dictionary.items())

    def __iter__(self):
        return self

    def __next__(self):
        if not self.dictionary:
            raise StopIteration
        result_str = self.dictionary.pop(0)
        return result_str

result = dictionary_iter({"name": "Peter", "age": 24.2})
for x in result:
    print(x)

