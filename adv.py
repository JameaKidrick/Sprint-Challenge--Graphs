from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from graph import Graph
from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# ['n', 'n']
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

directions = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
full = {'n':'north', 's':'south', 'e':'east', 'w':'west'}

def lets_go(starting_room, visited = None, ss = None):
    print(f'~~~~~CURRENT ROOM: {player.current_room.id} \n~~~~~POSSIBLE EXITS: {player.current_room.get_exits()}', 'TRAVERSAL PATH', traversal_path, 'VISITED', visited)
    if starting_room is None:
        return
    # CREATE A GRAPH
    graph = Graph()
    # CREATE A STACK
    if ss == None:
        ss = Stack()
    # ADD ROOM TO STACK
        ss.push((None, None))
    # RENAME GRAPH.VERTICES TO VISITED FOR EASY READING
    if visited is None:
        visited = graph.vertices
    # WHILE STACK LENGTH IS LESS THAN 0:
    while ss.size() > 0:
        # TEMP VAR = POP OUT LAST ELEMENT IN STACK
        room_info = ss.pop()
        direction = room_info[0]
        last_room = room_info[1]
        # IF LAST ROOM IN VAR IS NOT IN VISITED:
        print('TEST', player.current_room.id not in visited, player.current_room.id)
        if player.current_room.id not in visited:
            add_to_visited(graph, player.current_room.id, visited)
            if last_room != None:
                visited[last_room][direction] = player.current_room.id
        #         new_path = list(path)
        #         new_path.append(next_room)
        #         ss.push(new_path)
            for k, v in visited[player.current_room.id].items():
                if '?' in visited[player.current_room.id].values():
                    if v == '?':
                        if player.current_room.get_room_in_direction(k) != None:
                            # print(direction)
                            # if direction != None:
                            #     visited[current][directions[direction]] = last_room
                            traversal_path.append(k)
                            player.travel(k)
                            ss.push((k, player.current_room.id))
                            print(f'DESCRIPTION: Player went from ROOM {player.current_room.id} {full[k]} towards ROOM {player.current_room.get_room_in_direction(k).id}')
                            lets_go(player.current_room.get_room_in_direction(k).id, visited, ss)
                else:
                    # THIS IS WHERE THE BFS WILL GO
                    print(f'ENDING: current room {player.current_room.id}, visited: {visited}')
                    return
                    # THIS IS WHERE THE BFS WILL GO
    # print('VISITED', visited, 'CURRENT STACK', ss.stack, 'TRAVERSAL PATH', traversal_path)

def add_to_visited(graph, room, visited):
    # ADD LAST ROOM TO VISITED
    graph.add_vertex(room)
    exits = dict()
    # GET_EXISTS() OF ROOM (GIVES BACK ARRAY)
    # LOOP THROUGH ARRAY AND ADD TO VALUE WITH GET_ROOM_IN_DIRECTION(LOOPED ELEMENT) AS INNER VALUE
    for direction in player.current_room.get_exits():
        next_room = player.current_room.get_room_in_direction(direction).id
        exits[direction] = '?'
        visited[player.current_room.id] = exits
        

def test():
    print('test')

def bfs(current_room, last_direction, destination):
    qq = Queue()
    qq.enqueue([last_direction])
    while qq.size() > 0:
        path = qq.dequeue()
        # print('~~~ BFS ~~~', current_room, last_direction, destination)
        # // ~~~ BFS ~~~ 2 n ?
        print('PATH', path)
        if directions[path[-1]] == destination:
            pass
    return

lets_go(player.current_room.id)


    # print(f'CURRENT GRAPH: {graph.vertices}')
    # # ADDING ROOM TO GRAPH/VISITED
    # if starting_room in graph.vertices:
    #     return
    # if starting_room not in graph.vertices:
    #     graph.add_vertex(room)
    #     exits = dict()
    #     for direction in player.current_room.get_exits():
    #         exits[direction] = '?'
    #         graph.vertices[room] = exits
    #     for k, v in graph.vertices[room].items():
    #         if v == '?':
    #             player.travel(k)
    #             print('TRAVEL TO ROOM:', k, player.current_room.id)
    #             graph.vertices[room][k] = player.current_room.id
    #             lets_go(player.current_room.id, graph)
    #             print(f'CURRENT GRAPH: {graph.vertices}', room, player.current_room.id)
    # return None
    # print(f'CURRENT GRAPH: {graph.vertices}', room, player.current_room.id)
    # print('TRAVERSAL PATH', traversal_path)


# lets_go(player.current_room.id)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
