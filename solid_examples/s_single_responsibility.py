"""
S — Single Responsibility Principle
Принцип единственной ответственности.

Идея:
Каждый класс должен отвечать только за одну задачу.
Если у класса несколько обязанностей, его сложнее поддерживать и изменять.
"""


class CarRepository:
    """
    Отвечает только за хранение и поиск информации о машинах.
    Это одна зона ответственности: работа с данными.
    """

    def __init__(self) -> None:
        self._cars = {
            "A111AA": {"model": "Toyota Camry", "type": "sedan"},
            "B222BB": {"model": "Ford Transit", "type": "van"},
            "C333CC": {"model": "Mitsubishi L200", "type": "pickup"},
        }

    def find_by_number(self, number: str) -> dict | None:
        return self._cars.get(number)


class BookingService:
    """
    Отвечает только за бронирование машины.
    Не занимается ни печатью, ни уведомлениями, ни хранением данных.
    """

    def book_car(self, car_number: str, customer_name: str) -> str:
        return f"Машина {car_number} успешно забронирована для клиента {customer_name}."


class PrinterService:
    """
    Отвечает только за вывод/печать заказа.
    """

    def print_booking(self, booking_text: str) -> None:
        print(f"[Печать заказа]: {booking_text}")


class NotificationService:
    """
    Отвечает только за отправку уведомлений.
    """

    def send_notification(self, message: str) -> None:
        print(f"[Уведомление]: {message}")


def run_srp_example() -> None:
    """
    Демонстрация того, как несколько маленьких классов
    лучше одного большого 'универсального' класса.
    """
    repository = CarRepository()
    booking_service = BookingService()
    printer = PrinterService()
    notifier = NotificationService()

    car = repository.find_by_number("A111AA")
    if car is None:
        print("Машина не найдена.")
        return

    booking_result = booking_service.book_car("A111AA", "Иван")
    printer.print_booking(booking_result)
    notifier.send_notification(
        f"Клиенту отправлено сообщение о бронировании машины {car['model']}."
    )
