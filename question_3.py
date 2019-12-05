def generate_world():
    world = [[],[],[],[],[],[],[],[],[],[]]
    for i in range(10):
        for j in range(10):
            # Each element in world holds its utility, index, and whether or not it's been visited
            world[i] += [[0, (i,j), 0]]
    return world

def pretty_print(world):
    for x in world:
        for y in x:
            print("%.3f" % y[0], end=" ")
        print()

# Get indices of all neighbors, if available
def get_neighbors(world, node):
    neighbors = []
    up = (node[0] - 1, node[1]) 
    down = (node[0] + 1, node[1])
    left = (node[0], node[1] - 1)
    right = (node[0], node[1] + 1)
    if(up[0] >=  0 and world[up[0]][up[1]][2] == 0):
        neighbors += [up]
    if(down[0] <= 9 and world[down[0]][down[1]][2] == 0):
        neighbors += [down]
    if(left[1] >= 0 and world[left[0]][left[1]][2] == 0):
        neighbors += [left]
    if(right[1] <= 9 and world[right[0]][right[1]][2] == 0):
        neighbors += [right]
    return neighbors


def bellman():
    world = generate_world()
    # World a
    world[9][9][0] = 1 
    # World b
    world[9][0][0] = -1
    pretty_print(world)
    # BFS from target (Each element gets a value of 0 initially, besides target) 
    # Each new element, consider if it's value is greater than the value you're about to give it
    # Equation to do is, Is new element's value than V = .9(oldValue) 
    queue = []
    queue.append(world[9][9][1]) 
    while(queue):
        # Remove from queue and mark as visited 
        node = queue.pop(0)
        curr_x = node[0]
        curr_y = node[1]
        world[curr_x][curr_y][2] = 1
        neighbors = get_neighbors(world, node) 
        #print(neighbors)
        #input()
        for coord in neighbors:
            # Add to queue
            new_x = coord[0]
            new_y = coord[1]
            queue.append(coord)

            # Update utility if appropriate
            new_util = .9 * world[curr_x][curr_y][0] 
            if (new_util > world[new_x][new_y][0]):
                if(world[new_x][new_y][0] == -1):
                    continue
                world[new_x][new_y][0] = new_util
    pretty_print(world) 

bellman()
