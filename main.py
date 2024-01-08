from room import Room
from adventure_map import AdventureMap
from inventory import Inventory
from item import Item
from room_not_found_error import RoomNotFoundError


def main():
    print("\nWelcome to the Adkins house! This time you won't be able to leave so easily. Goodluck.")

    # Initialize map w/room storage
    adventure_map = AdventureMap()

    # Initialize player inventory
    inventory = Inventory()

    # Initialize Items
    book = Item("Book", "\"A Tale of Two Cities by Charles Dickens\". The greatest novel ever written.")
    book.set_action("read")
    book.set_item_content(
        "You skip to the ending to read Sydney Carton's final speech:\n\tIt is a far, far better thing that I do, than I have ever done; it is a far far better rest that I go to than I have ever known.\nWhat a perfect ending...")

    fork = Item("Fork", "A conveniently pronged eating utensil. Now I just need something to eat.")

    pizza_cutter = Item("Pizza Cutter", "This must be left over from the tragedy that occurred at Adkin's Pizzeria")

    harmonica = Item("Harmonica", "A mouth organ. This might keep me entertained for a couple of hours.")
    harmonica.set_action("play")
    harmonica.set_item_content(
        "You play the sweet sweet melodies of Piano Man on the harmonica. If only someone could hear you...")

    key = Item("Key", "A golden key. This has to unlock something. Right?")
    key.set_action("unlock")
    key.set_item_content(
        "You unlock the trapdoor under the bed. You crawl through it and into the real world.\nParadiso awaits.\nCongratulations.")

    trophy = Item("Old Trophy",
                  "An old youth bowling league trophy. The words engraved in the plaque are: \"Highest Youth Average: Richard Khouri 186\"")

    picture = Item("Picture", "An old picture found on the night stand.")
    picture.set_action("inspect")
    picture.set_item_content(
        "You take a closer look at the picture. It's an old picture of Evan Kessler and Richard Khouri back when they studied at Clemson. Good times.")

    adventure_map.add_room(
        Room("Guest Room", "A room filled with numerous torture devices. Who said anything about welcome guests?",
             ['Kitchen'], [harmonica]))
    adventure_map.add_room(Room("Library",
                                "Better version of the study. It has all of the different books that one may want. Make sure that you stay quiet or the mean librarian will slap you!",
                                ["Holodeck", "Trophy Room", "Study"], [book]))
    adventure_map.add_room(Room("Kitchen",
                                "This amazing culinary art studio has it all: cheese cellar, wine racks, and a 16 stove burner. With its pizza oven, it makes for the perfect Italian getaway.",
                                ["Study", "Guest Room"], [fork, pizza_cutter]))
    adventure_map.add_room(Room("Study",
                                "Do you love being disturbed while working? This room has it all. It is the central hub to the whole house. It has a giant wall of computers and amazing lighting, but doors that exit out into numerous different rooms.",
                                ["Kitchen", "Library", "Bedroom"], []))
    adventure_map.add_room(Room("Holodeck",
                                "A room that can disguise itself in a variety of ways. Experience a lush, humid rainforest, a speakeasy of the 1920’s, or the dungeons of Cooper Library.",
                                ["Library"], [key]))
    adventure_map.add_room(Room("Trophy Room",
                                "Spacious room with oak wood as far as the eye can see, shelves filled to the brim with trophies and obscure collections, it really makes you wonder who they belong to.",
                                ["Bedroom", "Library"], [trophy]))
    adventure_map.add_room(Room("Bedroom",
                                "A lavished bed adorns the center of this room, with long curtains, beautiful rugs, and gilded furniture acting as little details to truly make this a great bedroom. You see a trapdoor hidden under the bed.",
                                ["Study", "Trophy Room"], [picture]))

    # Input variations
    inputs = {"exit": ["exit", "leave"],
              "lookaround": ["look around", "lookaround", "look"],
              "pickup": ["pick up", "pickup", "take", "grab"],
              }

    name = "study"
    print(adventure_map.get_room(name).__str__())
    # gameplay loop
    actions = 0
    gameplay = True
    while True:
        print("Please choose an action: ")
        # strips inputs in order to remove newlines for autograder
        action_choice = input().strip()
        # because strip removes spaces, trophy room and guest room need them back
        if len(action_choice) < 4:
            pass
        elif action_choice[-4] == "R":
            action_choice.replace("Room", " Room")
        if action_choice in inputs["exit"]:
            actions += 1
            print("Where would you like to go?")
            room_choice = input()
            try:
                # .title() used to capitalize first letter of every word
                if room_choice.title() not in adventure_map.get_room(name).get_exits():
                    print(f"Invalid room: {room_choice}-> Room not found")
                elif room_choice.title() in adventure_map.get_room(name).get_exits():
                    name = room_choice
                    print(adventure_map.get_room(name).__str__())
            except RoomNotFoundError as e:
                print(f"{room_choice}-> {e}")
        elif action_choice in inputs["lookaround"]:
            actions += 1
            print(adventure_map.get_room(name).get_description())
            print("You find some items around you: ", end="")
            if len(adventure_map.get_room(name).get_room_items()) == 0:
                print("There are no items around here.")
            elif len(adventure_map.get_room(name).get_room_items()) == 1:
                print(f"{adventure_map.get_room(name).get_room_items()[0].name}.")
            else:
                items = ""
                for item in adventure_map.get_room(name).get_room_items():
                    items = items + item.name + ", "
                items = items[:-2]
                print(f"{items}.")
        elif action_choice == "inventory":
            actions += 1
            print("INVENTORY:")
            for item in inventory.inventory:
                print(f"        {item.name}- {item.description}")
        elif action_choice in inputs["pickup"]:
            actions += 1
            if len(adventure_map.get_room(name).get_room_items()) != 0:
                inventory.add_item(adventure_map.get_room(name).get_room_items()[0])
                adventure_map.get_room(name).remove_item()
                print(f"Picked up {inventory.inventory[-1].name}.")
        elif action_choice == "read":
            actions += 1
            has_book = False
            for item in inventory.inventory:
                if item.name == "Book":
                    print(item.content)
                    has_book = True
                    break
            if not has_book:
                print("I don't have anything to read.")
                # elif count == len(inventory.inventory):
        elif action_choice == "play":
            actions += 1
            has_harmonica = False
            for item in inventory.inventory:
                if item.name == "Harmonica":
                    print(item.content)
                    has_harmonica = True
                    break
            if not has_harmonica:
                print("I don't have anything to play.")
        elif action_choice == "unlock":
            actions += 1
            for item in inventory.inventory:
                if item.name == "Key":
                    print(item.content)
                    gameplay = False
                    break
        elif action_choice.lower() == "inspect":
            actions += 1
            has_picture = False
            for item in inventory.inventory:
                if item.name == "Picture":
                    print(item.content)
                    has_picture = True
                    break
            if not has_picture:
                print("I don't have anything to inspect.")
        else:
            print(f'I don\'t know the word "{action_choice}".')

        if not gameplay:
            break
    with open("gamelog.txt","w") as f:
        f.write(str(actions))

if __name__ == "__main__":
    main()
