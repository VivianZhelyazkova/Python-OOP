class Equipment:
    _id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.get_next_id()
        Equipment._id += 1

    @staticmethod
    def get_next_id():
        return Equipment._id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

