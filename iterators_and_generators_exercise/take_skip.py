class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.num = 0 - self.step

    def __iter__(self):
        return self

    def __next__(self):
        self.num += self.step
        if self.count > 0:
            self.count -= 1
            return self.num
        raise StopIteration



