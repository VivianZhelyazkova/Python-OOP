def vowel_filter(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        result = [char for char in result if char in ('a', 'e', 'i', 'o', 'u')]
        return result

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
