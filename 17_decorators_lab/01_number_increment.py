def number_increment(numbers):

    def increase():
        result = [x + 1 for x in numbers]
        return result

    return increase()

print(number_increment([1, 2, 3]))