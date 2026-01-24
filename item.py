# item.py
''' Define the Item class '''

class Item:
    """
    This class represents a item. 
    A item is composed of a name, a description, a weight.
    Attributes:
        name : name of the room.
        desciprion : description of the item.
        weight : weight of the item.
    Methods:
        __init__(self, command_word, help_string, action, number_of_parameters) : The constructor.
        __str__(self) : The string representation of the character.
    """

    def __init__(self, name: str, description: str, weight: str):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight} kg)"
