import json

with open("orders_july_2023.json", "r") as my_file:
    orders = json.load(my_file)
print('''
Список команд:
1. Какой номер самого дорого заказа за июль?
2. Какой номер заказа с самым большим количеством товаров?
3. В какой день в июле было сделано больше всего заказов?
4. Какой пользователь сделал самое большое количество заказов за июль?
5. У какого пользователя самая большая суммарная стоимость заказов за июль?
6. Какая средняя стоимость заказа была в июле?
7. Какая средняя стоимость товаров в июле?
8. Выход из программы
''')
while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Какой номер самого дорого заказа за июль?')
        max_price = 0
        max_order = ''
        # цикл по заказам
        for order_num, orders_data in orders.items():
        # получаем стоимость заказа
            price = orders_data['price']
        # если стоимость больше максимальной - запоминаем номер и стоимость заказа
            if price > max_price:
                max_order = order_num
                max_price = price
        print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')
    elif command == 2:
        print('2. Какой номер заказа с самым большим количеством товаров?')
        max_quantity = 0
        for order_num, orders_data in orders.items():
            quantity = orders_data['quantity']
            if quantity > max_quantity:
                orders = order_num
                max_quantity = quantity
        print(f'Номер заказа с самым большим количеством товаров: {orders}, количество заказов: {max_quantity}')
    elif command == 3:
        print('3. В какой день в июле было сделано больше всего заказов?')
        date_dict = {}
        for order_num, orders_data in orders.items():
            date = orders_data['date']
            date_dict[date] = date_dict.get(date, 0) + 1
        for date in sorted(date_dict):
            max_value = max(date_dict.values())
            if date_dict[date] == max_value:
                print(f'Больше всего заказов было сделано в {date}: {date_dict[date]}')
    elif command == 4:
        print('4. Какой пользователь сделал самое большое количество заказов за июль?')
        max_orders = 0
        user_dict = {}
        for order_num, orders_data in orders.items():
            user_id = orders_data['user_id']
            user_dict[user_id] = user_dict.get(user_id, 0) + 1
            orders_2 = user_dict.get(user_id)
            if orders_2 > max_orders:
                max_orders = orders_2
        print(f'Cамое большое количество заказов за июль сделал пользователь: {user_id}, количество заказов: {max_orders}')
    elif command == 5:
        print('5. У какого пользователя самая большая суммарная стоимость заказов за июль?')
        user_dict = {}
        max_price = 0
        for order_num, orders_data in orders.items():
            user_id = orders_data['user_id']
            user_dict[user_id] = user_dict.get(user_id, 0) + orders_data['price']
            all_price = user_dict.get(user_id)
            if all_price > max_price:
                max_price = all_price
        print(f'У пользователя {user_id} самая большая сумма стоимости товаров {max_price}')
    elif command == 6:
        print('6. Какая средняя стоимость заказа была в июле?')
        price_sum = 0
        price_count = 0
        for order_num, orders_data in orders.items():
            price_sum += orders_data['price']
            price_count = len(orders)
        print(f'Cредняя стоимость заказа в июле: {price_sum//price_count}')
    elif command == 7:
        print('7. Какая средняя стоимость товаров в июле?')
        price_sum = 0
        quantity_sum = 0
        for order_num, orders_data in orders.items():
            price_sum += orders_data['price']
            quantity_sum += orders_data['quantity']
        print(f'Cредняя стоимость товаров в июле: {price_sum//quantity_sum}')
    elif command == 8:
        print('8.Выход из программы')
        break