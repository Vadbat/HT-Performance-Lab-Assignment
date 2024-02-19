def main():
    n = int(input('n = '))
    m = int(input('m = '))

    i = 1
    path = []

    while True:
        path.append(i)
        i = 1 + (i + m - 2) % n
        if i == 1:
            break

    circular_array = ''.join(map(str, range(1, n + 1)))
    print(f"Круговой массив: {circular_array}.")

    result_path = ''.join(map(str, path))
    print(f"Путь: {result_path}")


if __name__ == "__main__":
    main()
