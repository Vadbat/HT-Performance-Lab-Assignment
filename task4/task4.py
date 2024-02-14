import sys

def min_moves(nums):
    target = sum(nums) // len(nums)  # Целевое значение, к которому стремимся
    moves = 0

    for num in nums:
        moves += abs(num - target)

    return moves

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            nums = [int(line.strip()) for line in file]
        return nums
    except FileNotFoundError:
        print("Ошибка: Файл не найден.")
        sys.exit(1)
    except ValueError:
        print("Ошибка: Файл содержит некорректные данные. Пожалуйста, убедитесь, что в файле числа.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python script.py author.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    nums = read_file(file_path)

    if not nums:
        print("Ошибка: Файл не содержит чисел.")
        sys.exit(1)

    result = min_moves(nums)

    print("Минимальное количество ходов:", result)
