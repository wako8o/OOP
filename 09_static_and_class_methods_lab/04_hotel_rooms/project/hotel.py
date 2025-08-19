class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.capacity = 0

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def get_room(self, room_num):
        return [r for r in self.rooms if r.number == room_num][0]

    def take_room(self, room_number, people):
        room = self.get_room(room_number)
        result = room.take_room(people)

    def free_room(self, room_number):
        room = self.get_room(room_number)
        result =  room.free_room()

    def status(self):
        free = [str(r.number) for r in self.rooms if not r.is_taken]
        take = [str(t.number) for t in self.rooms if t.is_taken]
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join(free)}\n"
                f"Taken rooms: {', '.join(take)}\n")
