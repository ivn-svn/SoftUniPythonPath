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

    def take_room(self, room_number: int, people: int):
        for room in self.rooms:
            if room.number == room_number:
                result = room.take_room(people)
                if "taken" in result:
                    self.guests += people
                return result
        return f"Room number {room_number} not found"

    def free_room(self, room_number: int):
        for room in self.rooms:
            if room.number == room_number:
                result = room.free_room()
                if "freed" in result:
                    self.guests -= room.guests
                return result
        return f"Room number {room_number} not found"

    def status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {', '.join(free_rooms)}\nTaken rooms: {', '.join(taken_rooms)}"
