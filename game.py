# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
from quest import Quest
from config import DEBUG

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.directions_valides = set()
    
    # Setup the game
    def setup(self, player_name=None):
        """Initialize the game with rooms, commands, and quests."""
        self._setup_commands()
        self._setup_rooms()
        self._setup_player(player_name)
        self._setup_items()
        self._setup_characters()
        self._setup_quests()

    # Setup commands
    def _setup_commands(self):
        """Initialize all game commands."""
        self.commands["help"] = Command("help"
                                        , " : afficher cette aide"
                                        , Actions.help
                                        , 0)
        self.commands["quit"] = Command("quit"
                                        , " : quitter le jeu"
                                        , Actions.quit
                                        , 0)
        self.commands["go"] = Command("go"
                                      , "<N|E|S|O> : se déplacer dans une direction cardinale"
                                      , Actions.go
                                      , 1)
        self.commands["history"] = Command("history"
                                      , " : afficher votre historique"
                                      , Actions.history
                                      , 0)
        self.commands["back"] = Command("back"
                                      , " : revenir en arrière"
                                      , Actions.back
                                      , 0)
        self.commands["look"] = Command("look"
                                      , " : observer l'environnement"
                                      , Actions.look
                                      , 0)
        self.commands["take"] = Command("take"
                                      , " <item> : prendre un objet"
                                      , Actions.take
                                      , 1)
        self.commands["drop"] = Command("drop"
                                      , " <item> : reposer un objet"
                                      , Actions.drop
                                      , 1)
        self.commands["check"] = Command("check"
                                      , " : vérifier son inventaire"
                                      , Actions.check
                                      , 0)
        self.commands["talk"] = Command("talk"
                                      , " <pesonnage> : parler à un personnage"
                                      , Actions.talk
                                      , 1)
        self.commands["quests"] = Command("quests"
                                          , " : afficher la liste des quêtes"
                                          , Actions.quests
                                          , 0)
        self.commands["quest"] = Command("quest"
                                         , " <titre> : afficher les détails d'une quête"
                                         , Actions.quest
                                         , 1)
        self.commands["activate"] = Command("activate"
                                            , " <titre> : activer une quête"
                                            , Actions.activate
                                            , 1)
        self.commands["rewards"] = Command("rewards"
                                           , " : afficher vos récompenses"
                                           , Actions.rewards
                                           , 0)

    # Setup rooms
    def _setup_rooms(self):
        """Initialize all rooms and their exits."""

        s = "dans la salle principale. Immense et désert, le réfectoire résonne d un silence oppressant. Les tables en métal, rayées et poisseuses, alignent leurs ombres sous des néons vacillants. Une odeur rance flotte encore, comme un souvenir de repas forcés. Au fond, les portes des cuisines grincent doucement, agitées par un courant d air invisible. L endroit semble vide… mais chaque bruit ici paraît écouter."
        hall = Room("Salle Principale", s)
        
        s = "dans la cuisine. Plongée dans une lumière blafarde, les néons clignotant au-dessus de plans de travail couverts de taches brunâtres. Une odeur lourde de graisse rance et de viande avariée vous prend à la gorge. Dans le silence, un ustensile glisse lentement au sol… alors que personne n est là."
        cuisine = Room("Cuisine", s)

        s = "dans le parloir. Il est plongé dans une pénombre oppressante, les vitres épaisses entre les cabines couvertes de griffures profondes. Les chaises en métal semblent encore vibrer, comme si quelqu un venait de se lever précipitamment. Dans les combinés téléphoniques suspendus, un souffle faible se fait entendre… alors que personne n a décroché."
        parloir = Room("Parloir", s)

        s = "à l infirmerie. Eclairée par une lampe vacillante qui projette des ombres longues sur les lits aux draps froissés et tachés. Les armoires médicales sont entrouvertes, laissant pendre des instruments qui oscillent lentement comme s ils venaient d être utilisés. Une odeur métallique flotte dans l air… et un lit au fond semble encore s affaisser sous un poids invisible."
        infirmerie = Room("Infirmerie", s)
    
        s = "à l accueil. Déserte, les chaises renversées et les vitres blindées couvertes de traces de mains qui semblent s être agrippées dans la panique. Le vieux ventilateur au plafond tourne par à-coups, émettant un grincement régulier qui résonne dans le hall vide. Derrière le comptoir obscurci, vous croyez apercevoir une silhouette immobile… mais en clignant des yeux, elle a disparu."
        accueil = Room("Accueil", s)

        s = "Reserve", "dans la réserve. Encombrée de caisses poussiéreuses et de sacs éventrés, laissant s échapper une odeur d humidité et de moisissure. Les ampoules n éclairent qu un mince couloir entre les étagères tordues, où chaque pas résonne anormalement fort. Au fond, une porte métallique vibre imperceptiblement… comme si quelque chose frappait faiblement derrière."
        reserve = Room("Réserve", s)
        
        s = "en haut de l escalier. Consistué de béton, il descend dans une obscurité épaisse, chaque marche résonnant d un écho creux comme si quelqu un marchait juste derrière vous. La rampe froide est couverte de traces sombres que vous préférez ne pas identifier. Un souffle glacial remonte lentement du bas… pourtant rien ne bouge dans les profondeurs."
        escaliersH = Room("Escaliers Haut", s)

        s = "en bas de l escalier. Consistué de béton, il monte dans une obscurité épaisse, chaque marche résonnant d un écho creux comme si quelqu un marchait juste derrière vous. La rampe froide est couverte de traces sombres que vous préférez ne pas identifier. Un souffle glacial remonte lentement du bas… pourtant rien ne bouge dans les profondeurs."
        escaliersB = Room("Escaliers Bas", s)

        s = "dans une cellule. Minuscule, les murs couverts de griffures irrégulières qui semblent avoir été faites à mains nues. Le lit en fer grince à chaque courant d air, comme s il s animait seul. Une mare d eau stagnante reflète votre silhouette… mais déformée, comme si quelque chose se tenait juste derrière vous."
        cellule = Room("Cellule", s)

        s = "dans votre cellule. Saturée d une odeur âcre, et des dessins étranges recouvrent les murs, tracés avec une précision presque obsessionnelle. Le matelas est déchiré, laissant apparaître des morceaux de tissu entremêlés de cheveux humains. Au centre, une chaise renversée semble avoir été déplacée récemment… pourtant aucun détenu n est censé s y trouver."
        ma_cellule = Room("Ma cellule", s)

        s = "à la sortie. Une lourde grille s est abattue, scellant le passage comme si la prison elle-même refusait de vous laisser partir. De l autre côté, la lumière vacille et projette des ombres qui semblent se rapprocher lentement. Quand vous touchez les barreaux, un frisson glacial remonte votre bras… comme un avertissement."
        sortie = Room("Sortie", s)
        
        for room in [hall, parloir, cuisine, infirmerie, accueil, reserve, escaliersH, escaliersB, cellule, ma_cellule, sortie]:
            self.rooms.append(room)

        # Create exits for rooms

        hall.exits = {"N" : parloir, "E" : infirmerie, "S" : escaliersB, "O" : cuisine, "Up" : None, "Down" : None}
        cuisine.exits = {"N" : reserve, "E" : hall, "S" : escaliersB, "O" : None, "Up" : None, "Down" : None}
        parloir.exits = {"N" : accueil, "E" : None, "S" : hall, "O" : None, "Up" : None, "Down" : None}
        infirmerie.exits = {"N" : accueil, "E" : None, "S" : None, "O" : hall, "Up" : None, "Down" : None}
        accueil.exits = {"N" : sortie, "E" : infirmerie, "S" : parloir, "O" : None, "Up" : None, "Down" : None}
        reserve.exits = {"N" : None, "E" : accueil, "S" : cuisine, "O" : None, "Up" : None, "Down" : None}
        escaliersH.exits = {"N" : None, "E" : cellule, "S" : ma_cellule, "O" : None, "Up" : None, "Down" : escaliersB}
        escaliersB.exits = {"N" : cuisine, "E" : hall, "S" : None, "O" : None, "Up" : escaliersH, "Down" : None}
        cellule.exits = {"N" : None, "E" : None, "S" : None, "O" : escaliersH, "Up" : None, "Down" : None}
        ma_cellule.exits = {"N" : escaliersH, "E" : None, "S" : None, "O" : None, "Up" : None, "Down" : None}
        sortie.exits = {"N" : None, "E" : None, "S" : accueil, "O" : None, "Up" : None, "Down" : None}


    # Setup items
    def _setup_items(self):
        hall = self.rooms[0]
        cuisine = self.rooms[2]
        parloir = self.rooms[1]
        infirmerie = self.rooms[3]
        accueil = self.rooms[4]
        reserve = self.rooms[5]
        escaliersH = self.rooms[6]
        escaliersB = self.rooms[7]
        cellule = self.rooms[8]
        ma_cellule = self.rooms[9]
        sortie = self.rooms[10]

        hall.inventory["note"] = Item("note", "un morceau de papier jauni avec des symboles étranges", 1)
        hall.inventory["barre"] = Item("Barre (fer)", "c'est très lourd !", 11)
        cuisine.inventory["knife"] = Item("knife", "un couteau rouillé mais encore utilisable", 1)

        parloir.inventory["téléphone"] = Item(
            "téléphone",
            "un ancien téléphone à touches est posé",
            1
        )
        
        infirmerie.inventory["médicaments"] = Item(
            "médicaments",
            "une armoire pleine de médicaments",
            1
        )

        infirmerie.inventory["pansements"] = Item(
            "pansements",
            "de quoi se soigner peut toujours être utile",
            1
        )

        reserve.inventory["barre de fer"] = Item(
            "barre de fer",
            "une énorme barre de fer est posée au sol",
            3
        )

        escaliersH.inventory["plan"] = Item(
            "plan",
            "un plan avec les issues de la prison",
            1
        )

        escaliersB.inventory["plan"] = Item(
            "plan",
            "un plan avec les issues de la prison",
            1
        )

    # Setup player and starting room
    def _setup_player(self, player_name=None):
        """Initialize the player."""
        if player_name is None:
            player_name = input("\nEntrez votre nom: ")

        self.player = Player(player_name)
        self.player.current_room = self.rooms[0]

        self.directions_valides = set()
        for room in self.rooms:
            self.directions_valides.update(room.exits.keys())

    # Setup characters
    def _setup_characters(self):
        hall = self.rooms[0]
        cuisine = self.rooms[2]
        parloir = self.rooms[1]
        infirmerie = self.rooms[3]
        accueil = self.rooms[4]
        reserve = self.rooms[5]
        escaliersH = self.rooms[6]
        escaliersB = self.rooms[7]
        cellule = self.rooms[8]
        ma_cellule = self.rooms[9]
        sortie = self.rooms[10]
        
        hall.characters["Bob"] = Character(
            "Bob",
            "un gentil monsieur",
            hall,
            ["Salut, moi c'est Bob !", "Veux tu un indice ?", "Montre moi la carte"]
        )

        cuisine.characters["Cuisto"] = Character(
            "Cuisto",
            "un homme effrayant, transpirant, faisant des plats plus que douteux.",
            cuisine,
            ["Viens manger mon enfant... !", "Veux-tu du ragout ?"]
        )

        hall.characters["Alice"] = Character(
            "Alice",
            "une gentile dame",
            hall,
            ["Salut, moi c'est Alice !", "J'aime les poupées"]
        )

    # Setup quests
    def _setup_quests(self):
        """Initialize all quests."""
        exploration_quest = Quest(
            title="Quete de reconnaissance",
            description="Explorez ces lieux clés pour votre réussite dans le jeu : Infirmerie, Cuisine et Parloir",
            objectives=["Visiter Cuisine", "Visiter Infirmerie", "Visiter Parloir"],
            reward="Titre de l'explorateur"
        )

        item_quest = Quest(
            title = "Première quete",
            description = "Retenez bien cette indication afin de trouver la carte de la prison et pouvoir vous repérer. Dans le hall, seul le sud vous guidera...",
            objectives = ["take plan"],
            reward = "Guide du savoir"
        )

        interaction_quest = Quest(
            title = "Quete d'interaction",
            description = "Parler avec le cuisinier",
            objectives = ["talk Cuisto"],
            reward = "Trophée de sociabilité"
        )

        # Ajouter la quête au gestionnaire de quêtes du joueur
        self.player.quest_manager.add_quest(exploration_quest)
        self.player.quest_manager.add_quest(item_quest)
        self.player.quest_manager.add_quest(interaction_quest)

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
                
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            if command_word != "":
                print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)
    
    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Quand tu ouvres les yeux, tu es affalé sur une table froide du réfectoire. Le silence est si lourd qu il finit par bourdonner dans tes oreilles. Les rangées de chaises renversées, les plateaux éparpillés et l odeur de métal rouillé te donnent l impression que la prison a été abandonnée depuis longtemps. Pourtant… quelque chose cloche. Dans les coins du réfectoire, les ombres semblent trop épaisses, comme si elles retenaient leur souffle à ton passage. Ici, rien n est vraiment désert. Et si tu veux t en sortir, tu vas devoir comprendre ce qui s est glissé entre ces murs — et surtout, ce qui t observe déjà.")
        print("Entrez 'help' si vous avez besoin d'aide.")
        
        print(self.player.current_room.get_long_description())

def main():
    # Create a game object and play the game
    Game().play()
    
if __name__ == "__main__":
    main()