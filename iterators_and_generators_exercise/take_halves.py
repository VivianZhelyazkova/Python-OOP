def solution():
    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():

        for i in integers():
            yield i / 2

    def take(n, seq):
        some_list = []
        for _ in range(n):
            some_list.append(next(seq))

        return some_list

    return take, halves, integers


