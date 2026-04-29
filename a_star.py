# -------- NODE CLASS --------
class Node:
    def __init__(self, state, x, y, g, parent):
        self.state = state
        self.x = x
        self.y = y
        self.g = g
        self.parent = parent
        self.h = self.calculate_heuristic(state)
        self.f = self.g + self.h

    def calculate_heuristic(self, state):
        goal = [[1,2,3],[4,5,6],[7,8,0]]
        count = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0 and state[i][j] != goal[i][j]:
                    count += 1
        return count


# -------- PRINT STATE --------
def print_state(state):
    for i in range(3):
        for j in range(3):
            print(state[i][j], end=" ")
        print()
    print()


# -------- CHECK GOAL --------
def is_goal(state):
    goal = [[1,2,3],[4,5,6],[7,8,0]]
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j]:
                return False
    return True


# -------- COPY STATE --------
def copy_state(state):
    new_state = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(state[i][j])
        new_state.append(row)
    return new_state


# -------- CHECK IN CLOSED --------
def is_visited(closed, state):
    for s in closed:
        same = True
        for i in range(3):
            for j in range(3):
                if s[i][j] != state[i][j]:
                    same = False
                    break
        if same:
            return True
    return False


# -------- GET NODE WITH MIN F --------
def get_min_node(open_list):
    min_index = 0
    for i in range(len(open_list)):
        if open_list[i].f < open_list[min_index].f:
            min_index = i
    return open_list.pop(min_index)


# -------- PRINT PATH --------
def print_path(node):
    if node is None:
        return
    print_path(node.parent)
    print_state(node.state)


# -------- SOLVE FUNCTION --------
def solve(start, x, y):
    open_list = []
    closed = []

    start_node = Node(start, x, y, 0, None)
    open_list.append(start_node)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while len(open_list) != 0:
        current = get_min_node(open_list)

        if is_goal(current.state):
            print("Goal Reached!\nSolution Path:")
            print_path(current)
            return

        closed.append(current.state)

        for i in range(4):
            nx = current.x + dx[i]
            ny = current.y + dy[i]

            if nx >= 0 and nx < 3 and ny >= 0 and ny < 3:
                new_state = copy_state(current.state)

                # swap
                new_state[current.x][current.y] = new_state[nx][ny]
                new_state[nx][ny] = 0

                if is_visited(closed, new_state):
                    continue

                new_node = Node(new_state, nx, ny, current.g + 1, current)
                open_list.append(new_node)

    print("No Solution Found")


# -------- MAIN --------
start = [
    [1,2,3],
    [4,0,6],
    [7,5,8]
]

solve(start, 1, 1)