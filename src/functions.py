import json
import datetime
import os
from config import ROOT_DIR


file_path = os.path.join(ROOT_DIR, 'data', 'operations.json')


def get_json_file(file_json):
    """ забираем json файл из папки, по path, который задан через ROOT_DIR"""
    with open(file_json, 'r', encoding='utf-8') as file:
        file_read = file.read()
        json_content = json.loads(file_read)
        return json_content


def filtered_lines(list_of_json):
    """Выбираем только EXECUTED операции """

    filter_executed_rows = []
    for item in list_of_json[::-1]:
        if item.get("state") == "EXECUTED":
            filter_executed_rows.append(item)
    return filter_executed_rows


def sorted_datetime_toprows(dict_to_filter, top_rows_to_filter):
    """Последние top_rows_to_filter выполненных (EXECUTED) операций срезом"""
    top_rows = int(top_rows_to_filter)
    result = sorted(dict_to_filter, key=lambda operation: operation["date"], reverse=True)
    top5_result = result[:top_rows]
    # json_view = json.dumps(top5_result, indent=4)
    # print(json_view)
    return top5_result


def date_convert(transaction_row_dict):
    date_from_str = datetime.datetime.strptime(transaction_row_dict.get("date"), '%Y-%m-%dT%H:%M:%S.%f')
    date_format = date_from_str.strftime("%d-%m-%Y")
    return date_format


def hide_numbers(transaction_from_to):
    """Счет 43241152692663622869"""
    if transaction_from_to is None:
        return "Не определено"
    elif str(transaction_from_to).lower().startswith("счет"):
        """ Если это счет, возвращаем последние 4 цифры"""
        return f"Счет **{transaction_from_to[-4::]}"
    else:
        """ Если это НЕ счет, то подразумеваем карта и разбиваем номер по 4 цифры и скрываем"""
        # full_code = ','.join(str(transaction_from_to).split(' '))
        card_number = str(transaction_from_to).split(' ')
        hidden_number = ""
        count = 0
        for number in card_number[-1]:
            count += 1
            if count in [5, 13]:
                hidden_number += ' ' + number
            elif count in [9]:
                hidden_number += ' *'
            elif count in [1, 2, 3, 4, 5, 6, 13, 14, 15, 16]:
                hidden_number += number
            else:
                hidden_number += "*"
        # card_text = " ".join(card_number[:-1:])
        # {card_number[-1]} # ' '.join(card_number[:-1:])
        return f"{" ".join(card_number[:-1:])} {hidden_number}"


def result_transactions(transaction_list):
    for row in transaction_list:
        # print(row)
        print(f"\n{date_convert(row)} {row.get("description")}"
              f"\n{hide_numbers(row.get("from"))} -> {hide_numbers(row.get("to"))}"
              f"\n{row.get("operationAmount").get("amount")} {row.get("operationAmount").get("currency").get("name")}")


if __name__ == '__main__':
    content_to_filter = get_json_file(file_path)
    filtered_array = filtered_lines(content_to_filter)
    filtered_top5rows = sorted_datetime_toprows(filtered_array, 5)
    row_ = result_transactions(filtered_top5rows)
    print(row_)