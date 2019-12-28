import util
from copy import copy
from lib import Coord, Maze
from lib.graph import build_graph, Node, Path


def IsKey(value):
    return value == value.lower()


def IsDoor(value):
    return value == value.upper()


def add_or_replace_shortest_paths(newpaths, knownpaths):
    for newpath in newpaths:
        existed = False
        for i, path in enumerate(knownpaths):
            if newpath.end == path.end:
                existed = True
                if len(newpath) < len(path):
                    knownpaths[i] = newpath
                    break
        if not existed:
            knownpaths.append(newpath)


def find_keys(currentpath: Path, keychain):
    paths = []
    keys = []
    for neighbor in currentpath.end.neighbors:
        node = neighbor.node

        # skip checking backtracks
        if len(currentpath) > 2 and currentpath.path[-2] == node:
            continue

        if node not in currentpath:
            isClear = node.value in [".", "@"]
            isKey = not isClear and IsKey(node.value)
            isDoor = not isClear and IsDoor(node.value)
            haveKey = isKey and node.value in keychain
            haveKeyForDoor = isDoor and node.value.lower() in keychain

            if isClear or haveKey or haveKeyForDoor:  # open path
                newpath = copy(currentpath)
                newpath.append(neighbor)
                newpaths = find_keys(newpath, keychain)
                add_or_replace_shortest_paths(newpaths, paths)

            if isKey and node.value not in keychain:
                newpaths = [
                    copy(currentpath),
                ]
                newpaths[0].append(neighbor)
                add_or_replace_shortest_paths(newpaths, paths)

    return sorted(paths, key=len)


bestsolution = (None, None)


def getsolutions(start: Node, keychain=[], solution=0, totalkeys=0):
    global bestsolution
    solutions = []

    if len(keychain) == totalkeys:
        if bestsolution[1] is None or solution < bestsolution[1]:
            bestsolution = ("".join(keychain), solution)

        solutions.append(solution)
        print("".join(keychain), solution, bestsolution[1])
    else:
        print(
            f"Chain (best: {bestsolution[1]} {bestsolution[0]}): {solution}",
            "".join(keychain),
        )
        paths = find_keys(Path(start), keychain,)

        for path in paths:
            newsolution = solution + len(path)
            if bestsolution[1] is not None and newsolution >= bestsolution[1]:
                continue  # too long, skip

            node = path.end

            subkeys = copy(keychain)
            subkeys.append(node.value)

            solutions += getsolutions(node, subkeys, newsolution, totalkeys)

    return solutions


def part1(data):
    maze = Maze(data)

    nodes = build_graph(maze, "#", ".", True)

    # collect points of interest
    keys = {}
    doors = {}
    start = None
    for node in nodes.values():
        if node.value == "@":
            start = node.position
        elif node.value != ".":
            if IsKey(node.value):
                keys[node.value] = node.position
            elif IsDoor(node.value):
                doors[node.value] = node.position

    for node in nodes.values():
        print(node)

    keychain = []
    paths = find_keys(Path(nodes[start]), keychain)
    print("***", paths)
    # for path in paths:
    #     print(path.end.value, len(path))

    print("Solution")
    solutions = getsolutions(nodes[start], totalkeys=len(keys))

    util.Answer(1, min(solutions))


def part2(data):
    util.Answer(2, None)


if __name__ == "__main__":
    data = util.ReadPuzzle()

    # data = [
    #     "########################",
    #     "#f.D.E.e.C.b.A.@.a.B.c.#",
    #     "######################.#",
    #     "#d.....................#",
    #     "########################",
    # ]  # 86 steps

    # data = [
    #     "#########",
    #     "#b.A.@.a#",
    #     "#########",
    # ]  # 8 steps

    # data = [
    #    "#################",
    #    "#i.G..c...e..H.p#",
    #    "########.########",
    #    "#j.A..b...f..D.o#",
    #    "########@########",
    #    "#k.E..a...g..B.n#",
    #    "########.########",
    #    "#l.F..d...h..C.m#",
    #    "#################",
    # ]  # 136

    part1(data)
    part2(data)
