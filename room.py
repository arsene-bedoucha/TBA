# room.py

class Room:
    """
    Cette classe représente un lieu (une salle) du jeu.
    """

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}                 # dictionnaire pour l'inventaire de la pièce
        self.characters = {}

    # Retourne la salle accessible dans une direction donnée
    def get_exit(self, direction):
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None

    # Retourne une chaîne décrivant les sorties
    def get_exit_string(self):
        exit_string = "Sorties: "
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Description complète de la salle
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
    
    def get_inventory(self) :
        if not self.inventory and not self.characters:
            return "Il n'y a rien ici. \n"
        
        texte = "La pièce contient :\n"
        for item in self.inventory.values():
            texte = texte + " - " + str(item) + "\n"
        for character in self.characters.values():
            texte = texte + " - " + str(character) + "\n"
        return texte