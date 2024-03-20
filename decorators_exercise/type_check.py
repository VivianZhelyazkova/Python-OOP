def type_check(some_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if isinstance(*args, some_type):
                result = func(*args, **kwargs)
                return result
            else:
                return "Bad Type"
        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))