import os

def min_moves(nums):
    n = len(nums)
    nums.sort()

    median = nums[n // 2]

    moves = 0
    for num in nums:
        moves += abs(num - median)

    return moves

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "numbers.txt")

    try:
        with open(file_path, 'r') as file:
            nums = [int(line.strip()) for line in file]
            result = min_moves(nums)
            print(f"Минимальное количество ходов: {result}")
    except FileNotFoundError:
        print(f"Файл numbers.txt не найден в каталоге {script_dir}.")

if __name__ == "__main__":
    main()
