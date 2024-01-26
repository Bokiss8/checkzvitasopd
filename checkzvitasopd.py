import os


def check_file(file_path, output_file_path, filename):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Добавьте переменную для отслеживания наличия ошибок в текущем файле
    # Новая переменная для отслеживания ошибок в текущем файле
    file_errors_found = False

    # Проверка условий 1-5
    headers = ["Банк", "Пошта", "Інтернатні установи", "Інші установи", "Всього (рядки 1+2+3+4)"]
    for i in range(5):
        elements = lines[i].strip().split(';')
        # print(elements)
        if elements[1] != headers[i]:
            error_message = f"В файлі {filename} в шаблоні структури {i+1}-й строці невідповідність."
            print(error_message)
            output_file_path.write(error_message + '\n')
            file_errors_found = True

    # Проверка условия 6
    elements_5th_line = lines[4].strip().split(';')
    if elements_5th_line[2] != elements_5th_line[29] or elements_5th_line[2] != elements_5th_line[31]:
        error_message = f"В файлі {filename} в 5 строці (кількість людей) в 1 колонці неспівпада з 28 або 30."
        print(error_message)
        output_file_path.write(error_message + '\n')
        file_errors_found = True
        # print(f"3 элемент {elements_5th_line[2]} не 29 {elements_5th_line[29]} and 31 {elements_5th_line[31]}")

    # Проверка условия 7
    if elements_5th_line[3] != elements_5th_line[32]:
        error_message = f"В файлі {filename} в 5 строці (члени родини) в 2 колонці неспівпада з 31."
        print(error_message)
        output_file_path.write(error_message + '\n')
        file_errors_found = True
        # print(f"4 элемент {elements_5th_line[3]} несоответ 32 {elements_5th_line[32]}")

    # Проверка условия 8
    if elements_5th_line[4] != elements_5th_line[30] or elements_5th_line[4] != elements_5th_line[33]:
        error_message = f"В файлі {filename} в 5 строці (сума) в 3 колонці неспівпада з 29 або 32."
        print(error_message)
        output_file_path.write(error_message + '\n')
        file_errors_found = True
        # print(f"5 элемент {elements_5th_line[4]} не 30 {elements_5th_line[30]} and 33 {elements_5th_line[33]}")

    # Вернуть True, если обнаружены ошибки, иначе False

    return file_errors_found


def main():
    directory_path = r"D:\time_export"
    csv_files = [filename for filename in os.listdir(directory_path) if filename.lower().endswith(".csv")]

    if not csv_files:
        print("Нема файлів CSV у вказаному каталозі.")
        return  # Выход из функции, так как нет файлов для проверки

    output_file_path = os.path.join(directory_path, "error_log_zvit_asopd.txt")

    all_files_valid = True  # Переменная для отслеживания общей корректности всех файлов
    # Открываем файл для записи ошибок
    with open(output_file_path, 'w') as output_file:
        for filename in csv_files:
            file_path = os.path.join(directory_path, filename)
            file_errors_found = check_file(file_path, output_file, filename)

            # Обновление флага общей корректности всех файлов
            all_files_valid = all_files_valid and not file_errors_found

            # Вывод сообщения, если ошибок не обнаружено в текущем файле
            # if not file_errors_found:
            #     print(f"В файлі {filename} помилок не знайдено.")
            #
            # if file_errors_found:
            #     print(f"В файлі {filename} знайдено помилки.")

    # Вывод сообщения, если ошибок не обнаружено
    if all_files_valid:
        print("Всі файли успішно перевірені. Помилок не знайдено.")


if __name__ == "__main__":
    main()
