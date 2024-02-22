import sys

def main():
    
    if len(sys.argv) != 3:
        print("Пример команды через комадной строки python task1.py 4 3")
        n = int(input("n = "))
        m = int(input("m = "))
    else:
        n = int(sys.argv[1])
        m = int(sys.argv[2])

    i = 1
    path = []

    while True:
        path.append(i)
        i = 1 + (i + m - 2) % n
        if i == 1:
            break

    result_path = ''.join(map(str, path))
    print(result_path)


if __name__ == "__main__":
    main()
    
