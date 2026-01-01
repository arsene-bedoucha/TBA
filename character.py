# character.py
import random
from config import DEBUG

class Character:
    def __init__(self, name : str, description : str, current_room : None, msgs : list[str]):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs

    def move(self):
        l = [True, False]
        if random.choice(l) is False:
            if DEBUG:
                print(f"DEBUG: {self.name} ne bouge pas")
            return False

        adjacent_rooms = [r for r in self.current_room.exits.values() if r is not None]
        if not adjacent_rooms:
            if DEBUG:
                print(f"DEBUG: {self.name} ne peut pas se déplacer (aucune salle adjacente)")
            return False

        self.current_room.characters.pop(self.name, None)
        new_room = random.choice(adjacent_rooms)
        new_room.characters[self.name] = self
        self.current_room = new_room

        if DEBUG:
            print(f"DEBUG: {self.name} bouge vers {new_room.name}")

        return True

    def __str__(self):
        return f"{self.name} : {self.description}"

    def get_msg(self):
        if not self.msgs:
            return

        msg = self.msgs.pop(0)
        print(msg)
        self.msgs.append(msg)