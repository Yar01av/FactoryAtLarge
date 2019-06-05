##########################################
# This file should be run from the console
##########################################
from customers import SimpleCustomer
from factory import EttenLeurFactory


if __name__ == "__main__":
    FACTORY = EttenLeurFactory(10)
    CUSTOMER = SimpleCustomer("Yaro", factories=[FACTORY])

    print(CUSTOMER.buy_item())
