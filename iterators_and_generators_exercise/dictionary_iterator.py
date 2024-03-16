class dictionary_iter:
    def __init__(self, some_dict):
        self.some_dict = some_dict
        self.keys_list = list(self.some_dict.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.keys_list):
            key = self.keys_list[self.index]
            value = self.some_dict[key]
            self.index += 1
            return key, value
        raise StopIteration


