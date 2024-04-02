# Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики,
# такие как адрес, название и ассортимент товаров. Ваша задача — создать класс `Store`,
# который можно будет использовать для создания различных магазинов.

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name)
        if not item in items:
            none

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

#Рандом магазины
store1 = Store("Магнит", "Невский проспект")
store1.add_item("Яблоки", 50)
store1.add_item("Мандарины", 100)
store1.add_item("Ананасы", 150)

store2 = Store("Vintage shop", "Улица 80")
store2.add_item("Пиджак", 1000)
store2.add_item("Туфли", 2500)
store2.add_item("Брюки", 3000)

store3 = Store("Supermarket", "Ул. Пушкина")
store3.add_item("Молоко", 70)
store3.add_item("Хлеб", 50)
store3.add_item("Авокадо", 150)



store3.add_item("Творог", 50)
print(store3.items)
store3.update_price(50, 60)
print(store3.items)
store3.remove_item("Авокадо")
print(store3.items)
store3.get_price("Авокадо")
print(store3.items)

# Шаги:
# 1. Создай класс `Store`:

# -Атрибуты класса:
# - `name`: название магазина.
# - `address`: адрес магазина.
# - `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.
#
# - Методы класса:
#
# - `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
# -  метод для добавления товара в ассортимент.
# - метод для удаления товара из ассортимента.
# - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
# - метод для обновления цены товара.

# 2. Создай несколько объектов класса `Store`:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.

# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.
# В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с реализацией задания.