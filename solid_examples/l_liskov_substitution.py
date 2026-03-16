"""
L — Liskov Substitution Principle
Принцип подстановки Лисков.

Идея:
Если класс B наследуется от класса A,
то объект B должен без проблем использоваться там, где ожидается A.

Наследник не должен ломать ожидаемое поведение родителя.
"""


class Account:
    """
    Базовый класс счета.
    Здесь содержится только та логика, которая подходит всем счетам.
    """

    def __init__(self, balance: float) -> None:
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def get_balance(self) -> float:
        return self.balance


class PaymentAccount(Account):
    """
    Отдельный класс для счетов, которые поддерживают оплату.
    Не все счета обязаны уметь проводить оплату.
    """

    def pay(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError("Недостаточно средств.")
        self.balance -= amount


class SalaryAccount(PaymentAccount):
    """
    Зарплатный счет поддерживает пополнение, просмотр баланса и оплату.
    Его можно подставить вместо PaymentAccount без проблем.
    """
    pass


class DepositAccount(Account):
    """
    Депозитный счет не поддерживает оплату.
    Поэтому он наследуется не от PaymentAccount, а от обычного Account.
    Это правильнее с точки зрения LSP.
    """
    pass


def process_salary_payment(account: PaymentAccount, amount: float) -> None:
    """
    Функция ожидает счет, который умеет проводить оплату.
    SalaryAccount подходит.
    DepositAccount сюда передавать не нужно и нельзя.
    """
    account.pay(amount)
    print(f"Оплата {amount} выполнена. Остаток: {account.get_balance()}")


def run_lsp_example() -> None:
    salary_account = SalaryAccount(5000)
    process_salary_payment(salary_account, 1200)

    deposit_account = DepositAccount(10000)
    deposit_account.deposit(500)
    print(f"Баланс депозитного счета: {deposit_account.get_balance()}")
