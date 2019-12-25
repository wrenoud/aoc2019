import util


def separate_layers(data, width, height):
    layers = []
    offset = 0
    length = width * height
    while offset < len(data):
        layers.append(data[offset:offset+length])
        offset += length
    return layers


def part1(data):
    layers = separate_layers(data,25,6)
    
    values = {}

    for layer in layers:
        values[layer.count('0')] = layer.count('1') * layer.count('2')

    util.Answer(1, values[min(values.keys())])

        
def part2(data):
    layers = separate_layers(data,25,6)

    image = ['2'] * (25*6)
    for layer in layers:
        for i in range(25*6):
            if layer[i] == '0':
                if image[i] == '2':
                    image[i] = ' '
            elif layer[i] == '1':
                if image[i] == '2':
                    image[i] = '#'

    util.Answer(2, None)

    print("-"*25)
    for offset in range(0, 25*6, 25):
        print("".join(image[offset:offset+25]))
    print("-"*25)


if __name__ == "__main__":
    data = util.ReadPuzzle()[0]
    part1(data)
    part2(data)
