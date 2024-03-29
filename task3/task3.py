import json
import os
import sys

def fill_values(tests, values):
    for test in tests:
        test_id = test["id"]
        for value in values["values"]:
            if value["id"] == test_id:
                test["value"] = value["value"]
            elif "values" in test:
                fill_values(test["values"], values)

def get_file_path(prompt):
    file_path = input(prompt)
    return os.path.abspath(file_path)

def main():
    if len(sys.argv) != 4:
        print("Пример команды через комадной строки python task3.py values.json tests.json report.json")
        values_path = get_file_path("Введите путь к файлу values.json: ")
        tests_path = get_file_path("Введите путь к файлу tests.json: ")
        report_path = get_file_path("Введите путь к файлу report.json: ")
    else:
        values_path = sys.argv[1]
        tests_path = sys.argv[2]
        report_path = sys.argv[3]

    

    if not os.path.exists(values_path):
        print(f"Файл {values_path} не найден.")
        return

    if not os.path.exists(tests_path):
        print(f"Файл {tests_path} не найден.")
        return

    with open(values_path, 'r') as values_file:
        values = json.load(values_file)

    with open(tests_path, 'r') as tests_file:
        tests = json.load(tests_file)

    fill_values(tests["tests"], values)

    with open(report_path, 'w') as report_file:
        json.dump(tests, report_file, indent=2)

    print("Программа завершена. Результат записан в файл report.json.")

if __name__ == "__main__":
    main()
