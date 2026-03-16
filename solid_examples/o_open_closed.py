"""
O — Open/Closed Principle
Принцип открытости/закрытости.

Идея:
Класс должен быть открыт для расширения, но закрыт для изменения.
То есть новую функциональность лучше добавлять через новые классы,
а не переписывать уже работающий код.
"""

from abc import ABC, abstractmethod


class NotificationSender(ABC):
    """
    Абстракция для отправки уведомлений.
    Если нужно добавить новый способ отправки,
    мы просто создаем новый класс-наследник.
    """

    @abstractmethod
    def send(self, message: str) -> None:
        pass


class EmailNotification(NotificationSender):
    """
    Отправка уведомления по email.
    """

    def send(self, message: str) -> None:
        print(f"[Email] Отправлено сообщение: {message}")


class SMSNotification(NotificationSender):
    """
    Отправка уведомления по SMS.
    """

    def send(self, message: str) -> None:
        print(f"[SMS] Отправлено сообщение: {message}")


class TelegramNotification(NotificationSender):
    """
    Новый способ отправки сообщений.
    Мы добавили новый класс, но не меняли существующие.
    Это и есть соблюдение OCP.
    """

    def send(self, message: str) -> None:
        print(f"[Telegram] Отправлено сообщение: {message}")


def notify_user(sender: NotificationSender, message: str) -> None:
    """
    Функция работает с абстракцией NotificationSender.
    Ей не важно, какой именно канал отправки используется.
    """
    sender.send(message)


def run_ocp_example() -> None:
    notify_user(EmailNotification(), "Ваш заказ подтвержден.")
    notify_user(SMSNotification(), "Ваш код подтверждения: 1234.")
    notify_user(TelegramNotification(), "Доставка будет завтра.")
