from typing import List



class Hotel:
    name: str
    rooms: List
    guests: int

    def __init__(self,name:str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls,stars_count:int):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self,room:"Room"):
        if room not in self.rooms:
            self.rooms.append(room)

    def take_room(self,room_number:int,people:int):
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)
                if room.is_taken:
                    self.guests += people

    def free_room(self,room_number:int):
        for room in self.rooms:
            if room.number == room_number:
                self.guests -= room.guests
                room.free_room()


    def print_status(self):
        free_rooms = ', '.join(map(str, [room.number for room in self.rooms if not room.is_taken]))
        taken_rooms = ', '.join(map(str, [room.number for room in self.rooms if room.is_taken]))
        print(f"Hotel {self.name} has {self.guests} total guests")
        print(f"Free rooms: {free_rooms}")
        print(f"Taken rooms: {taken_rooms}")





