def tags(func):
    def decorator(decor):
        def wrapper(*args, **kwargs):
            result = decor(*args, **kwargs)
            return f"<{func}>{result}</{func}>"

        return wrapper
    return decorator

@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))

@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
