from tabulate import tabulate


items = [{'name': 'Charger', 'quantity': 35, 'unit': 'pcs.', 'unit_price': 24},
         {'name': 'Headphones', 'quantity': 12, 'unit': 'pcs.', 'unit_price': 30},
         {'name': 'Phone Case', 'quantity': 127, 'unit': 'pcs.', 'unit_price': 28},
         {'name': 'Screen Protector', 'quantity': 88, 'unit': 'pcs.', 'unit_price': 20}]


def add_item(name, quantity, unit, unit_price):
    new_item = {'name': name, 'quantity': quantity, 'unit': unit, 'unit_price': unit_price}
    items.append(new_item)


def menu():
    while True:
        print("\nWarehouse\n")
        print("1-Items available in warehouse")
        print("2-Add new item")
        print("3-Exit")

        action = input("What would you like to do?")

        if action == "3":
            exit()
        elif action == '1':
            print(tabulate(items, headers={'name': 'Name', 'quantity': 'Quantity:',
                                           'unit': 'Unit', 'unit_price': 'Unit Price (PLN)'}))
        elif action == '2':
            name = input('Item name:')
            quantity = input('Item quantity:')
            unit = input('Item unit eg. l, kg, pcs:')
            unit_price = input('Item price in PLN:')
            add_item(name, quantity, unit, unit_price)
        else:
            print('Please choose available option.')


if __name__ == '__main__':
    print(type(items))
    menu()
