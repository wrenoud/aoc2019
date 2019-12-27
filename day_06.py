import util


class OrbitalObject(object):
    def __init__(self, id):
        self.id = id
        self.parent = None

    @property
    def orbits(self):
        if self.parent == None:
            return 0
        return self.parent.orbits + 1

    def orbitchain(self):
        if self.parent == None:
            return []
        return [self.id,] + self.parent.orbitchain()


def part1(objects):
    util.Answer(1, sum(obj.orbits for obj in objects.values()))


def part2(objects):
    you = objects["YOU"].orbitchain()
    san = objects["SAN"].orbitchain()

    santa = 0
    for i, obj in enumerate(you[2:]):
        try:
            santa = san.index(obj)
            print(i)
            break
        except:
            continue

    util.Answer(2, santa + i)


if __name__ == "__main__":
    data = util.ReadPuzzle()
    # data = ["COM)B","B)C","C)D","D)E","E)F","B)G","G)H","D)I","E)J","J)K","K)L","K)YOU","I)SAN",]

    data = list(orbit.split(")") for orbit in data)

    objects = {}

    for major, minor in data:
        if major not in objects:
            objects[major] = OrbitalObject(major)
        if minor not in objects:
            objects[minor] = OrbitalObject(minor)

        objects[minor].parent = objects[major]

    part1(objects)
    part2(objects)
