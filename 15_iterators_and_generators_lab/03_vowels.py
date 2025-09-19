class vowels:

    def __init__(self, word):
        self.word = word
        self.index = 0
        self.vowel = 'aeiouy'

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.word):
            letter_index = self.word[self.index]
            self.index += 1
            if letter_index.lower() in self.vowel:
                return letter_index
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

# def __init__(self, word):
#         self.word = word
#         self.index = - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.index += 1
#         if self.index >= len(self.word):
#             raise StopIteration
#         if self.word[self.index].lower() in 'aeiouy':
#             return self.word[self.index]
#         return self.__next__()

