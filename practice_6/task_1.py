"""
ПР6, Задание 2.
Запрограммировать представления графа (матрица смежности, матрица инцидентности,
список смежности, список дуг, упорядоченный список дуг).
"""

def adjacency_matrix_from_arcs(num_vertices, arcs):
    """Матрица смежности"""
    mat = [[0] * num_vertices for _ in range(num_vertices)]
    for u, v in arcs:
        mat[u][v] = 1
    return mat

def incidence_matrix_from_arcs(num_vertices, arcs):
    """Матрица инцидентности"""
    sorted_arcs = sorted(arcs)         
    m = len(sorted_arcs)
    mat = [[0] * m for _ in range(num_vertices)]
    for col, (u, v) in enumerate(sorted_arcs):
        mat[u][col] = -1
        mat[v][col] = 1
    return mat

def adjacency_list_from_arcs(num_vertices, arcs):
    """Список смежности"""
    adj = {i: [] for i in range(num_vertices)}
    for u, v in arcs:
        adj[u].append(v)
    for u in adj:
        adj[u].sort()
    return adj

def arc_list_from_arcs(arcs):
    """Список дуг"""
    return list(arcs)

def sorted_arc_list_from_arcs(arcs):
    """Упорядоченный список дуг"""
    return sorted(arcs)


if __name__ == '__main__':
    V = 4
    edges = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 0)]

    print("1) Матрица смежности:")
    for row in adjacency_matrix_from_arcs(V, edges):
        print(row)

    print("\n2) Матрица инцидентности:")
    inc = incidence_matrix_from_arcs(V, edges)
    for row in inc:
        print(row)

    print("\n3) Список смежности:")
    print(adjacency_list_from_arcs(V, edges))

    print("\n4) Список дуг:")
    print(arc_list_from_arcs(edges))

    print("\n5) Упорядоченный список дуг:")
    print(sorted_arc_list_from_arcs(edges))
