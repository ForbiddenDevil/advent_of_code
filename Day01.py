def main():
    count, prev = -1, 0
    for num in list(map(int, open('./Day01.txt', 'r').readlines())):
        if num > prev:
            count += 1
        prev = num
    print(count)

if __name__ == "__main__":
    main()