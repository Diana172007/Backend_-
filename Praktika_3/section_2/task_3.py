class Product:
    """Товар в магазине: название, цена, остаток на складе и категория."""

    def __init__(self, name, price, quantity_in_stock, category):
        """Создаёт товар.

        Args:
            name (str): Название товара.
            price (float): Цена за единицу.
            quantity_in_stock (int): Количество на складе.
            category (str): Категория товара.
        """
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        self.category = category

    def is_available(self, quantity):
        """Проверяет, хватает ли товара на складе.

        Args:
            quantity (int): Запрашиваемое количество.

        Returns:
            bool: True, если товара достаточно.
        """
        return self.quantity_in_stock >= quantity

    def reduce_stock(self, quantity):
        """Списывает товар со склада.

        Args:
            quantity (int): Сколько списать.

        Returns:
            int: Остаток после списания.
            str: Сообщение, если товара недостаточно.
        """
        if self.is_available(quantity):
            self.quantity_in_stock = self.quantity_in_stock - quantity
            return self.quantity_in_stock
        else:
            return "на складе товара меньше"


class Order:
    """Заказ: корзина, скидка и налог для расчёта итоговой стоимости."""

    def __init__(self, cart, discount, tax):
        """Создаёт заказ.

        Args:
            cart (ShoppingCart): Корзина с товарами.
            discount (float): Скидка (0.1 = 10%).
            tax (float): Налог (0.2 = 20%).
        """
        self.cart = cart
        self.discount = discount
        self.tax = tax

    def calculate_total(self):
        """Считает итоговую стоимость заказа.

        Returns:
            float: Итог с учётом скидки и налога.
        """
        subtotal = sum(
            product.price * quantity for product, quantity in self.cart.items.items()
        )
        after_discount = subtotal * (1 - self.discount)
        return after_discount * (1 + self.tax)


class Customer:
    """Покупатель: имя, email и история заказов."""

    def __init__(self, name):
        """Создаёт покупателя.

        Args:
            name (str): Имя покупателя.
        """
        self.name = name
        self.order_history = []

    def add_order(self, order):
        """Добавляет заказ в историю.

        Args:
            order (Order): Заказ для добавления.
        """
        self.order_history.append(order)


class ShoppingCart:
    """Корзина: хранит товары и их количество перед оформлением заказа."""

    def __init__(self):
        """Создаёт пустую корзину."""
        self.items = dict()

    def add_product(self, product, counter):
        """Добавляет товар в корзину или увеличивает его количество.

        Args:
            product (Product): Товар.
            counter (int): Сколько добавить.

        Returns:
            dict: Текущее содержимое корзины.
        """
        if product in self.items.keys():
            self.items[product] += counter
        else:
            self.items[product] = counter
        return self.items

    def remove_product(self, product):
        """Удаляет товар из корзины.

        Args:
            product (Product): Товар для удаления.
        """
        del self.items[product]


phone = Product("iPhone", 1000, 10, "Электроника")
cart = ShoppingCart()
cart.add_product(phone, 2)
order = Order(cart, 0.1, 0.2)
print(order.calculate_total())
customer = Customer("Аня")
customer.add_order(order)
print(len(customer.order_history))
phone.reduce_stock(2)
print(phone.quantity_in_stock)
