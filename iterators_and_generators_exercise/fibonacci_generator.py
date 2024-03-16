def fibonacci():
    num = 0
    next = num + 1
    yield num
    yield next
    while True:
        yield num + next
        temp = num
        num = next
        next = num + temp


