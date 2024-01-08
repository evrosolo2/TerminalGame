class Item:
    action = ""
    content = ""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def set_action(self, action):
        self.action = action

    def set_item_content(self, content):
        self.content = content