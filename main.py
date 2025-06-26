import argparse
import csv
import re
from tabulate import tabulate

def where(where_str: str, products: list[dict]) -> list[dict]:
    '''
    :param where_str: настройка для фильрации по where
    :param products: список словарей, которые будут отфильтровываться
    :return: отфильтрованный список словарей

    Данная функция фильтрует список словарей по заданной настройке where
    '''
    where_conditions = re.split('[<>=]', where_str)
    where_col_name = where_conditions[0]
    where_meaning = where_conditions[1]
    where_comparison = re.search(r'[<>=]', where_str)
    if where_comparison: where_comparison = where_comparison.group()
    res = []

    match where_comparison:
        case '=':
            for row in products:
                if row[where_col_name] == where_meaning: res.append(dict(row))
        case '<':
            try:
                where_meaning = float(where_meaning)
            except ValueError:
                return [{' ': ['error']}]
            for row in products:
                if float(row[where_col_name]) < float(where_meaning): res.append(dict(row))
        case '>':
            try:
                where_meaning = float(where_meaning)
            except ValueError:
                return [{' ': ['error']}]
            for row in products:
                if float(row[where_col_name]) > float(where_meaning): res.append(dict(row))
    return res
def aggregate(aggregate_str: str, products: list[dict]) -> dict[str : list]:
    '''
    :param aggregate_str: настройка для аггрегации по aggregate
    :param products: список словарей, которые будут агрегироваться
    :return: агрегированный словарь

    Данная функция агрегирует список словарей по заданной настройке aggregate
    '''
    aggregate_conditions = aggregate_str.split('=', 1)
    aggregate_col_name = aggregate_conditions[0]
    aggregate_meaning = aggregate_conditions[1]
    res = {}
    if aggregate_conditions:

        match aggregate_meaning:
            case 'avg':
                avg_res = 0
                counter = 0
                for row in products:
                    try:
                        float(row[aggregate_col_name])
                    except ValueError:
                        return {' ': ['error']}
                    avg_res += float(row[aggregate_col_name])
                    counter += 1
                avg_res /= counter
                res[aggregate_meaning] = [round(avg_res, 2)]
            case 'min':
                min_res = float('inf')  # Начальное значение — бесконечность
                for row in products:
                    try:
                        float(row[aggregate_col_name])
                    except ValueError:
                        return {' ': ['error']}
                    price = float(row[aggregate_col_name])
                    if price < min_res:
                        min_res = price
                res[aggregate_meaning] = [min_res]
            case 'max':
                max_res = 0
                for row in products:
                    try:
                        float(row[aggregate_col_name])
                    except ValueError:
                        return {' ': ['error']}
                    price = float(row[aggregate_col_name])
                    if price > max_res:
                        max_res = price
                res[aggregate_meaning] = [max_res]
    return res

def args_parse() -> list[str]:
    '''
    Данная функция парсит настройки введенные в сmd при запуске кода
    '''
    parser = argparse.ArgumentParser(description="Обработка CSV-файла с фильтрацией.")
    parser.add_argument('--file', required=True, help='Путь к CSV-файлу')
    parser.add_argument('--where', required=False, help='Условие фильтрации')
    parser.add_argument('--aggregate', required=False, help='Условие агрегации')
    return parser.parse_args()

def main():
    args = args_parse()
    with open(args.file, "r", newline="") as file:
        products = csv.DictReader(file)

        if args.where:
            products = where(args.where, products)

        if args.aggregate:
            products = aggregate(args.aggregate, products)

        print(tabulate(products, headers="keys", tablefmt="outline"))


if __name__ == "__main__":
    main()
