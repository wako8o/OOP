from project.get_id import GetId


class Trainer(GetId):

    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()
        self.next_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"