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
        if "_ok" in filename:
            error_message = (f"ок(підтверджено) - В файлі {filename} в 5 строці (кількість людей) в 1 колонці "
                             f"неспівпада з 28 або 30.")
        else:
            error_message = f"В файлі {filename} в 5 строці (кількість людей) в 1 колонці неспівпада з 28 або 30."
        print(error_message)
        output_file_path.write(error_message + '\n')
        file_errors_found = True
        # print(f"3 элемент {elements_5th_line[2]} не 29 {elements_5th_line[29]} and 31 {elements_5th_line[31]}")

    # Проверка условия 7
    if elements_5th_line[3] != elements_5th_line[32]:
        if "_ok" in filename:
            error_message = (f"ок(підтверджено) - В файлі {filename} в 5 строці (члени родини) в 2 колонці "
                             f"неспівпада з 31.")
        else:
            error_message = f"В файлі {filename} в 5 строці (члени родини) в 2 колонці неспівпада з 31."
        print(error_message)
        output_file_path.write(error_message + '\n')
        file_errors_found = True
        # print(f"4 элемент {elements_5th_line[3]} несоответ 32 {elements_5th_line[32]}")

    # Проверка условия 8
    if elements_5th_line[4] != elements_5th_line[30] or elements_5th_line[4] != elements_5th_line[33]:
        if "_ok" in filename:
            error_message = (f"ок(підтверджено) - В файлі {filename} в 5 строці (сума) в 3 колонці неспівпада з 29 або"
                             f" 32.")
        else:
            error_message = f"В файлі {filename} в 5 строці (сума) в 3 колонці неспівпада з 29 або 32."
        # Проверка
        print(error_message)
        output_file_path.write(error_message + '\n')
        file_errors_found = True
        # print(f"5 элемент {elements_5th_line[4]} не 30 {elements_5th_line[30]} and 33 {elements_5th_line[33]}")

    # Проверка условия 9
    sum_of_elements_5_6_7 = round(
        float(elements_5th_line[5]) + float(elements_5th_line[6]) + float(elements_5th_line[7]), 2)
    # Преобразование sum_of_elements_5_6_7 в строку с двумя знаками после запятой
    sum_of_elements_5_6_7_str = "{:.2f}".format(sum_of_elements_5_6_7)
    # print(f"elements_5th_line[4] {elements_5th_line[4]} = sum_of_elements_5_6_7_str {sum_of_elements_5_6_7_str}")
    # Вывод типов элементов
    # print(f"Тип elements_5th_line[4]: {type(elements_5th_line[4])}")
    # print(f"Тип sum_of_elements_5_6_7: {type(sum_of_elements_5_6_7)}")
    if elements_5th_line[4] != sum_of_elements_5_6_7_str:
        error_message = f"В файлі {filename} в 5 строці (сума 4+5+6) в 3 колонці не дорівнює сумі колонок 4+5+6."
        print(error_message)
        output_file_path.write(error_message + '\n')
        file_errors_found = True

    # Проверка условия 10
    minus_of_elements_14_17 = round(float(elements_5th_line[14]) - float(elements_5th_line[17]), 2)
    minus_of_elements_14_17_str = "{:.2f}".format(minus_of_elements_14_17)
    if elements_5th_line[20] != minus_of_elements_14_17_str:
        error_message = f"В файлі {filename} в 5 строці (сума 13-16) в 19 колонці не дорівнює різниці колонок 13-16."
        print(error_message)
        output_file_path.write(error_message + '\n')
        file_errors_found = True

    # Проверка условия 11
    minus_of_elements_15_18 = round(float(elements_5th_line[15]) - float(elements_5th_line[18]), 2)
    minus_of_elements_15_18_str = "{:.2f}".format(minus_of_elements_15_18)
    if elements_5th_line[21] != minus_of_elements_15_18_str:
        error_message = f"В файлі {filename} в 5 строці (сума 14-17) в 20 колонці не дорівнює різниці колонок 14-17."
        print(error_message)
        output_file_path.write(error_message + '\n')
        file_errors_found = True

    # Проверка условия 12
    minus_of_elements_16_19 = round(float(elements_5th_line[16]) - float(elements_5th_line[19]), 2)
    minus_of_elements_16_19_str = "{:.2f}".format(minus_of_elements_16_19)
    if elements_5th_line[22] != minus_of_elements_16_19_str:
        error_message = f"В файлі {filename} в 5 строці (сума 15-18) в 21 колонці не дорівнює різниці колонок 15-18."
        print(error_message)
        output_file_path.write(error_message + '\n')
        file_errors_found = True

    # Проверка условия 13
    narah_3 = round(float(elements_5th_line[4]), 2)
    vuplata_32 = round(float(elements_5th_line[33]), 2)
    if narah_3 < vuplata_32:
        error_message = (f"В файлі {filename} в 5 строці (сума 3<32) в 3 колонці сума нарахування менша ніж в 32 "
                         f"сума виплати.")
        # Проверка
        print(error_message)
        output_file_path.write(error_message + '\n')
        file_errors_found = True
        # print(f"5 элемент {narah_3} < {vuplata_32}")

    # Вернуть True, если обнаружены ошибки, иначе False

    return file_errors_found


def main():
    directory_path = r"F:\time_export"
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
