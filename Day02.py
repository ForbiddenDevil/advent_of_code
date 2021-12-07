def part1(arr):
    horizontal, vertical = 0, 0
    for cmd, val in arr:
        if cmd == 'forward':
            horizontal += val
            continue
        if cmd == 'down':
            vertical += val
            continue
        if cmd == 'up':
            vertical -= val
            continue
    print(horizontal*vertical)

def part2(arr):
    horizontal, vertical, aim = 0, 0, 0
    for cmd, val in arr:
        if cmd == 'forward':
            horizontal += val
            vertical += aim * val
            continue
        if cmd == 'down':
            aim += val
            continue
        if cmd == 'up':
            aim -= val
            continue
    print(horizontal*vertical)

def main():
    commands = []
    for item in open('./Day02.txt', 'r').readlines():
        item = item.split(" ")
        commands.append((item[0], int(item[1])))

    # Part 1
    part1(commands)

    # Part 2
    part2(commands)

if __name__ == "__main__":
    main()