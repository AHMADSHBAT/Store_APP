

from curses.ascii import isdigit
from itertools import product
from re import M
import string


class Product:
    def __init__(self, name: string):
        self.name = name


class Categories(Product):
    def __init__(self, name: string, type: string, exist: bool):
        Product.__init__(self, name)
        self.type = type
        self.exist = exist


class Amplifier(Product):
    def __init__(self, name: string, power: int, ChannelNumbers: int):
        product.__init__(self, name)
        self.type = "AMP"
        self.power = power
        self.channelNumbers = ChannelNumbers


class Receiver(Product):
    def __init__(self, name: string, size: int, color: string, ChannelNumbers: int):
        product.__init__(self, name)
        self.type = "AMP"
        self.size = size
        self.channelNumbers = ChannelNumbers
        self.color = color


class Orders(Product):
    def __init__(self, name: string, type: string, size: int = 1, color: string = None, ChannelNumbers: int = None):
        product.__init__(self, name)
        self.type = "AMP"
        self.size = size
        self.channelNumbers = ChannelNumbers
        self.color = color


def catagories():
    print('''
        choose option:
            1. Add a category
            2. Remove a category
            3. Display all the categories
        ''')
    option: int = input(':')
    if (isdigit(option) == False):
        print('You have intered wrong option, Please try again...')
        return;
    match option:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass


def products():
    print('''
        choose option:
            1. Add a products
            2. Remove a products
            3. Display all the products
        ''')
    option: int = input(':')
    if (isdigit(option) == False):
        print('You have intered wrong option, Please try again...')
        return;
    match option:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass


def Orders():
    print('''
        choose option:
            1. Add a Orders
            2. Remove a Orders
            3. Display all the Orders
        ''')
    option: int = input(':')
    if (isdigit(option) == False):
        print('You have intered wrong option, Please try again...')
        return;
    
    match option:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass


if __name__ == '__main__':

    while True:
        print('''
        Sekelton Store:
        choose option:
            1. Categories
            2. Products
            3. Orders
            4. Exit
        ''')

        option: int = input(':')
        if (isdigit(option) == False):
            print('You have intered wrong option, Please try again...')
            break;
        print("hello")
        match option:
            case 1:
                catagories()
                break
            case 2:
                product()
                break
            case 3:
                Orders()
                break
            case 4:
                break
