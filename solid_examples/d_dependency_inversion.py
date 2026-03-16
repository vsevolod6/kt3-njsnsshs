"""
D — Dependency Inversion Principle
Принцип инверсии зависимостей.

Идея:
Модуль высокого уровня не должен зависеть от конкретных реализаций.
И высокий, и низкий уровень должны зависеть от абстракции.

Проще говоря:
магазин не должен быть жестко привязан, например, только к наличным.
"""

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    """
    Абстракция способа оплаты.
    Магазин будет работать именно с этой абстракцией.
    """

    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


class CashPayment(PaymentMethod):
    """
    Реализация оплаты наличными.
    """

    def pay(self, amount: float) -> None:
        print(f"Оплата наличными: {amount}")


class CardPayment(PaymentMethod):
    """
    Реализация оплаты картой.
    """

    def pay(self, amount: float) -> None:
        print(f"Оплата картой: {amount}")


class SBPPayment(PaymentMethod):
    """
    Реализация оплаты через СБП / телефон.
    """

    def pay(self, amount: float) -> None:
        print(f"Оплата через СБП: {amount}")


class Shop:
    """
    Магазин зависит не от конкретного класса оплаты,
    а от абстракции PaymentMethod.

    Благодаря этому можно легко менять способ оплаты,
    не переписывая код магазина.
    """

    def __init__(self, payment_method: PaymentMethod) -> None:
        self.payment_method = payment_method

    def checkout(self, amount: float) -> None:
        print("Оформление покупки...")
        self.payment_method.pay(amount)
        print("Покупка успешно оплачена.")


def run_dip_example() -> None:
    cash_shop = Shop(CashPayment())
    cash_shop.checkout(2000)

    card_shop = Shop(CardPayment())
    card_shop.checkout(3500)

    sbp_shop = Shop(SBPPayment())
    sbp_shop.checkout(4200)
