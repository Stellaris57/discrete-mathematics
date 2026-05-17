"""
ПР6, Задание 3.
Функция просмотра дуг, исходящих из данной вершины.
Вход: граф в любом представлении, название представления, номер вершины.
Выход: список кортежей (i, j), где i – исходная вершина, j – целевая.
"""

def outgoing_arcs(graph, repr_name, vertex):
    """
    graph      – структура данных, соответствующая repr_name
    repr_name  – одно из: 'матрица смежности', 'матрица инцидентности',
                 'список смежности', 'список дуг', 'упорядоченный список дуг'
    vertex     – номер вершины (int)
    """
    result = []

    if repr_name == 'матрица смежности':
        # graph – двумерный список n x n
        n = len(graph)
        for j in range(n):
            if graph[vertex][j] == 1:
                result.append((vertex, j))

    elif repr_name == 'матрица инцидентности':
        # graph – двумерный список n x m; -1 исток, +1 сток
        n = len(graph)
        m = len(graph[0]) if n > 0 else 0
        for col in range(m):
            if graph[vertex][col] == -1:
                # ищем целевую вершину в том же столбце
                for row in range(n):
                    if graph[row][col] == 1:
                        result.append((vertex, row))
                        break   # в столбце ровно одна +1

    elif repr_name == 'список смежности':
        # graph – словарь {вершина: [соседи]}
        for target in graph.get(vertex, []):
            result.append((vertex, target))

    elif repr_name in ('список дуг', 'упорядоченный список дуг'):
        # graph – список кортежей (u, v)
        for u, v in graph:
            if u == vertex:
                result.append((u, v))

    else:
        raise ValueError(f"Неизвестное представление: {repr_name}")

    return result


# тест
if __name__ == '__main__':
    # Подготовим один и тот же граф в разных представлениях
    V = 4
    arcs = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 0)]

    # Матрица смежности
    adj_mat = [[0]*V for _ in range(V)]
    for u,v in arcs: adj_mat[u][v] = 1

    # Матрица инцидентности
    sorted_arcs = sorted(arcs)
    inc_mat = [[0]*len(sorted_arcs) for _ in range(V)]
    for col, (u,v) in enumerate(sorted_arcs):
        inc_mat[u][col] = -1
        inc_mat[v][col] = 1

    # Список смежности
    adj_list = {i: [] for i in range(V)}
    for u,v in sorted_arcs: adj_list[u].append(v)

    # Списки дуг
    arc_list = list(arcs)
    sorted_arc_list = sorted(arcs)

    # Проверим для вершины 0
    test_vertex = 0
    for name, gr in [
        ('матрица смежности', adj_mat),
        ('матрица инцидентности', inc_mat),
        ('список смежности', adj_list),
        ('список дуг', arc_list),
        ('упорядоченный список дуг', sorted_arc_list)
    ]:
        print(f"{name}: {outgoing_arcs(gr, name, test_vertex)}")
