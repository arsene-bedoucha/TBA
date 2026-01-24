# room.py
""" Define the Room class """

class Room:
    """
    This class represents a room. 
    A room is composed of a name and a description.
    Attributes:
        name : name of the room.
        description : description of the room.
        exits (dict) : exits of the room.
        inventory (dict) : items in the room.
        character (dict) : characters in the room.
    Methods:
        __init__(self, command_word, help_string, action, number_of_parameters) : The constructor.
        get_exit(self, direction) : know the exits of the room.
        get_exit_string(self) : print the exits of the room.
        get_long_description(self) : print the room description.
        get_inventory(self) : print the inventory of the room (characters and items).
    """

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}                 # dictionnaire pour l'inventaire de la pièce
        self.characters = {}

    # Retourne la salle accessible dans une direction donnée
    def get_exit(self, direction):
        """Get the exits for a room."""

        if direction in self.exits.keys():
            return self.exits[direction]

        return None

    # Retourne une chaîne décrivant les sorties
    def get_exit_string(self):
        '''Print the exits for a room.'''

        exit_string = "Sorties: "
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Description complète de la salle
    def get_long_description(self):
        '''Print the description of a room.'''

        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"

    def get_inventory(self):
        '''Print items and characters in a room.'''

        if not self.inventory and not self.characters:
            return "Il n'y a rien ici. \n"

        texte = "La pièce contient :\n"
        for item in self.inventory.values():
            texte = texte + " - " + str(item) + "\n"
        for character in self.characters.values():
            texte = texte + " - " + str(character) + "\n"
        return texte
