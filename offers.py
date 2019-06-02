from abc import ABC, abstractmethod


class Offer(ABC):
    """
    Encapsulates anything Factory can sell to Customer
    """

    @abstractmethod
    def __init__(self, name: str, price: float, effort: float, resources: dict):
        self._RESOURCES = resources
        self._PRICE = price
        self._NAME = name
        self._PRODUCTION_EFFORT = effort

    def get_price(self) -> float:
        """
        :return: Price of the offer
        """
        return self._PRICE

    def get_name(self) -> str:
        return self._NAME

    def get_resources(self) -> dict:
        return self._RESOURCES

    def get_production_effort(self) -> float:
        return self._PRODUCTION_EFFORT


class Seal(Offer):
    """
    Encapsulates a mechanical seal
    """

    def __init__(self, name: str, price: float, effort: float):
        super().__init__(f"SEAL-{name}", price, effort)

