from abc import ABC, abstractmethod


class Offer(ABC):
    """
    Encapsulates anything Factory can sell to Customer
    """

    @abstractmethod
    def __init__(self, name: str, price: float, effort: float):
        self._price = price
        self._name = name
        self._production_effort = effort

    def get_price(self) -> float:
        """
        :return: Price of the offer
        """
        return self._price

    def get_name(self) -> str:
        return self._name

    def get_production_effort(self) -> float:
        return self._production_effort


class Seal(Offer):
    """
    Encapsulates a mechanical seal
    """

    def __init__(self, name: str, price: float, effort: float):
        super().__init__(f"SEAL-{name}", price, effort)

