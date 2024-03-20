def make_bold(func):
    def wrapper(*args, **kwargs):
        result = f"<b>{func(*args)}</b>"
        return result

    return wrapper


def make_italic(func):
    def wrapper(*args, **kwargs):
        result = f"<i>{func(*args)}</i>"
        return result

    return wrapper


def make_underline(func):
    def wrapper(*args, **kwargs):
        result = f"<u>{func(*args)}</u>"
        return result

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))
