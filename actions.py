# Description: The actions module.
""" Define the Command class """

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.

# The error message is stored in the MSG0 and MSG1 variables and formatted
# with the command_word variable, the first word in the command.

# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:
    """
    This class represents an action. 
    Attributes:
        game.
        list_of_words (lst) : list of word in the terminal.
        number_of_parameters (int): The number of parameters expected by the command.
    Methods:
        go : move the player.
        quit : leave the game.
        help : show the commands.
        take : take an item.
        drop : drop an item.
        talk : talk to someone.
        history : show the player history.
        back : go back in the game.
        check : look the player inventory.
        look : look in the room.
        quests : show all the quests.
        quest : show a quest.
        activate : activate a quest.
        rewards : show the player rewards.
        points : show the player score.
        activate_all_quests : activate all the quests.
    """

    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        player = game.player
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        direction = list_of_words[1]
        directions_possibles = [(["N", "Nord", "nord", "NORD", "n"], "N"),
                                (["S", "Sud", "sud", "SUD", "s"], "S"),
                                (["E", "Est", "est", "EST", "e"], "E"),
                                (["O", "Ouest", "ouest", "OUEST", "o"], "O"),
                                (["Up", "UP", "up", "U", "u"], "Up"),
                                (["Down", "down", "DOWN", "D", "d"], "Down")]
        direction = list_of_words[1].upper()
        for liste in directions_possibles :
            if direction in liste[0] :
                direction = liste[1]

        if direction not in game.directions_valides:
            print(f"\n La direction {direction} n'est pas valide.")
            print(game.player.current_room.get_long_description())

            return False

        player.move(direction)

        all_characters = []

        for room in game.rooms:
            all_characters.extend(room.characters.values())

        for character in list(all_characters):
            character.move()

        return True

    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    @staticmethod
    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    @staticmethod
    def history(game, list_of_words, number_of_parameters):
        """
        Print the player history.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> history(game, ["history"], 0)
        True
        >>> history(game, ["history", "N"], 0)
        False

        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        player = game.player

        if len(player.history) == 0:
            print("\n Vous n'avez pas encore d'historique \n")
            return True

        print("\nVotre historique :")
        for salle in player.history:
            print("\t- " + salle.name)
        print()
        return True

    @staticmethod
    def back(game, list_of_words, number_of_parameters):
        """
        Go back in the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> back(game, ["back"], 0)
        True
        >>> back(game, ["back", "N"], 0)
        False

        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        player = game.player
        historique = player.get_history()

        if len(historique) == 0:
            print("\nImpossible de revenir en arrière : aucun historique disponible.\n")
            return False

        previous_room = historique.pop(0)
        player.current_room = previous_room

        print(f"\nVous revenez dans : {previous_room.name}\n")

        if len(historique) == 0:
            print("Votre historique est maintenant vide.\n")
        else:
            print("Historique restant :")
            for salle in historique:
                print("\t- " + salle.name)
            print()
        return True

    @staticmethod
    def check(game, list_of_words, number_of_parameters):
        """
        Check player inventory.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> check(game, ["check"], 0)
        True
        >>> check(game, ["check", "N"], 0)
        False

        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        player = game.player
        print("\n" + player.get_inventory() + "\n") # affiche l'inventaire du joueur.
        return True

    @staticmethod
    def look(game, list_of_words, number_of_parameters):
        """
        Look in the room.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> look(game, ["look"], 0)
        True
        >>> look(game, ["look", "N"], 0)
        False

        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        room = game.player.current_room
        print(room.get_inventory())

        return True

    @staticmethod
    def take(game, list_of_words, number_of_parameters):
        """
        Take an item.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> take(game, ["take"], 1)
        False
        >>> take(game, ["take", "clé"], 1)
        True

        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        item_name = list_of_words[1]

        player = game.player
        room = game.player.current_room

        if item_name not in room.inventory:
            print(f"\nL'item '{item_name}' n'est pas présent ici.\n") # objet pas dans la pièce.
            return False

        item = room.inventory[item_name]
        poids = player.get_current_weight()

        if poids + item.weight > player.poids_max :
            print(f"Impossible de prendre cet objet : poids dépassé ({poids}/{player.poids_max})\n")
            return False

        poids = player.get_current_weight() + item.weight
        item = room.inventory.pop(item_name)
        player.inventory[item_name] = item

        print(f"\nVous avez pris cet objet : {item_name}. \n")
        print(f"Voici le poids actuel de votre inventaire : {poids}/{player.poids_max} kg.\n")

        player.quest_manager.check_action_objectives("take", item_name)

        return True

    @staticmethod
    def drop(game, list_of_words, number_of_parameters):
        """
        Drop an item.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> drop(game, ["drop"], 1)
        False
        >>> drop(game, ["drop", "clé"], 1)
        True

        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        item_name = list_of_words[1]

        player = game.player
        room = game.player.current_room

        # Objet pas dans l'inventaire
        if item_name not in player.inventory:
            print(f"\nL'item '{item_name}' n'est pas dans votre inventaire.\n")
            return False

        item = player.inventory[item_name]
        poids = player.get_current_weight() - item.weight
        item = player.inventory.pop(item_name)
        room.inventory[item_name] = item

        print(f"\nVous avez jeté cet objet : {item_name}. \n")
        print(f"Voici le poids de votre invenaire actuellement : {poids}/{player.poids_max} kg.\n")

        room = game.rooms[8]
        if game.player.current_room is room :
            player.quest_manager.check_action_objectives("drop", item_name)
            game.player.teleport_to_exit(game.rooms[10])

        room2 = game.rooms[2]
        if game.player.current_room is room2 :
            player.quest_manager.check_action_objectives("drop", item_name)

        return True

    @staticmethod
    def talk(game, list_of_words, number_of_parameters):
        """
        Talk with a PNJ.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> talk(game, ["talk"], 1)
        False
        >>> talk(game, ["talk", "Guardien"], 1)
        True

        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        name = list_of_words[1]
        room = game.player.current_room

        if name not in room.characters:
            print(f"\n{name} n'est pas ici.\n")
            return False

        character = room.characters[name]
        character.get_msg()

        player = game.player
        player.quest_manager.check_action_objectives("talk", name)

        return True

    @staticmethod
    def quests(game, list_of_words, number_of_parameters):
        """
        Show all quests and their status.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.quests(game, ["quests"], 0)
        <BLANKLINE>
        📋 Liste des quêtes:
          ❓ Grand Explorateur (Non activée)
          ❓ Grand Voyageur (Non activée)
          ❓ Découvreur de Secrets (Non activée)
        <BLANKLINE>
        True
        >>> Actions.quests(game, ["quests", "param"], 0)
        <BLANKLINE>
        La commande 'quests' ne prend pas de paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Show all quests
        game.player.quest_manager.show_quests()
        return True


    @staticmethod
    def quest(game, list_of_words, number_of_parameters):
        """
        Show details about a specific quest.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.quest(game, ["quest", "Grand", "Voyageur"], 1)
        <BLANKLINE>
        📋 Quête: Grand Voyageur
        📖 Déplacez-vous 10 fois entre les lieux.
        <BLANKLINE>
        Objectifs:
          ⬜ Se déplacer 10 fois (Progression: 0/10)
        <BLANKLINE>
        🎁 Récompense: Bottes de voyageur
        <BLANKLINE>
        True
        >>> Actions.quest(game, ["quest"], 1)
        <BLANKLINE>
        La commande 'quest' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n < number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the quest title from the list of words (join all words after command)
        quest_title = " ".join(list_of_words[1:])

        # Prepare current counter values to show progress
        current_counts = {
            "Se déplacer": game.player.move_count
        }

        # Show quest details
        game.player.quest_manager.show_quest_details(quest_title, current_counts)
        return True


    @staticmethod
    def activate(game, list_of_words, number_of_parameters):
        """
        Activate a specific quest.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.activate(game, ["activate", "Grand", "Voyageur"], 1) # doctest: +ELLIPSIS
        <BLANKLINE>
        🗡️  Nouvelle quête activée: Grand Voyageur
        📝 Déplacez-vous 10 fois entre les lieux.
        <BLANKLINE>
        True
        >>> Actions.activate(game, ["activate"], 1)
        <BLANKLINE>
        La commande 'activate' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n < number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the quest title from the list of words (join all words after command)
        quest_title = " ".join(list_of_words[1:])

        # Try to activate the quest
        if game.player.quest_manager.activate_quest(quest_title):
            return True

        msg1 = f"\nImpossible d'activer la quête '{quest_title}'. "
        msg2 = "Vérifiez le nom ou si elle n'est pas déjà active.\n"
        print(msg1 + msg2)
        # print(f"\nImpossible d'activer la quête '{quest_title}'. \
        #             Vérifiez le nom ou si elle n'est pas déjà active.\n")
        return False


    @staticmethod
    def rewards(game, list_of_words, number_of_parameters):
        """
        Display all rewards earned by the player.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.rewards(game, ["rewards"], 0)
        <BLANKLINE>
        🎁 Aucune récompense obtenue pour le moment.
        <BLANKLINE>
        True
        >>> Actions.rewards(game, ["rewards", "param"], 0)
        <BLANKLINE>
        La commande 'rewards' ne prend pas de paramètre.
        <BLANKLINE>
        False
        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Show all rewards
        game.player.show_rewards()
        return True

    def points(game, list_of_words, number_of_parameters):
        """
        Print the player score.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> points(game, ["points"], 0)
        True
        >>> points(game, ["points", "N"], 0)
        False

        """
        n = len(list_of_words)
        if n != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        player = game.player
        player.show_points()
        return True

    def activate_all_quests(game, list_of_words, number_of_parameters):
        """
        Activate all the quests with one command.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> activate_all_quests(game, ["activate_all_quests"], 0)
        True
        >>> activate_all_quests(game, ["activate_all_quests", "N"], 0)
        False

        """
        n = len(list_of_words)
        if n < number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        game.player.quest_manager.activate_all_quests()
        return True
