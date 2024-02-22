import sys
import math

def read_circle_data(file_path):
    try:
        with open(file_path, 'r') as file:
            x, y = map(float, file.readline().split())
            radius = float(file.readline())
        return x, y, radius
    except FileNotFoundError:
        print(f"Файл не верно введет - {file_path}")
        sys.exit(1)
    except ValueError:
        print(f"Неверные данные в файле - {file_path}")
        sys.exit(1)

def read_dots(file_path):
    try:
        with open(file_path, 'r') as file:
            dots = [tuple(map(float, line.split())) for line in file.readlines()]
        return dots
    except FileNotFoundError:
        print(f"Файл не верно введет - {file_path}")
        sys.exit(1)
    except ValueError:
        print(f"Неверные данные в файле - {file_path}")
        sys.exit(1)

def get_file_path(prompt):
    while True:
        file_path = input(prompt)
        try:
            with open(file_path, 'r'):
                return file_path
        except FileNotFoundError:
            print(f"Файл не верно введет - {file_path}")
        except PermissionError:
            print(f"Отказано в разрешении на доступ к файлу - {file_path}")

def dot_position_relative_to_circle(dot, circle):
    x, y, radius = circle
    distance = math.sqrt((dot[0] - x)**2 + (dot[1] - y)**2)
    
    if distance == radius:
        return 0  
    elif distance < radius:
        return 1  
    else:
        return 2 

def main():
    if len(sys.argv) != 3:
        print("Пример команды через комадной строки python task2.py circle.txt dot.txt")
        circle_file_path = get_file_path("Введите путь к файлу circle.txt: ")
        dots_file_path = get_file_path("Введите путь к файлу dot.txt: ")
    else:
        circle_file_path = sys.argv[1]
        dots_file_path = sys.argv[2]

    circle_data = read_circle_data(circle_file_path)
    dots = read_dots(dots_file_path)

    for dot in dots:
        position = dot_position_relative_to_circle(dot, circle_data)
        print(position)

if __name__ == "__main__":
    main()
