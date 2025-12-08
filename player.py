# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None

    # Define the move method.
    def move(self, direction):

        next_room = self.current_room.exits[direction]

        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        self.current_room = next_room
        print(self.current_room.get_long_description())        

        return True