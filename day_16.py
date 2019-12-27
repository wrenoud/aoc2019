import util
import math
import time

def multpattern(repeat):
    while True:
        for i in range(repeat):
            yield 0
        for i in range(repeat):
            yield 1
        for i in range(repeat):
            yield 0
        for i in range(repeat):
            yield -1


def fft(message, offset):
    count = len(message)
    for r in range(100):
        output = []
        for outputindex in range(count):
            pattern = multpattern(outputindex + 1)
            next(pattern) # skip first in pattern
            output.append(abs(sum(val * next(pattern) for val in message)) % 10)

        message = output
        print("Completed:", r)
    return message[offset:offset+8]

def part1(data):
    start = time.clock()
    util.Answer(1, "".join(str(v) for v in fft(data, 0)))
    print("Duration:", time.clock() - start)
        
def part2(data):
    offset = int("".join(str(v) for v in data[:7]))
    message = []
    for i in range(10000):
        message += data
    print("Started 2")
    util.Answer(2, fft(message, offset))


if __name__ == "__main__":
    data = util.ReadPuzzle()
    #data = ["80871224585914546619083218645595"] # 24176176
    #data = ["12345678"]
    puzzle = []
    for ch in data[0]:
        puzzle.append(int(ch))

    part1(puzzle)
    part2(puzzle)
