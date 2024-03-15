class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current_num = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_num += 1
        if self.current_num <= self.end:
            return self.current_num
        raise StopIteration


some = custom_range(1, 5)
for num in some:
    print(num)
