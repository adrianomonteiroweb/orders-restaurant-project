class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.orders = []
        self.stock = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }
        self.buy = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def get_available_dishes(self):
        accessible = set()

        for ingredient in self.INGREDIENTS:
            make = True
            for food in self.INGREDIENTS[ingredient]:
                if self.stock[food] == 0:
                    make = False
            if make:
                accessible.add(ingredient)

        return accessible

    def add_new_order(self, customer, order, day):
        dishes = self.get_available_dishes()

        for ingredient in self.INGREDIENTS[order]:
            if order in dishes:
                self.stock[ingredient] -= 1
                self.buy[ingredient] += 1
            elif order not in dishes:
                return False

            self.orders.append((customer, order, day))

    def get_quantities_to_buy(self):
        return self.buy
