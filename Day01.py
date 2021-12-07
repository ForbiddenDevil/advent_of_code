def has_increased(arr):
    return sum(arr[:3]) < sum(arr[1:])

def part1(numbers):
    count, prev = -1, 0
    for num in numbers:
        if num > prev:
            count += 1
        prev = num
    print("Part1 answer: ", count)
    
def part2(numbers):
    count = 0
    for i in range(len(numbers)-3):
        if has_increased(numbers[i:i+4]):
            count += 1
    print("Part2, answer:", count)

def main():
    numbers = list(map(int, open('./Day01.txt', 'r').readlines()))
    
    # Part 1
    part1()

    # Part 2
    part2()

if __name__ == "__main__":
    main()
