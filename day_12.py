import util
from lib import Coord3D
from copy import copy, deepcopy


class Moon(object):
    def __init__(self, x, y, z):
        self.position = Coord3D(x,y,z)
        self.velocity = Coord3D(0,0,0)

    @property
    def energy(self):
        return len(self.position) * len(self.velocity)
    
    def __eq__(self, other):
        return self.position == other.position and self.velocity == other.velocity

    def __repr__(self):
        return f"{self.__class__.__name__}(position: {self.position}, velocity: {self.velocity})"


class OrbitalSystem(object):
    def __init__(self, objects):
        self.time = 0
        self.objects = objects
        self._orig = deepcopy(objects)
        self.count = len(objects)
    
    @staticmethod
    def _update_velocity(left, right):
        for axis in ['x','y','z']:
            if left.position.__dict__[axis] < right.position.__dict__[axis]:
                left.velocity.__dict__[axis] += 1
                right.velocity.__dict__[axis] -= 1
            elif left.position.__dict__[axis] > right.position.__dict__[axis]:
                left.velocity.__dict__[axis] -= 1
                right.velocity.__dict__[axis] += 1   
            # else they are equal and do nothing

    def step(self):
        # update velocity for each pair
        for i in range(self.count - 1):
            for j in range(i + 1, self.count):
                self._update_velocity(self.objects[i], self.objects[j])

        # update object positions
        for obj in self.objects:
            obj.position += obj.velocity

        # advance time
        self.time += 1


def part1(moons):
    system = OrbitalSystem(moons)

    for timestep in range(1000):
        system.step()

    energy = 0
    for moon in moons:
        energy += moon.energy

    util.Answer(1, energy)

        
def part2(moons):
    system = OrbitalSystem(moons)

    # this is just to see the periods on each axis
    while True and system.time < 231615:
        system.step()

        for axis in ['x','y','z']:
            allequal = True
            for i in range(system.count):
                allequal &= system.objects[i].position.__dict__[axis] == system._orig[i].position.__dict__[axis]
            if allequal:
                print(axis, system.time)
        #print(system.time, system.objects[0].position.x, system.objects[0].position.y, system.objects[0].position.z)

        if system.time % 10000 == 0:
            pass #print(f"Time:{system.time:,}")

    print("periods: (x: 84032, y: 231614, z: 193052)")
    print("used a LCM (Least Common Multiple) calculator to find below")
    util.Answer(2, 469671086427712)


if __name__ == "__main__":
    data = util.ReadPuzzle()

    # test data
    #data = ["<x=-8, y=-10, z=0>","<x=5, y=5, z=10>","<x=2, y=-7, z=3>","<x=9, y=-8, z=-3>",]
    #data = ["<x=-1, y=0, z=2>","<x=2, y=-10, z=-7>","<x=4, y=-8, z=8>","<x=3, y=5, z=-1>",]
    
    moons = []
    for line in data:
        x,y,z = list(int(c.split('=')[1]) for c in line[1:-1].split(','))
        moons.append(Moon(x,y,z))

    part1(deepcopy(moons))
    part2(moons)
