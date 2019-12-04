import util
from typing import Optional, List


class Cracker(object):
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def permute(self, left: int, depth: int) -> Optional[List[str]]:
        perms = []
        for i in range(left, 10):
            c = str(i)

            if depth < len(self.lower) - 1:
                sub = self.permute(i, depth + 1)
                if sub is None:
                    continue
                perms += list(c + v for v in sub if i <= int(v[0]))
            else:
                perms.append(c)
        if depth == 0:
            lower = int(self.lower)
            upper = int(self.upper)

            return list(v for v in perms if lower <= int(v) <= upper)
        else:
            return perms


def part1(perms):
    good = 0
    for perm in perms:
        for i in range(0, len(perm) - 1):
            if perm[i] == perm[i + 1]:
                good += 1
                break

    util.Answer(1, good)


def part2(perms):
    good = 0
    for perm in perms:
        for i in range(10):
            c = str(i)
            if c not in perm:
                continue
            count = 0
            for i in range(len(perm)):
                if perm[i] == c:
                    count += 1
            if count == 2:
                good += 1
                break

    util.Answer(2, good)


if __name__ == "__main__":
    # print(Cracker("173", "578").permute(0, 0))

    data = util.ReadPuzzle()
    data = data[0].split("-")

    perms = Cracker(data[0], data[1]).permute(2, 0)

    part1(perms)
    part2(perms)
