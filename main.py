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
                return 'Successfully sold {} {} of {}'.format(quantity, item['unit'], item['name'])
            else:
                print('Sorry we have only {} {} of {} at this moment.'
                      .format(item['quantity'], item['unit'], item['name']))


def menu():
    while True:
        print("\nWarehouse\n")
        print("1-Items available in warehouse")
        print("2-Add new item")
        print("3-Sell an item")
        print("4-Exit")

        action = input("What would you like to do?")

        if action == "4":  # Exit
            exit()

        elif action == '1':  # Displaying items in warehouse
            print(tabulate(items, headers={'name': 'Name', 'quantity': 'Quantity:',
                                           'unit': 'Unit', 'unit_price': 'Unit Price (PLN)'}))

        elif action == '2':  # Adding new item
            new_name = (input('Item name:')).capitalize()
            new_quantity = int(input('Item quantity:'))
            new_unit = input('Item unit eg. l, kg, pcs:')
            new_unit_price = int(input('Item price in PLN:'))
            add_item(new_name, new_quantity, new_unit, new_unit_price)

        elif action == '3':  # Selling item
            sell_name = (input('Item name:')).capitalize()
            sell_quantity = int(input('Item quantity:'))
            print(sell_item(sell_name, sell_quantity))

        else:
            print('Please choose available option.')


if __name__ == '__main__':
    print(type(items))
    menu()
