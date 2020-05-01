"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {} # this is our adjacency list

# ALL TESTS PASSED
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = dict()

# ALL TESTS PASSED
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2
        """
        # CHECK IF VERTICES EXISTS
        if v1 in self.vertices and v2 in self.vertices:
            # ADD TO EDGE
            self.vertices[v1] = v2
        else:
            print('ERROR ADDING EDGE: VERTEX NOT FOUND')

# ALL TESTS PASSED
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print('ERROR GET NEIGHBORS: VERTEX NOT FOUND')
            return None

# ALL TESTS PASSED
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # CREATE A QUEUE
        qq = Queue()
        # ENQUEUE STARTING VERTEX
        qq.enqueue([starting_vertex])
        # DEBUGGER
        # test = 'hello'
        # breakpoint()
        # CREATE A SET OF TRAVERSED VERTICES
        visited = set()
        # WHILE QUEUE IS NOT EMPTY:
        while qq.size() > 0:
            # DEQUEUE THE FIRST VERTEX
            path = qq.dequeue()
            # IF NOT VISITED:
            if path[-1] not in visited:
                # DO THE THING
                print(path[-1])
                # ADD IT TO VISITED
                visited.add(path[-1])
                # ENQUEUE ALL NEIGHBORS
                for next_vertex in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vertex)
                    qq.enqueue(new_path)

# ALL TESTS PASSED
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # CREATE A STACK
        ss = Stack()
        # push STARTING VERTEX
        ss.push([starting_vertex])
        # CREATE A SET OF TRAVERSED VERTICES
        visited = set()
        # WHILE STACK IS NOT EMPTY:
        while ss.size() > 0:
            # POP THE FIRST VERTEX
            path = ss.pop()
            # IF NOT VISITED:
            if path[-1] not in visited:
                # DO THE THING
                print('LAST OF PATH', path)
                # ADD IT TO VISITED
                visited.add(path[-1])
                # PUSH ALL NEIGHBORS
                for next_vertex in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vertex)
                    ss.push(new_path)

# ALL TESTS PASSED
    def dft_recursive(self, starting_room, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # INITIATE STACK WITH THE FIRST VERTEX
        ss = Stack()
        ss.push([starting_room])
        # BASE CASE: IF STARTING VERTEX IS NONE THEN STOP RECURSION
        if starting_room is None:
            return
        # INITIALIZE VISITED
        if visited is None:
            visited = set()
        # IF THE STARTING VERTEX HAS NOT ALREADY BEEN VISITED
        if starting_room not in visited:
            # WHILE THE STACK HAS AT LEAST ONE ELEMENT
            while ss.size() > 0:
                # POP OUT THAT ELEMENT AND PUT IT INTO OUR NEW ARRAY
                path = ss.pop()
                # CHECK IF THE LAST ELEMENT HAS BEEN VISITED ALREADY
                if path[-1] not in visited:
                    # DO THE THING
                    print(path[-1])
                    # ADD IT TO VISITED
                    # visited.add(starting_room)
                    visited.add(path[-1])
                    # PUSH ALL NEIGHBORS
                    for direction in player.current_room.get_exits():
                        next_room = player.current_room.get_room_in_direction(direction).id
                        new_path = list(path)
                        new_path.append(next_room)
                        ss.push(new_path)
                        # RECURSE WITH LAST ELEMENT AND OUR VISITED SET
                        if next_room == pathSS[-1]:
                            print('PATH', pathSS[-1], direction, 'NEWPATH', new_path)
                            traversal_path.append(direction)
                            player.travel(direction)
                            dft_recursive(path[-1], visited)

# ALL TESTS PASSED
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # CREATE A QUEUE
        qq = Queue()
        # ENQUEUE STARTING VERTEX
        qq.enqueue([starting_vertex])
        # CREATE A SET OF TRAVERSED VERTICES
        visited = set()
        # WHILE QUEUE IS NOT EMPTY:
        while qq.size() > 0:
            # DEQUEUE THE FIRST VERTEX
            path = qq.dequeue()
            # IF THE LAST ELEMENT OF THE PATH IS OUR DESTINATION VERTEX, RETURN
            if path[-1] == destination_vertex:
                return path
            # IF NOT VISITED:
            if path[-1] not in visited:
                # ADD IT TO VISITED
                visited.add(path[-1])
                # ENQUEUE ALL NEIGHBORS
                for next_vertex in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vertex)
                    qq.enqueue(new_path)

# ALL TESTS PASSED
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # CREATE A STACK
        ss = Stack()
        # push STARTING VERTEX
        ss.push([starting_vertex])
        # CREATE A SET OF TRAVERSED VERTICES
        visited = set()
        # WHILE STACK IS NOT EMPTY:
        while ss.size() > 0:
            # POP THE FIRST VERTEX
            path = ss.pop()
            # IF THE LAST ELEMENT OF THE PATH IS OUR DESTINCATION VERTEX, RETURN
            if path[-1] == destination_vertex:
                return path
            # IF NOT VISITED:
            if path[-1] not in visited:
                # ADD IT TO VISITED
                visited.add(path[-1])
                # PUSH ALL NEIGHBORS
                for next_vertex in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vertex)
                    ss.push(new_path)

# ALL TESTS PASSED
    def dfs_recursive(self, starting_vertex, destination_vertex, visited = set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # INITIATE STACK WITH THE FIRST VERTEX
        ss = Stack()
        ss.push([starting_vertex])
        # BASE CASE: IF STARTING VERTEX IS NONE THEN STOP RECURSION
        if starting_vertex is None:
            return
        # IF THE STARTING VERTEX HAS NOT ALREADY BEEN VISITED
        if starting_vertex not in visited:
            # WHILE THE STACK HAS AT LEAST ONE ELEMENT
            while ss.size() > 0:
                # POP OUT THAT ELEMENT AND PUT IT INTO OUR NEW ARRAY
                path = ss.pop()
                # IF THE LAST ELEMENT OF THE PATH IS OUR DESTINCATION VERTEX, RETURN
                if path[-1] == destination_vertex:
                    return path
                # CHECK IF THE LAST ELEMENT HAS BEEN VISITED ALREADY
                if path[-1] not in visited:
                    # ADD IT TO VISITED
                    visited.add(path[-1])
                    # PUSH ALL NEIGHBORS
                    for next_vertex in self.get_neighbors(path[-1]):
                        new_path = list(path)
                        new_path.append(next_vertex)
                        ss.push(new_path)
                        # RECURSE WITH LAST ELEMENT AND OUR VISITED SET
                        self.dfs_recursive(path[-1], visited)