class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
    def travel(self, direction, show_rooms = False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            # print('IN PLAYER CLASS - TRAVEL (BEFORE TRAVEL)', self.current_room.id)
            self.current_room = next_room
            # print('IN PLAYER CLASS - TRAVEL (AFTER TRAVEL)', self.current_room.id)
            if (show_rooms):
                next_room.print_room_description(self)
        else:
            print("You cannot move in that direction.", direction, self.current_room.id)
