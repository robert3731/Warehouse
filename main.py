from tabulate import tabulate


items = [{'name': 'Charger', 'quantity': 35, 'unit': 'pcs.', 'unit_price': 24},
         {'name': 'Headphones', 'quantity': 12, 'unit': 'pcs.', 'unit_price': 30},
         {'name': 'Phone case', 'quantity': 127, 'unit': 'pcs.', 'unit_price': 28},
         {'name': 'Screen protector', 'quantity': 88, 'unit': 'pcs.', 'unit_price': 20}]

sold_items = []


def add_item(name, quantity, unit, unit_price):
    new_item = {'name': name, 'quantity': quantity, 'unit': unit, 'unit_price': unit_price}
    for item in items:
        if item['name'] == new_item['name']:
            print('Item already in warehouse')
            item['quantity'] = item['quantity'] + new_item['quantity']
            break
    else:
        items.append(new_item)
        print('Successfully added {}'.format(name))


def sell_item(name, quantity):
    for item in items:
        if item['name'] == name:
            if item['quantity'] >= int(quantity):
                item['quantity'] = item['quantity'] - quantity
                sold_item = {'name': name, 'quantity': quantity, 'unit': item['unit'], 'unit_price': item['unit_price']}
                sold_items.append(sold_item)
                return 'Successfully sold {} {} of {}'.format(quantity, item['unit'], item['name'])
            else:
                return 'Sorry we have {} {} of {} at this moment.'\
                    .format(item['quantity'], item['unit'], item['name'])


def get_costs():
    values = []
    for i in items:
        value = i.get('quantity') * i.get('unit_price')
        values.append(value)
    return sum(values)


def get_income():
    values = []
    for i in sold_items:
        value = i.get('quantity') * i.get('unit_price')
        values.append(value)
    return sum(values)


def show_revenue():
    return get_income() - get_costs()


def menu():
    while True:
        print("1-Items available in warehouse")
        print("2-Add new item")
        print("3-Sell an item")
        print("4-Get revenue")
        print("5-Exit")

        action = input("What would you like to do?")

        if action == "5":  # Exit
            exit()

        elif action == '1':  # Displaying items in warehouse
            print(tabulate(items, headers={'name': 'Name', 'quantity': 'Quantity:',
                                           'unit': 'Unit', 'unit_price': 'Unit Price (PLN)'}))

        elif action == '2':  # Adding new item
            new_name = (input('Item name:')).capitalize()
            new_quantity = int(input('Item quantity:'))
            new_unit = input('Item unit eg. l, kg, pcs:')
            new_unit_price = float(input('Item price in PLN:'))
            add_item(new_name, new_quantity, new_unit, new_unit_price)

        elif action == '3':  # Selling item
            sell_name = (input('Item name:')).capitalize()
            sell_quantity = int(input('Item quantity:'))
            print(sell_item(sell_name, sell_quantity))

        elif action == '4':
            print('Revenue breakdown (PLN)')
            print('Income:\t{}'.format(get_income()))
            print('Costs:\t{}'.format(get_costs()))
            print("-" * 10)
            print('Revenue\t{} PLN'.format(show_revenue()))

        else:
            print('Please choose available option.')


if __name__ == '__main__':
    print("Warehouse\n")
    menu()
