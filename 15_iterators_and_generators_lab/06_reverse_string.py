def reverse_text(chars):
    result = ''.join(reversed(chars))
    yield result

for char in reverse_text("step"):
    print(char, end='')



# def reverse_text(chars):
#     result = ''.join(chars)[::-1]
#     yield result
#
