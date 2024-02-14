import json

def fill_values(tests, values):
    for test in tests:
        test_id = test["id"]
        for value in values["values"]:
            if value["id"] == test_id:
                test["value"] = value["value"]
            elif "values" in test:
                fill_values(test["values"], values)

def main(values_path, tests_path, report_path):
    try:
        with open(values_path, 'r') as values_file:
            values = json.load(values_file)

        with open(tests_path, 'r') as tests_file:
            tests = json.load(tests_file)

        fill_values(tests["tests"], values)

        with open(report_path, 'w') as report_file:
            json.dump(tests, report_file, indent=2)
        
        print("Успешно создан файл report.json.")

    except FileNotFoundError:
        print("Ошибка: Один из файлов не найден.")
    except json.JSONDecodeError:
        print("Ошибка: Некорректный формат JSON в одном из файлов.")

if __name__ == "__main__":
    try:
        values_path = input("Введите путь к файлу values.json: ")
        tests_path = input("Введите путь к файлу tests.json: ")
        report_path = input("Введите путь к файлу report.json: ")

        main(values_path, tests_path, report_path)

    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем.")
