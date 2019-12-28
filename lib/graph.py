from lib import Coord


class Node(object):
    def __init__(self, position: Coord, value):
        self.position = position
        self.value = value
        self.neighbors = []

    def find_neighbor(self, node):
        for neighbor in self.neighbors:
            if neighbor.node == node:
                return neighbor
        return None

    def remove_neighbor(self, node):
        for i in range(len(self.neighbors)):
            if self.neighbors[i].node == node:
                del self.neighbors[i]
                break

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)

    def __repr__(self):
        return f"Node('{self.value}', {self.position}, {self.neighbors})"


class Neighbor(object):
    def __init__(self, node: Node, distance: int):
        self.distance = distance
        self.node = node

    def __repr__(self):
        return f"Neighbor('{self.node.value}', {self.distance})"


class Path(object):
    def __init__(self, start: Node):
        self.path = [
            start,
        ]
        self.distance = 0

    def append(self, neighbor: Neighbor):
        self.path.append(neighbor.node)
        self.distance += neighbor.distance

    @property
    def end(self):
        return self.path[-1]

    def __copy__(self):
        newone = Path(self.path[0])
        newone.distance = self.distance
        newone.path += self.path[1:]
        return newone

    def __contains__(self, other):
        return other in self.path

    def __len__(self):
        return self.distance

    def __repr__(self):
        nodes = "\n\t".join(str(v) for v in self.path)
        return f"Path({self.distance}:\n\t{nodes})\n"


def build_graph(maze, wall, space, trimdeadends):
    nodes = {}

    # build the graph
    for position, value in maze.iter():
        if value != wall:
            if position not in nodes:
                nodes[position] = Node(position, value)
            neighbors = maze.adjacent(position, exclude=[wall,])
            for neighbor_position, neighbor_value in neighbors:
                if neighbor_position not in nodes:
                    nodes[neighbor_position] = Node(neighbor_position, neighbor_value)
                nodes[position].neighbors.append(Neighbor(nodes[neighbor_position], 1))

    def trim_deadend(deadend: Node):
        neighbor = deadend.neighbors[0].node
        neighbor.remove_neighbor(node)
        if deadend.position in nodes:
            del nodes[deadend.position]
        if len(neighbor.neighbors) == 1:
            trim_deadend(neighbor)

    # trim deadends
    if trimdeadends:
        nodevalues = list(nodes.values())
        for node in nodevalues:
            if node.value == space:
                if len(node.neighbors) == 1:
                    trim_deadend(node)

    # remove straight through paths
    nodevalues = list(nodes.values())
    for node in nodevalues:
        if node.value == space:
            if len(node.neighbors) == 2:
                left = node.neighbors[0]
                right = node.neighbors[1]

                otherleft = left.node.find_neighbor(node)
                otherright = right.node.find_neighbor(node)

                otherleft.node = right.node
                otherleft.distance += right.distance

                otherright.node = left.node
                otherright.distance += left.distance

                del nodes[node.position]

    return nodes
