"""
ПР6, Задание 4.
Функция перевода графа из одного представления в другое.
Аргументы: граф, начальное представление, требуемое представление
(кроме 'упорядоченный список дуг' в качестве целевого).
"""

def convert_graph(graph, from_repr, to_repr):
    if to_repr == 'упорядоченный список дуг':
        raise ValueError("Преобразование в упорядоченный список дуг не разрешено")

    arcs, n = _extract_arcs_and_vertices(graph, from_repr)

    if to_repr == 'матрица смежности':
        mat = [[0] * n for _ in range(n)]
        for u, v in arcs:
            mat[u][v] = 1
        return mat

    elif to_repr == 'матрица инцидентности':
        m = len(arcs)
        mat = [[0] * m for _ in range(n)]
        for col, (u, v) in enumerate(arcs):
            mat[u][col] = -1
            mat[v][col] = 1
        return mat

    elif to_repr == 'список смежности':
        adj = {i: [] for i in range(n)}
        for u, v in arcs:
            adj[u].append(v)
        for u in adj:
            adj[u].sort()
        return adj

    elif to_repr == 'список дуг':
        return list(arcs)   # дуги уже отсортированы для детерминизма

    else:
        raise ValueError(f"Неизвестное целевое представление: {to_repr}")


def _extract_arcs_and_vertices(graph, repr_name):
    if repr_name == 'матрица смежности':
        n = len(graph)
        arcs = []
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 1:
                    arcs.append((i, j))
        return sorted(arcs), n

    elif repr_name == 'матрица инцидентности':
        n = len(graph)
        if n == 0:
            return [], 0
        m = len(graph[0])
        arcs = []
        for col in range(m):
            source = target = None
            for row in range(n):
                if graph[row][col] == -1:
                    source = row
                elif graph[row][col] == 1:
                    target = row
            if source is not None and target is not None:
                arcs.append((source, target))
        return sorted(arcs), n

    elif repr_name == 'список смежности':
        if isinstance(graph, dict):
            vertices = list(graph.keys())
            n = max(vertices) + 1 if vertices else 0
            arcs = []
            for u in graph:
                for v in graph[u]:
                    arcs.append((u, v))
        else:  # список списков
            n = len(graph)
            arcs = []
            for u in range(n):
                for v in graph[u]:
                    arcs.append((u, v))
        return sorted(arcs), n

    elif repr_name in ('список дуг', 'упорядоченный список дуг'):
        arcs = list(graph)
        if not arcs:
            return [], 0
        n = max(max(u, v) for u, v in arcs) + 1
        return sorted(arcs), n

    else:
        raise ValueError(f"Неизвестное начальное представление: {repr_name}")


# тест
if __name__ == '__main__':
    # Исходный граф в виде матрицы смежности
    adj_mat = [
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0]
    ]

    print("Исходная матрица смежности:")
    for row in adj_mat: print(row)

    # Перевод в список смежности
    adj_list = convert_graph(adj_mat, 'матрица смежности', 'список смежности')
    print("\nСписок смежности:", adj_list)

    # Перевод обратно в матрицу инцидентности
    inc_mat = convert_graph(adj_list, 'список смежности', 'матрица инцидентности')
    print("\nМатрица инцидентности:")
    for row in inc_mat: print(row)

    # Перевод в список дуг
    arc_list = convert_graph(inc_mat, 'матрица инцидентности', 'список дуг')
    print("\nСписок дуг:", arc_list)
