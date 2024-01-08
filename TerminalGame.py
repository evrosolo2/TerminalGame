class Room:
    name = ""
    description = ""
    exits = []

    # creates these attributes when room object is created
    def __init__(self, name, description, exits, room_items):
        self.name = name
        self.description = description
        self.exits = exits
        self.room_items = room_items

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_exits(self):
        return self.exits

    def get_room_items(self):
        return self.room_items

    def list_exits(self):
        return ",".join(exit for exit in self.exits)

    def remove_item(self):
        self.room_items.remove(self.room_items[0])

    # Returns a string representation of the room including its name, description, and exits.
    def __str__(self):
        string = f"{self.name}: {self.description}\nExits:"
        for item in self.exits:
            string += f"\n{item}"
        return string