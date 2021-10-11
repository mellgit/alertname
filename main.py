import yaml
import json
import os
import re
# from pprint import pprint


def main():
    # чтение списка с названиями файлов
    with open('filename.txt') as file:
        ln = file.readlines()

    # формирование списка с названиями файлов
    path_file_rules = []
    for i in range(len(ln)):
        path_file_rules.append(re.sub("^\s+|\n|\r|\s+$", '', ln[i]))
    
    # чтение содержимого json файла
    with open('alertname.json') as file1:
        temp = json.load(file1)

    temp['templating']['list'][3]['query'] = string_alertname(path_file_rules)

    # pprint(string_alertname(path_file_rules))

    with open('alertname.json', 'w') as file2:
        json.dump(temp, file2, skipkeys=False, ensure_ascii=False)



# возвращает строку с именами alert`ов через запятую
def string_alertname(path_file_rules):

    # список строк
    alert_str_list = []

    # открытие всех rules файлов, в папке alerts
    for j in range(len(path_file_rules)):
        with open(path_file_rules[j]) as file:
            templates = yaml.safe_load(file)

        # путь до ключа 'alert'
        main_keys = templates['groups'][0]['rules']

        # список alertname в i-том файле
        ln = [main_keys[i]['alert'] for i in range(len(main_keys))]

        # создание строки из списк и добавление i-го списока в главный список
        alert_str_list.append(', '.join(ln))

    return ', '.join(alert_str_list)


if __name__ == '__main__':
    main()

# def write_filename_to_file():

#     directory = f'{os.getcwd()}/alerts'

#     file_lists = os.listdir(directory)

#     path_file_rules = [
#         f"alerts/{file_lists[i]}" for i in range(len(file_lists))]
    
    
#     with open('filename.txt', 'w') as file:
#         for i in range(len(path_file_rules)):
#             file.write(path_file_rules[i])
#             file.write('\n')