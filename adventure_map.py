from room import Room
from room_not_found_error import RoomNotFoundError

class AdventureMap:
    map = {}

    def add_room(self, room):
        self.map[room.get_name().lower()] = room

    def get_room(self, name):
        if name.lower() not in self.map.keys():
            raise RoomNotFoundError
        else:
            return self.map[name.lower()]
