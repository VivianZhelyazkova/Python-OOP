class Trainer:
    _id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.get_next_id()
        Trainer._id += 1

    @staticmethod
    def get_next_id():
        return Trainer._id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
