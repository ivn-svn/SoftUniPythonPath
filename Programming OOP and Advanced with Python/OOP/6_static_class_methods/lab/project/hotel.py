from movie_world.project import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = self.find_room_by_room_number(room_number)
        result = room.take_room(people)
        if result:
            return result
        self.guests += people

    def free_room(self, room_number):
        room = self.find_room_by_room_number(room_number)
        room_guests = self.guests
        result = room.free_room()
        if result:
            return result
        self.guests -= room_guests

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        return f'Hotel {self.name} has {self.guests} total guests\n' \
               f'Free rooms: {", ".join(free_rooms)}\n' \
               f'Taken rooms: {", ".join(taken_rooms)}'

    def find_room_by_room_number(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room
        return None