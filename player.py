# player.py

from quest import QuestManager

class Player:
    def __init__(self, name, poids_max = 50, points_min = 150):
        self.name = name
        self.current_room = None
        self.history = []           # liste pour l'historique.
        self.inventory = {}         # dictionnaire pour l'inventaire du joueur.
        self.poids_max = poids_max
        self.move_count = 0
        self.quest_manager = QuestManager(self)
        self.rewards = []
        self.points = []
        self.points_min = points_min

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

        # Check room visit objectives
        self.quest_manager.check_room_objectives(self.current_room.name)

        # Increment move counter and check movement objectives
        self.move_count += 1
        self.quest_manager.check_counter_objectives("Se déplacer", self.move_count)

        return True
    
    def teleport_to_exit(self, exit_room):
        if exit_room.name != "Sortie":
            return False

        self.current_room = exit_room
        print(self.current_room.get_long_description())
        return True
    
    def add_reward(self, reward):
        """
        Add a reward to the player's rewards list.
        
        Args:
            reward (str): The reward to add.
            
        Examples:
        
        >>> player = Player("Bob")
        >>> player.add_reward("Épée magique") # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Vous avez obtenu: Épée magique
        <BLANKLINE>
        >>> "Épée magique" in player.rewards
        True
        >>> player.add_reward("Épée magique") # Adding same reward again
        >>> len(player.rewards)
        1
        """
        if reward and reward not in self.rewards:
            self.rewards.append(reward)
            print(f"\n🎁 Vous avez obtenu: {reward}\n")
    
    def show_rewards(self):
        """
        Display all rewards earned by the player.
        
        Examples:
        
        >>> player = Player("Charlie")
        >>> player.show_rewards() # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Aucune récompense obtenue pour le moment.
        <BLANKLINE>
        >>> player.add_reward("Bouclier d'or") # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Vous avez obtenu: Bouclier d'or
        <BLANKLINE>
        >>> player.show_rewards() # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Vos récompenses:
        • Bouclier d'or
        <BLANKLINE>
        """
        if not self.rewards:
            print("\n🎁 Aucune récompense obtenue pour le moment.\n")
        else:
            print("\n🎁 Vos récompenses:")
            for reward in self.rewards:
                print(f"  • {reward}")
            print()

    def add_points(self, points):
        if points is not None:
            self.points.append(points)
            print(f"\n Vous avez obtenu: {points} points\n")

    def score(self):
        score = sum(self.points)
        return score

    def show_points(self):
        if not self.points:
            print("Vous n'avez aucun point.\n")
            return

        score = self.score()
        print("Votre score : " + str(score) + " points")
