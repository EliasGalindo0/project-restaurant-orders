from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []
        self.all_customers = set()
        self.all_orders = set()
        self.all_days = set()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer: str, order: str, day: str):
        self.orders.append({"customer": customer, "order": order, "day": day})
        self.all_customers.add(customer)
        self.all_orders.add(order)
        self.all_days.add(day)

    def get_most_ordered_dish_per_customer(self, customer: str):
        orders_dish = [
            entry["order"]
            for entry in self.orders
            if entry["customer"] == customer
        ]
        return Counter(orders_dish).most_common(1)[0][0]

    def get_never_ordered_per_customer(self, customer: str):
        ordereds = {
            entry["order"]
            for entry in self.orders
            if entry["customer"] == customer
        }
        return self.all_orders - ordereds

    def get_days_never_visited_per_customer(self, customer: str):
        visits = {
            entry["day"]
            for entry in self.orders
            if entry["customer"] == customer
        }
        return self.all_days - visits

    def get_busiest_day(self):
        day_busiest = [entry["day"] for entry in self.orders]
        return Counter(day_busiest).most_common(1)[0][0]

    def get_least_busy_day(self):
        day_least_busy = [entry["day"] for entry in self.orders]
        return Counter(day_least_busy).most_common()[-1][0]
      