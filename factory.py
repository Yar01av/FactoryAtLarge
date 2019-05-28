from abc import ABC, abstractmethod
from typing import List

from offers import Offer, Seal


class Factory(ABC):
    """
    Factory satisfies the customers' orders
    """
    def __init__(self, personnel: int):
        self.personnel = personnel

    @abstractmethod
    def get_offers(self) -> List[Offer]:
        """
        :return: A list of products that can be purchased at the factory at that time
        """

    @abstractmethod
    def place_order(self, offer: Offer):
        """
        :param offer: what the customer wants to buy
        :return: throw exception on failure and return a dictionary with useful info otherwise
        """

        # Check that this a valid offer (and it comes from the list provided by the factory)
        if offer not in self.get_offers():
            raise Exception()


class EttenLeurFactory(Factory):
    """
    Flowserve factory in Etten-Leur
    """

    def __init__(self, personnel: int):
        super().__init__(personnel)

        self._offers = [Seal("A", 15000.0, 12), Seal("B", 15000.0, 12)]

    def place_order(self, offer: Offer):
        super().place_order(offer)

    def get_offers(self) -> List[Offer]:
        return self._offers