# item.py

class Item:
    """
    Cette classe représente un item (objet) que le joueur peut trouver,
    prendre ou déposer dans le jeu.
    """

    def __init__(self, name: str, description: str, weight: str):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight} kg)"
