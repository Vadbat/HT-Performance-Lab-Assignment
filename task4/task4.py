import os
import sys

def min_moves(nums):
    n = len(nums)
    nums.sort()

    median = nums[n // 2]

    moves = 0
    for num in nums:
        moves += abs(num - median)

    return moves

def get_file_path(prompt):
    while True:
        file_path = input(prompt)
        if file_path.lower() == 'exit':
            sys.exit(0)  # Exiting the script if the user wants to quit
        try:
            with open(file_path, 'r'):
                return file_path
        except FileNotFoundError:
            print(f"Файл не верно введен - {file_path}")

def main():
    if len(sys.argv) != 2:
        print("Пример команды через комадной строки python task4.py numbers.txt")
        file_path = get_file_path("Введите путь к файлу numbers.txt (или введите 'exit' для выхода): ")
    else:
        file_path = sys.argv[1]
    

    try:
        with open(file_path, 'r') as file:
            nums = [int(line.strip()) for line in file]
            result = min_moves(nums)
            print(f"Минимальное количество ходов: {result}")
    except FileNotFoundError:
        print(f"Файл numbers.txt не найден по указанному пути.")

if __name__ == "__main__":
    main()
