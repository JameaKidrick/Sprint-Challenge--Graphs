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
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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
visited_gg = {}
final_check = player.current_room.id

def lets_go(starting_room):
    # print(f'START\n\n~~~~~CURRENT ROOM: {player.current_room.id} \n~~~~~POSSIBLE EXITS: {player.current_room.get_exits()} \n~~~~~TRAVERSAL PATH: {traversal_path}\n\n')
    # CREATE A GRAPH
    graph = Graph()
    # CREATE A STACK
    ss = Stack()
    # ADD ROOM TO STACK
    ss.push((None, None))
    # RENAME GRAPH.VERTICES TO VISITED FOR EASY READING
    visited = graph.vertices
    # WHILE STACK LENGTH IS LESS THAN 0:
    while ss.size() > 0:
        if player.current_room.id == 118:
            print('ROOM 118', ss.size(), ss.stack)
        # print('VISITED', visited)
        # print(f'~~~~~CURRENT ROOM: {player.current_room.id} \n~~~~~POSSIBLE EXITS: {player.current_room.get_exits()} \n~~~~~TRAVERSAL PATH: {traversal_path} \n~~~~~VISITED: {visited} \n~~~~~STACK: {ss.stack}\n\n')
        # TEMP VAR = POP OUT LAST ELEMENT IN STACK
        room_info = ss.pop()
        # print('ROOM INFO', room_info)
        if room_info[-1] is not None:
            # print('ROOM INFO SEPARATION ~~~~~~~~', room_info[-1][0])
            direction = room_info[-1][0]
            last_room = room_info[-1][1]
        else:
            direction = room_info[0]
            last_room = room_info[1]
        # print('ROOM INFO', room_info, direction, last_room)
        # IF LAST ROOM IN VAR IS NOT IN VISITED:
        # print('CURRENT ROOM BEFORE CHECKING IF IN VISITED', player.current_room.id)
        if player.current_room.id not in visited:
            add_to_visited(graph, player.current_room.id, visited)
            # print('CHECK', player.current_room.id, last_room, direction)
            if last_room != None and direction != None:
                visited[last_room][direction] = player.current_room.id
                visited[player.current_room.id][directions[direction]] = last_room
                # print('VISITED AFTER ADDING NEW INFO', visited)
                # ADDING COPY OF VISITED TO GLOBAL VISITED VARIABLE
                global visited_gg
                visited_gg = visited
            if '?' in visited[player.current_room.id].values():
                destination = [key for key, value in visited[player.current_room.id].items() if value == '?'][0]
                new_path = list(room_info)
                new_path.append((destination, player.current_room.id))
                traversal_path.append(destination)
                ss.push(new_path)
                player.travel(destination)
            else:
                print('')
                unknown_room = bfs(player.current_room.id, visited, direction)
                if unknown_room is not None:
                    # new_path = list(room_info)
                    # new_path.append((unknown_room[0], unknown_room[1]))
                    # print('CURRENT ROOM', player.current_room.id, 'PATH FROM BFS', unknown_room)
                    last_room_bfs = player.current_room.id
                    for move in unknown_room:
                        # print('NEXT MOVE', move)
                        if player.current_room.id == 23:
                            print('STACK', ss.stack)
                        global final_check
                        final_check = player.current_room.id
                        traversal_path.append(move)
                        player.travel(move)
                        # ISSUE ISSUE ISSUE ISSUE ISSUE
                        # print(f'MOVING {move} FROM {last_room_bfs} TO {player.current_room.id}')
                        if player.current_room.id not in visited:
                            new_path = list(room_info)
                            new_path.append((move, last_room_bfs))
                            ss.push(new_path)
                        else:
                            last_room_bfs = player.current_room.id
                    print('ISSUE???', player.current_room.id)
                else:
                    print('FOUND FULL MAP')
                    print(visited)
                    return
        else:
            
            visited[last_room][direction] = player.current_room.id
            visited[player.current_room.id][directions[direction]] = last_room
            unknown_room = bfs(player.current_room.id, visited, direction)
            if unknown_room is not None:
                # print('CURRENT ROOM 2', player.current_room.id, 'PATH FROM BFS 2', unknown_room)
                last_room_bfs = player.current_room.id
                for move in unknown_room:
                    # print('NEXT MOVE 2', move)
                    traversal_path.append(move)
                    player.travel(move)
                    # print(f'MOVING {move} FROM {last_room_bfs} TO {player.current_room.id} 2')
                    # print('VISITED IN BFS 2', visited)
                    if player.current_room.id not in visited:
                        new_path = list(room_info)
                        new_path.append((move, last_room_bfs))
                        ss.push(new_path)
                        # print('CURRENT ROOM 2', player.current_room.id, last_room_bfs)
                    else:
                        last_room_bfs = player.current_room.id
            else:
                print('STOPS AT: LINE 123')


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

def bfs(current_room, visited, last_direction):
    qq = Queue()
    qq.enqueue([(current_room, directions[last_direction])])
    # print('START', current_room, last_direction, visited)
    visited_qq = set()
    travel = []
    while qq.size() > 0:
        path = qq.dequeue()
        # print('DEBUGGING', path, path[-1])
        if '?' in visited[path[-1][0]].values():
            final_travel = []
            # print('DEBUGGING3', path, path[-1][0], travel)
            direction = [key for key, value in visited[path[-1][0]].items() if value == '?'][0]
            travel.append(direction)
            for room in path:
                if room[0] != current_room:
                    final_travel.append(room[1])
            final_travel.append(direction)
            # print(f'FINAL TRAVEL {final_travel} VS TRAVEL {travel}')
            return final_travel
        if path[-1][0] not in visited_qq:
            visited_qq.add(path[-1][0])
            for next_direction, next_room in visited[path[-1][0]].items():
                if next_room not in visited_qq:
                    new_path = list(path)
                    new_path.append((next_room, next_direction))
                    qq.enqueue(new_path)
                    # print('DEBUGGING2', next_direction, next_room)
                    travel.append(next_direction)
        else:
                print('STOPS AT: LINE 167')

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
    print('STEPS:', len(traversal_path))
    print(f'CURRENT STATUS:\nPLAYER CURRENT ROOM - {player.current_room.id}\nVISITED - {visited_gg}\nCURRENT ROOM IS ALREADY IN VISITED -> HEADED TO BFS - {final_check}')



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