import util

from intcode import computer
import itertools


def stdin(phase, gen):
    yield phase
    for value in gen:
        yield value


def Amplify(program, phasesettings, inputvalue=0):
    stdout = (v for v in [0])

    for phase in phasesettings:
        stdout = computer.Run(program[:], stdin(phase, stdout))

    return list(stdout)[-1]


def AmplifyWithFeedback(program, phasesettings, inputvalue=0):
    feedback = [
        0,
    ]
    stdout = (v for v in feedback)

    for phase in phasesettings:
        stdout = computer.Run(program[:], stdin(phase, stdout))

    # pipe feedback to amplifier 1
    for value in stdout:
        feedback.append(value)

    return value


def part1(data):
    results = {}
    for test in itertools.permutations([0, 1, 2, 3, 4]):
        thrust = Amplify(data, test)
        results[thrust] = test
    maxthrust = max(results.keys())
    util.Answer(1, [maxthrust, results[maxthrust]])


def part2(data):
    results = {}
    for test in itertools.permutations([5, 6, 7, 8, 9]):
        thrust = AmplifyWithFeedback(data, test)
        results[thrust] = test
    maxthrust = max(results.keys())
    util.Answer(2, [maxthrust, results[maxthrust]])


if __name__ == "__main__":
    data = util.ReadPuzzle()
    # data = ["3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0",]
    # data = ["3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"]
    # data = ["3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"]
    # feedback examples
    # data = ["3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"]
    # data = ["3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"]
    data = list(int(v) for v in data[0].split(","))

    part1(data)
    part2(data)
