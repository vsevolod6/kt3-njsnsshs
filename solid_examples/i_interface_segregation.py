"""
I — Interface Segregation Principle
Принцип разделения интерфейсов.

Идея:
Не нужно заставлять класс реализовывать методы, которые ему не нужны.

Лучше сделать несколько маленьких специализированных интерфейсов,
чем один большой и неудобный.
"""

from abc import ABC, abstractmethod


class CardPayment(ABC):
    """
    Интерфейс для оплаты банковской картой.
    """

    @abstractmethod
    def pay_by_card(self, amount: float) -> None:
        pass


class PhonePayment(ABC):
    """
    Интерфейс для оплаты по номеру телефона.
    """

    @abstractmethod
    def pay_by_phone(self, amount: float) -> None:
        pass


class WebMoneyPayment(ABC):
    """
    Интерфейс для оплаты через WebMoney.
    """

    @abstractmethod
    def pay_by_webmoney(self, amount: float) -> None:
        pass


class InternetPaymentService(CardPayment, PhonePayment, WebMoneyPayment):
    """
    Интернет-сервис поддерживает все виды оплаты,
    поэтому может реализовать все маленькие интерфейсы.
    """

    def pay_by_card(self, amount: float) -> None:
        print(f"Оплата картой на сумму {amount} выполнена.")

    def pay_by_phone(self, amount: float) -> None:
        print(f"Оплата по номеру телефона на сумму {amount} выполнена.")

    def pay_by_webmoney(self, amount: float) -> None:
        print(f"Оплата через WebMoney на сумму {amount} выполнена.")


class TerminalPaymentService(CardPayment):
    """
    Терминал поддерживает только оплату картой.
    Благодаря ISP ему не нужно реализовывать лишние методы.
    """

    def pay_by_card(self, amount: float) -> None:
        print(f"Терминал принял оплату картой на сумму {amount}.")


def run_isp_example() -> None:
    internet_service = InternetPaymentService()
    internet_service.pay_by_card(1000)
    internet_service.pay_by_phone(500)
    internet_service.pay_by_webmoney(700)

    terminal_service = TerminalPaymentService()
    terminal_service.pay_by_card(1500)
