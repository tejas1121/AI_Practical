class GraphColoring:
    def __init__(self, graph, num_colors):
        self.graph = graph
        self.V = len(graph)
        self.colors = []

        # initialize colors with 0
        for i in range(self.V):
            self.colors.append(0)

        self.color_names = ["", "Red", "Green", "Blue"]

    # -------- CHECK SAFE --------
    def is_safe(self, v, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and self.colors[i] == c:
                return False
        return True

    # -------- BACKTRACKING --------
    def solve_graph(self, v, m):
        if v == self.V:
            self.print_solution()
            return True

        for c in range(1, m + 1):
            if self.is_safe(v, c):
                self.colors[v] = c

                if self.solve_graph(v + 1, m):
                    return True

                self.colors[v] = 0   # backtrack

        return False

    # -------- PRINT --------
    def print_solution(self):
        print("Vertex Colors:")
        for i in range(self.V):
            print("Vertex", i, "->", self.color_names[self.colors[i]])

    # -------- DRIVER --------
    def solve(self, m):
        if not self.solve_graph(0, m):
            print("No solution exists")


# -------- MAIN --------
graph = [
    [0,1,1,1],
    [1,0,1,0],
    [1,1,0,1],
    [1,0,1,0]
]

num_colors = 3

gc = GraphColoring(graph, num_colors)
gc.solve(num_colors)