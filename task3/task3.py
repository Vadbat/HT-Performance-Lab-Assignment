import json
import os

def fill_values(tests, values):
    for test in tests:
        test_id = test["id"]
        for value in values["values"]:
            if value["id"] == test_id:
                test["value"] = value["value"]
            elif "values" in test:
                fill_values(test["values"], values)

def main():
    # Полные пути к файлам
    script_path = os.path.dirname(os.path.abspath(__file__))
    values_path = os.path.join(script_path, 'values.json')
    tests_path = os.path.join(script_path, 'tests.json')
    report_path = os.path.join(script_path, 'report.json')

    # Загрузка данных из файлов
    with open(values_path, 'r') as values_file:
        values = json.load(values_file)

    with open(tests_path, 'r') as tests_file:
        tests = json.load(tests_file)

    # Заполнение значений в структуре tests.json
    fill_values(tests["tests"], values)

    # Запись результата в файл report.json
    with open(report_path, 'w') as report_file:
        json.dump(tests, report_file, indent=2)

    print("Программа завершена. Результат записан в файл report.json.")

if __name__ == "__main__":
    main()
