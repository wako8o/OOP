def vowel_filter(function):

    def wrapper():
        result = [x for x in function() if x.lower() in 'aeoyui']
        return result

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())