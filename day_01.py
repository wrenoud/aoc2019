import util


def FuelRequired(mass):
    return int(mass / 3) - 2


def part1(data):
    assert FuelRequired(100756) == 33583
    util.Answer(1, sum(FuelRequired(mass) for mass in data))


def TotalFuel(mass):
    total = 0
    fuel = FuelRequired(mass)
    while fuel > 0:
        total += fuel
        fuel = FuelRequired(fuel)
    return total


def part2(data):
    assert TotalFuel(100756) == 50346
    util.Answer(2, sum(TotalFuel(mass) for mass in data))


if __name__ == "__main__":
    data = util.ReadPuzzle()

    data = list(int(v) for v in data)

    part1(data)
    part2(data)
