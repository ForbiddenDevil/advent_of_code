def has_increased(arr):
    return sum(arr[:3]) < sum(arr[1:])

def main():
    # Part 1
    count, prev = -1, 0
    numbers = list(map(int, open('./Day01.txt', 'r').readlines()))
    for num in numbers:
        if num > prev:
            count += 1
        prev = num
    print(count)

    # Part 2
    count = 0
    for i in range(len(numbers)-3):
        if has_increased(numbers[i:i+4]):
            count += 1
    print(count)

if __name__ == "__main__":
    main()
