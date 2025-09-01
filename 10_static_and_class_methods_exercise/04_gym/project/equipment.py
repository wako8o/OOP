from project.get_id import GetId


class Equipment(GetId):

    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()
        self.next_id()

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
