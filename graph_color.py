def is_safe(v, graph, color, c, V):

    for i in range(V):

        if graph[v][i] == 1 and color[i] == c:

            return False

    return True


def solve(v, graph, color, m, V):

    # all vertices colored
    if v == V:

        print("Solution:")

        for i in range(V):

            print("Vertex", i, "-> Color", color[i])

        return True


    # try all colors
    for c in range(1, m + 1):

        if is_safe(v, graph, color, c, V):

            color[v] = c

            if solve(v + 1, graph, color, m, V):

                return True

            # backtrack
            color[v] = 0

    return False


# -------- MAIN --------

graph = [
    [0,1,1,1],
    [1,0,1,0],
    [1,1,0,1],
    [1,0,1,0]
]

V = 4

m = 3

color = [0] * V

solve(0, graph, color, m, V)