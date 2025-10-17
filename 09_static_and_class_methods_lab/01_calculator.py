from functools import reduce


class Calculator:

    @staticmethod
    def add(*args):
        return reduce(lambda x,y: x + y, args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x,y: x * y, args)

    @staticmethod
    def divide(*args):
        try:
            return reduce(lambda x,y: x / y, args)
        except ValueError('Cannot be divided by 0'):
            pass

    @staticmethod
    def subtract(*args):
        return reduce(lambda x,y: x - y, args)
