class RoomNotFoundError(Exception):
        def __int__(self):
            super().__init__("Room not found")