def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Пожалуйста, введите положительное значение.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

def print_circular_array(n):
    circular_array = ''.join(map(str, range(1, n + 1)))
    print(f"Круговой массив: {circular_array}.")

def main():
    n = get_positive_integer("Введите значение n: ")
    m = get_positive_integer("Введите значение m: ")

    i = 1
    path = []

    while True:
        path.append(i)
        i = 1 + (i + m - 2) % n
        if i == 1:
            break

    result_path = ''.join(map(str, path))
    print(f"Путь: {result_path}")

    print_circular_array(n)

if __name__ == "__main__":
    main()
