#                                        #
#                002                     #
#                 |                      #
#                 |                      #
#                001                     #
#                 |                      #
#                 |                      #
#      008--007--000--003--004           #
#                 |                      #
#                 |                      #
#                005                     #
#                 |                      #
#                 |                      #
#                006                     #
#                                        #

Graph will be a dictionary of vertices. Each vertex (key) will have a value (object)
example> 
{ // dictionary
  vertex(key) -> 0: {'n': '?', 's': '?', 'w': '?', 'e': '?'} <- mapped edges (value)
}

~~~ QUICK BRAIN NOTE: DFS for next move BFS for next move after finding no '?'

**PART 1 DFT**
CREATE A STACK
ADD ROOM TO STACK
RENAME GRAPH.VERTICES TO VISITED FOR EASY READING
WHILE STACK LENGTH IS LESS THAN 0:
  TEMP VAR = POP OUT LAST ELEMENT IN STACK
  IF LAST ROOM IN VAR IS NOT IN VISITED:
    ADD LAST ROOM TO VISITED
    GET_EXISTS() OF ROOM (GIVES BACK ARRAY)
    LOOP THROUGH ARRAY AND ADD TO VALUE WITH GET_ROOM_IN_DIRECTION(LOOPED ELEMENT) AS INNER VALUE
  LOOP THROUGH ROOM'S KEYS AND VALUES (NSEW : #) AND FIND FIRST ROOM PLAYER HAS NOT BEEN (NOT IN VISITED)
  TRAVEL IN THAT DIRECTION

<!-- LOOP THROUGH ARRAY AND ADD TO VALUE WITH '?' AS INNER VALUE
  LOOP THROUGH ROOM'S KEYS AND VALUES (NSEW : '?'/#) AND FIND FIRST '?' -->

|   |
|   |
|_0_|
Stack: [0]
Visited: {}

|   |
|   |
|___|  Var: 0
Stack: [0]
Visited: {0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}}



{
  0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
}



Try moving `south` and you will find yourself in room `5` which contains exits `['n', 's']`. You can now fill in some entries in your graph:

1. `south`

{
  0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
  5: {'n': 0, 's': '?'}
}

2. `south`

{
  0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
  5: {'n': 0, 's': 6},
  6: {'n': 5}
}

No other '?' so move back til a '?' is reached. Next '?' will be at room 0 for north.

5. `north`

{
  0: {'n': 1, 's': 5, 'w': '?', 'e': '?'},
  5: {'n': 0, 's': 6},
  6: {'n': 5},
  1: {'n': '?', 's': 0}
}

6. `north`

{
  0: {'n': 1, 's': 5, 'w': '?', 'e': '?'},
  5: {'n': 0, 's': 6},
  6: {'n': 5},
  1: {'n': 2, 's': 0},
  2: {'s': 1},
}

No other '?' so move back til a '?' is reached. Next '?' will be at room 0 for west.

9. `west`

{
  0: {'n': 1, 's': 5, 'w': 7, 'e': '?'},
  5: {'n': 0, 's': 6},
  6: {'n': 5},
  1: {'n': 2, 's': 0},
  2: {'s': 1},
  7: {'w': '?', 'e': 0}
}

10. `west`

{
  0: {'n': 1, 's': 5, 'w': 7, 'e': '?'},
  5: {'n': 0, 's': 6},
  6: {'n': 5},
  1: {'n': 2, 's': 0},
  2: {'s': 1},
  7: {'w': '8', 'e': 0},
  8: {'e': 7}
}

No other '?' so move back til a '?' is reached. Next '?' will be at room 0 for east.

13. `east`

{
  0: {'n': 1, 's': 5, 'w': 7, 'e': 3},
  5: {'n': 0, 's': 6},
  6: {'n': 5},
  1: {'n': 2, 's': 0},
  2: {'s': 1},
  7: {'w': '8', 'e': 0},
  8: {'e': 7},
  3: {'w': 0, 'e': '?'}
}

14. `east`

{
  0: {'n': 1, 's': 5, 'w': 7, 'e': 3},
  5: {'n': 0, 's': 6},
  6: {'n': 5},
  1: {'n': 2, 's': 0},
  2: {'s': 1},
  7: {'w': '8', 'e': 0},
  8: {'e': 7},
  3: {'w': 0, 'e': 4},
  4: {'w': 3}
}

No other '?' so move back til a '?' is reached. No '?' in graph. Finished.




DEPTH FIRST TRAVERSAL
- Gives the shortest path to another specified node
- If there is more than one valid path, it will just find the first one

|     |
|     |
|     |
|  6  | +
|__2__| +  3

Visited: 

|     |
|     |
|  7  | +
|  5  | +
|__2__|  6

Visited: 3

|  1  | +
|  5  | +
|  4  | +
|  5  |
|__2__|  7

Visited: 3, 6

|  2  | +
|  4  | +
|  5  |
|  4  |
|  5  |
|__2__|  1

Visited: 3, 6, 7

|  7  | +
|  6  | +
|  5  |
|  3  |
|  2  |
|  4  |
|  5  |
|  4  |
|  5  |
|__2__|  5

Visited: 3, 6, 7, 1, 2

|  7  | -
|  6  | -
|  3  | -
|  2  | -
|  4  |
|  5  |
|  4  |
|  5  |
|__2__|  7 VISITED, NEXT... 6 VISITED, NEXT... 3 VISITED, NEXT... 4

Visited: 3, 6, 7, 1, 2, 5

|  7  | -
|  1  | -
|  4  | -
|  5  | -
|  4  | -
|  5  | -
|__2__| - 7 VISITED, NEXT... 1 VISITED, NEXT... 4 VISITED, NEXT...

Visited: 3, 6, 7, 1, 2, 5, 4


BREATH FIRST TRAVERSAL
- Gives the shortest path to all of the other nodes
- If there is more than one valid path, it will just find the first one

______________

             4
______________  

Visited: 

______________
[4, 1]  [4, 7]  
______________  [4]

Visited: 4

____________________________

[4, 1, 7]  [4, 1, 2]  [4, 7]  
____________________________  [4, 1]

Visited: 4, 1

_____________________________________________________

[4, 7, 1]  [4, 7, 6]  [4, 7, 5]  [4, 1, 7]  [4, 1, 2] 
_____________________________________________________  [4, 7]

Visited: 4, 1, 7

____________________________________________________________________________________

[4, 1, 2, 3]  [4, 1, 2, 5]  [4, 1, 2, 1]  [4, 7, 1]  [4, 7, 6]  [4, 7, 5]  [4, 1, 7]   
____________________________________________________________________________________  [4, 1, 2]

Visited: 4, 1, 7, 2

......
____________

[4, 1, 2, 3]  
____________  [4, 1, 2]

Visited: 4, 1, 7, 2