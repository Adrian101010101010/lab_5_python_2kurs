# pylint: skip-file
from collections import defaultdict, deque
from itertools import chain


def topological_sort(graph):
    depending = defaultdict(int)
    neighbor = list(chain.from_iterable(graph.values()))

    for neighbor in neighbor:
        depending[neighbor] += 1

    queue = deque(node for node in graph if depending[node] == 0)
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            depending[neighbor] -= 1
            if depending[neighbor] == 0:
                queue.append(neighbor)

    return result


def optimal_order(input_data):
    graph = defaultdict(list)

    for line in input_data:
        current, prerequisite = line.split()
        graph[prerequisite].append(current)

    result = topological_sort(graph)

    return result


with open('../../govern.in', 'r') as file:
    input_data = file.read().strip().split('\n')

result = optimal_order(input_data)

with open('../../govern.out', 'w') as file:
    file.write('\n'.join(result) + '\n')
