class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop(-1)

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not self.data

    def __str__(self):
        current_data = list(reversed(self.data))
        return f'[{", ".join(current_data)}]'
