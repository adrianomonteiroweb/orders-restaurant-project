import csv


def analyze_log(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f'Extensão invalida: {path_to_file}')
    try:
        with open(path_to_file, "r") as file:
            reader = csv.DictReader(file, fieldnames=['nome', 'comida', 'dia'])

            array = []

            for row in reader:
                array.append(row)

        with open('data/mkt_campaign.txt', 'w') as write_file:
            write_file.write(
                f'{more_orders(array)}\n'
                f'{count_hamburguer(array)}\n'
                f'{no_orders(array)}\n'
                f'{did_not_visit(array)}\n'
            )

    except FileNotFoundError:
        raise FileNotFoundError(f'Arquivo inexistente: {path_to_file}')


def more_orders(array):
    count = {}

    maria_orders = [row for row in array if row['nome'] == 'maria']

    for row in maria_orders:
        if row['comida'] not in count:
            count[row['comida']] = 1
        if row['comida'] in count:
            count[row['comida']] += 1
        if count[row['comida']] > count[maria_orders[0]['comida']]:
            maria_orders[0]['comida'] = row['comida']

    return maria_orders[0]['comida']


def count_hamburguer(array):
    count = 0

    for row in array:
        if row['comida'] == 'hamburguer' and row['nome'] == 'arnaldo':
            count = count + 1

    return count


def no_orders(array):
    all_dishes = set(['misto-quente', 'hamburguer', 'pizza', 'coxinha'])

    not_dishes_orders = set()

    for row in array:
        if row['nome'] == 'joao':
            not_dishes_orders.add(row['comida'])

    return all_dishes.difference(not_dishes_orders)


def did_not_visit(array):
    all_days = set()

    not_visit_days = set()

    for row in array:
        all_days.add(row['dia'])
        if row['nome'] == 'joao':
            not_visit_days.add(row['dia'])

    return all_days.difference(not_visit_days)


analyze_log("data/orders_1.csv")
