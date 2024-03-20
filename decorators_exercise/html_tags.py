def tags(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = f"<{tag}>{func(*args, **kwargs)}</{tag}>"
            return result

        return wrapper

    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))