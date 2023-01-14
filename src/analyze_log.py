import csv


def read_file(path_to_file):
    with open(path_to_file, newline="") as csv_file:
        fields = ["customer", "order", "day"]
        return list(csv.DictReader(csv_file, fieldnames=fields))


def data_clients(customer, data):
    return [item for item in data if item["customer"] == customer]


def more_orders(data):
    counter = {}
    more_ordered = data[0]["order"]
    for item in data:
        if item["order"] not in counter:
            counter[item["order"]] = 1
        else:
            counter[item["order"]] += 1
        if counter[item["order"]] > counter[more_ordered]:
            more_ordered = item["order"]
    return more_ordered


def quantity(data, order_name):
    demands = 0
    for item in data:
        if item["order"] == order_name:
            demands += 1
    return demands


def never_ordered(customer_data, data):
    order_data = set([item["order"] for item in data])
    order_client = set([item["order"] for item in customer_data])
    return order_data.difference(order_client)


def days_never_dinner(customer_data, data):
    day_order = set([item["day"] for item in data])
    day_client_order = set([item["day"] for item in customer_data])
    return day_order.difference(day_client_order)


def write_file(target_path, data):
    file_w = open(target_path, "w")
    for item in data:
        file_w.write(f"{item}\n")
    file_w.close()


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file, "r") as file:
            data = [
                *csv.DictReader(file, fieldnames=["client", "dish", "weekday"])
            ]
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    data = read_file(path_to_file)
    data_maria = data_clients("maria", data)
    data_arnaldo = data_clients("arnaldo", data)
    data_joao = data_clients("joao", data)
    result1 = more_orders(data_maria)
    result2 = quantity(data_arnaldo, "hamburguer")
    result3 = never_ordered(data_joao, data)
    result4 = days_never_dinner(data_joao, data)
    path_to_file = "data/mkt_campaign.txt"
    write_file(path_to_file, [result1, result2, result3, result4])
