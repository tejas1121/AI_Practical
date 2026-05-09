def prims(graph, V, labels):

    selected = [False] * V

    selected[0] = True

    edges = 0
    cost = 0

    print("Edge : Weight")

    while edges < V - 1:

        minimum = float('inf')

        x = 0
        y = 0

        for i in range(V):

            if selected[i]:

                for neighbor, weight in graph[i]:

                    if not selected[neighbor]:

                        if weight < minimum:

                            minimum = weight

                            x = i
                            y = neighbor

        print(f"{labels[x]}-{labels[y]} : {minimum}")

        cost += minimum

        selected[y] = True

        edges += 1

    print("Total weight of MST:", cost)


graph = {
    0: [(1,7), (2,8)],
    1: [(0,7), (2,3), (3,6)],
    2: [(0,8), (1,3), (3,4), (4,3)],
    3: [(1,6), (2,4), (4,2), (5,5)],
    4: [(2,3), (3,2), (5,2)],
    5: [(3,5), (4,2)]
}

labels = ['A','B','C','D','E','F']

prims(graph, 6, labels)