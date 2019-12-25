import util
from intcode import computer


def part1(data):
    stdout = computer.Run(data[:], 1, True)
    util.Answer(1, list(stdout)[-1])

        
def part2(data):
    stdout = computer.Run(data[:], 2, True)
    util.Answer(2, list(stdout)[-1])


if __name__ == "__main__":
    data = util.ReadPuzzle()
    #data = ["109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"] # duplicates program to output
    #data = ["1102,34915192,34915192,7,4,7,99,0"] # generates 16 digit number
    #data = ["104,1125899906842624,99"] # outputs large number
    data = list(int(v) for v in data[0].split(','))

    part1(data)
    part2(data)
