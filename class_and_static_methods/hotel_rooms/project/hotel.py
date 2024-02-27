from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                taking_room = room.take_room(people)
                if not taking_room:
                    self.guests += people

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                if room.is_taken:
                    self.guests -= room.guests
                    room.free_room()

    def status(self):
        free_rooms = ", ".join([str(x.number) for x in self.rooms if not x.is_taken])
        taken_rooms = ", ".join([str(x.number) for x in self.rooms if x.is_taken])
        result = (f"Hotel {self.name} has {self.guests} total guests\n"
                  f"Free rooms: {free_rooms}\n"
                  f"Taken rooms: {taken_rooms}")
        return result
