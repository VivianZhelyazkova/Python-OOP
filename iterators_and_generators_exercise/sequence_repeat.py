class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = -1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        self.count += 1
        if self.count <= self.number:
            if self.index == len(self.sequence):
                self.index = 0
            return self.sequence[self.index]
        raise StopIteration

