from typing import List, Callable
from factory import Factory
from abc import ABC, abstractmethod

from offers import Offer


class Customer(ABC):
    """
    Base class for the customers who mainly place orders. Order means choosing one (or none) of the available options
    """
    @abstractmethod
    def __init__(self, name: str, factories: List[Factory], order_chooser=lambda ls: ls[0],
                 factory_chooser=lambda ls: ls[0]):
        self.factory_chooser = factory_chooser
        self.factories = factories
        self.order_chooser = order_chooser

    @abstractmethod
    def buy_item(self, options):
        """
        Forces the customer to place an order at a factory of their choosing

        :return:
        """
        pass


class SimpleCustomer(Customer):
    """
    Customer whose behavior is designed to be as
    simple as possible
    """

    def __init__(self, name: str, factories: List[Factory]):
        super().__init__(name, factories)

    def buy_item(self, options: List[Offer]):
        """
        Choose the desired item at the deired factory
        :param options: options to choose from
        :return:
        """
        fac_choice = self.factory_chooser(self.factories)
        prod_choice = self.order_chooser(fac_choice.get_offers(options))

        return fac_choice.place_order(prod_choice)