# MAP
#####
#                                        #
#                002                     #
#                 |                      #
#                 |                      #
#                001                     #
#                 |                      #
#                 |                      #
#      008--007--000--003--004           #
#       |         |                      #
#       |         |                      #
#      009       005                     #
#       |         |                      #
#       |         |                      #
#      010--011--006                     #
#                                        #

{0: {'n': 1, 's': 5, 'w': '?', 'e': '?'}, 1: {'n': 2, 's': 0}, 2: {'s': 1}, 5: {'n': 0, 's': 6}, 6: {'n': 5, 'w': 11}, 11: {'w': 10, 'e': 6}, 10: {'n': 9, 'e': 11}, 9: {'n': 8, 's': 10}, 8: {'s': 9, 'e': 7}, 7: {'w': 
8, 'e': '?'}}

# INIT
  # GET CURRENT ROOM
    # 0
  # GET THE EXISTS OF THE CURRENT ROOM
    # [n, s, w, e]

# # # HELPER FCN???
# ADD TO VISITED
  # SHOULD LOOK LIKE THIS
    # {0: {n: ?, s: ?, e: ?, w: ?}}

# INITIALIZE STACK
  # (DIRECTION = NONE, PREVIOUS_ROOM = NONE)

# TRAVERSAL IN DFT MODE
  # ONCE WE KNOW WHAT DIRECTION WE ARE GOING, ADD INFO TO STACK
    # ROOM_INFO = POP -> (DIRECTION, PREVIOUS_ROOM)
  # CURRENT_ROOM = CURRENT_ROOM.ID
  # PREVIOUS_ROOM = ROOM_INFO[1]
  # DIRECTION = ROOM_INFO[0]
  # GET THE CURRENT ROOM EXITS FROM VISITED

# CHECK IF CURRENT ROOM IS VISITED
# IF NOT THEN ADD TO VISITED 
  # ADD TO VISITED
  # SHOULD LOOK LIKE THIS
    # {CURRENT_ROOM: {EXITS}}

# THIS SHOULD FAIL ON THE FIRST ITERATION BECAUSE THERE IS NO PREVIOUS_ROOM
# IF PREVIOUS ROOM IS NOT NONE:
  # THIS IS WHERE WE UPDATE OUR PREVIOUS ROOM
  # VISITED[PREVIOUS_ROOM][DIRECTION] = CURRENT_ROOM

# THIS SHOULD FAIL ON THE FIRST ITERATION BECAUSE THERE IS NO DIRECTION
# UPDATE CURRENT ROOM EXITS IF WE HAVE A DIRECTIONS
# IF DIRECTION IS NOT NONE:
  # VISITED[CURRENT_ROOM][REVERSEDIRECTION] = PREVIOUS_ROOM

# UPDATE OUR CURRENT ROOM IN VISITED

# LOOP OVER UNVISITED EXITS/MAYBE ALL EXITS
  # MOVE IN THAT DIRECTION
  # UPDATE TRAVERSAL_PATH -> DIRECTION
  # UPDATE THE STACK -> (DIRECTION, CURRENT_ROOM)

# IF THERE ARE NO EXITS THAT ARE UNVISITED
# ENTER INTO BFT MODE THIS WILL PROBABLY BE A HELPER FUNCTION

# BFS WILL TRAVERSE OVER OUR VISITED GRAPH
  # DESTINATION IS A ROOM WITH QUESTION MARKS
  # BUILDING A PATH TO TRAVERSE AFTER FINDING THE DESTINATION