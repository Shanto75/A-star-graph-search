# graph = {'s': ['a', 'g'], 'a': ['b', 'c'], 'b': ['d'], 'c': ['d', 'g'], 'd': ['g']}
extend_f = {}
closed_set = []
start = 's'
extend = start
goal = 'g'
nodes = {'s': ['a', 'g'], 'a': ['b', 'c'], 'b': ['d'], 'c': ['d', 'g'], 'd': ['g'], }
path_cost = {'s': {'a': 1, 'g': 12}, 'a': {'b': 3, 'c': 1}, 'b': {'d': 3}, 'c': {'d': 1, 'g': 2}, 'd': {'g': 3}}
h_value = {'s': 75, 'a': 76, 'b': 80, 'c': 93, 'd': 81, 'g': 8}
temp = []
graph = []
count = 0
i = 0
j = 1
min_g = 0
min_f = 9999
node_index = {}
path = []


class Op:

    def __init__(self, node):
        self.name = node
        self.g = 0
        self.h = h_value[node]
        self.f = self.g + self.h


class Leaf:

    def __init__(self):
        self.name = nodes[extend][i]
        self.prev = count
        self.pg = graph[count].g
        self.g = self.pg+path_cost[extend][nodes[extend][i]]
        self.h = h_value[self.name]
        self.f = self.g + self.h
        extend_f[self.name] = self.f
        node_index[self.name] = j


if __name__ == '__main__':
    extend_f[extend] = h_value[extend]
    graph.append(Op(extend))
    node_index[extend] = 0
    while extend_f:
        i = 0
        if extend not in closed_set:
            for i in range(len(nodes[extend])):
                graph.append(Leaf())
                if graph[j].name == goal:
                    if min_f > graph[j].f:
                        min_f = graph[j].f
                        min_g = j
                    extend_f.pop(goal)
                j += 1
        closed_set.append(extend)
        extend_f.pop(extend)
        if extend_f:
            temp = list(extend_f.values()).index(min(list(extend_f.values())))
            extend = list(extend_f.keys())[temp]
            count = node_index[extend]


print('F: ', graph[min_g].f)
while 1:
    path.append(graph[min_g].name)
    min_g = graph[min_g].prev
    if graph[min_g].name == start:
        path.append(graph[min_g].name)
        break
path.reverse()
print('Optimal Path: ', '->'.join(path))
