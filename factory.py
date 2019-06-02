from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Type

from offers import Offer, Seal


class Factory(ABC):
    """
    Factory satisfies the customers' orders
    """

    class _Assembly(ABC):
        def __init__(self):
            pass

        @abstractmethod
        def assemble_order(self, offer: Offer, n_workers: int) -> dict:
            """
            Actually assemble the order. It is assumed that all resources have been allocated.

            :param offer: the offer to assemble
            :param n_workers: number of workers assigned
            :return: Dictionary with all the information of the assembly
            """
            pass

    @abstractmethod
    def __init__(self, personnel: int):
        self.personnel = personnel
        self.assembly = Factory.create_assembly()
        self.storage = dict()

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

    @classmethod
    def __extract_resources(cls, resources: dict, to_extract: dict) -> None:
        """
        Extracts resources form a resource dictionary
        :param resources:
        :param to_extract:
        """

        # Loop through keys and take the appropriate resources if possible
        for key in to_extract.keys():
            if resources[key] < to_extract[key]:
                raise Exception("Attempt to extract more resources than available.")
            else:
                resources[key] -= to_extract[key]

    @classmethod
    @abstractmethod
    def create_assembly(cls) -> Type[_Assembly]:
        """

        :return: instance of implementation of _Assembly
        """
        pass


class EttenLeurFactory(Factory):
    """
    Flowserve factory in Etten-Leur
    """
    
    class _QuickAssembly(Factory._Assembly):
        def assemble_order(self, offer: Offer, n_workers: int) -> dict:
            # TODO: continue
            pass

    def __init__(self, personnel: int):
        super().__init__(personnel)

        self._offers = [Seal("A", 15000.0, 12), Seal("B", 15000.0, 12)]

    @classmethod
    def create_assembly(cls):
        return cls._QuickAssembly()

    def place_order(self, offer: Offer):
        super().place_order(offer)

        EttenLeurFactory.__extract_resources(self.storage, offer.get_resources())
        self.assembly.assemble_order(self.assembly, offer, self.personnel)

    def get_offers(self) -> List[Offer]:
        return self._offers