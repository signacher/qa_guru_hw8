"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(0) is True
        assert product.check_quantity(100) is True
        assert product.check_quantity(999) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(0)
        assert product.quantity == 1000
        product.buy(486)
        assert product.quantity == 514
        product.buy(514)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError, 'Продуктов не хватает!'):
            product.buy(quantity=1500)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, product):
        cart = Cart()
        cart.add_product(product)

        assert cart.products == {product: 1}

    def test_buy_product(self, cart, product):
        cart.add_product(product, 10)
        cart.buy()

        assert len(cart.products) == 0

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 5)

        assert cart.get_total_price() == 500

    def test_remove_product_from_the_cart(self, cart, product):
        cart.add_product(product, 10)
        cart.remove_product(product, 7)

        assert cart.products == 3

    def test_buy_with_empty_cart(self, product):
        cart = Cart()

        with pytest.raises(ValueError,'Нет товаров в корзине!!!'):
            cart.buy()