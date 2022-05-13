class TrackOrders:
    def __init__(self):
        self.log = []

    def __len__(self):
        return len(self.log)

    def add_new_order(self, customer, order, day):
        self.log.append({"customer": customer, "order": order, "day": day})

    def get_most_ordered_dish_per_customer(self, customer):
        count = {}

        orders = [row for row in self.log if row['customer'] == customer]

        for row in orders:
            if row['order'] not in count:
                count[row['order']] = 1
            if row['order'] in count:
                count[row['order']] += 1
            if count[row['order']] > count[orders[0]['order']]:
                orders[0]['order'] = row['order']

        return orders[0]['order']

    def get_never_ordered_per_customer(self, customer):
        orders = set()

        orders_customer = set()

        array = self.log

        for row in array:
            orders.add(row['order'])

            if row['customer'] == customer:
                orders_customer.add(row['order'])

        return orders.difference(orders_customer)

    def get_days_never_visited_per_customer(self, customer):
        days = set()

        days_customer = set()

        array = self.log

        for row in array:
            days.add(row['day'])

            if row['customer'] == customer:
                days_customer.add(row['day'])

        return days.difference(days_customer)

    def get_busiest_day(self):
        count = {}

        array = self.log

        for row in array:
            if row['day'] not in count:
                count[row['day']] = 1

            if row['day'] in count:
                count[row['day']] += 1

            if count[row['day']] > count[array[0]['day']]:
                array[0]['day'] = row['day']

        return array[0]['day']

    def get_least_busy_day(self):
        count = {}

        array = self.log

        for row in array:
            if row['day'] not in count:
                count[row['day']] = 1

            if row['day'] in count:
                count[row['day']] += 1

            if count[row['day']] < count[array[0]['day']]:
                array[0]['day'] = row['day']

        return array[0]['day']
