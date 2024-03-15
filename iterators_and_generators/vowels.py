class vowels:
    def __init__(self, string):
        self.string = string
        self.vowels_list = ["a", "e", "i", "u", "y", "o"]
        self.vowels_only = [x for x in self.string if x.lower() in self.vowels_list]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.vowels_only):
            return self.vowels_only[self.index]
        raise StopIteration
