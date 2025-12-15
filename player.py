# player.py

class Player:
    def __init__(self, name, poids_max = 10):
        self.name = name
        self.current_room = None
        self.history = []           # liste pour l'historique.
        self.inventory = {}         # dictionnaire pour l'inventaire du joueur.
        self.poids_max = poids_max

    # Méthode pour retourner l'historique
    def get_history(self):
        return self.history

    def get_inventory(self):
        if not self.inventory :
            return ("Votre inventaire est vide.")   # inventaire du joueur vide.

        texte = "Vous disposez des items suivant :\n"
        for item in self.inventory.values() :
            texte = texte + " - " + str(item) + "\n"
        return texte

    def get_current_weight(self):
        poids = 0
        for item in self.inventory.values():
            poids = poids + int(item.weight)
        return poids
    
    # Déplacement du joueur
    def move(self, direction):
        next_room = self.current_room.exits[direction]

        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        self.history.insert(0, self.current_room)
        self.current_room = next_room
        print(self.current_room.get_long_description())

        return True