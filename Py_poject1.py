
from itertools import product
import json
from re import M
import string


class Product:
    def __init__(self, name: string):
        self.name = name

    def __str__(self):
        return json.dumps(self, ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

class Categories(Product):
    def __init__(self, name: string, type: string, exist: bool):
        Product.__init__(self, name)
        self.type = type
        self.exist = exist


class Amplifier(Categories):
    def __init__(self, name: string, power: int, ChannelNumbers: int):
        Product.__init__(self, name)
        self.type = "AMP"
        self.power = power
        self.channelNumbers = ChannelNumbers


class Receiver(Categories):
    def __init__(self, name: string, size: int, color: string, ChannelNumbers: int):
        Product.__init__(self, name)
        self.type = "AMP"
        self.size = size
        self.channelNumbers = ChannelNumbers
        self.color = color

    def __str__(self):
        return json.dumps(self, ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield {
            "name": self.name,
            "size": self.size,
            "color": self.color,
            "ChannelNumbers": self.channelNumbers,
            "type": self.type
        }


class Orders(Product):
    def __init__(self, name: string, type: string, size: int = 1, color: string = None, ChannelNumbers: int = None):
        Product.__init__(self, name)
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
    match int(option):
        case 1:
            AddCategory();
        case 2:
            pass
        case 3:
            pass


def AddCategory():
    inpI = int(input('''
        type of product category:
            for Receiver choose 1
            For Amplifier choose 2
            :
    '''))
    match inpI:
        case 1:
            inpS = input('category name:');
            if not inpS:
                print('please insert string..');
                return -1;
            size = int(input('category size:'));
            if size < 1:
                print('please insert digit');
                return -1;
            color = input('category color:');
            if not color:
                print('please insert color..');
                return -1;
            ch = int(input('category size:'));
            if ch < 1:
                print('please insert digit');
                return -1;
            Rec = Receiver(inpS, size, color, ch);
            saveData(Rec);

def saveData(Cate):
    with open('data.json', 'a') as f:
        print(Cate);
        f.write(Cate);


def products():
    print('''
        choose option:
            1. Add a products
            2. Remove a products
            3. Display all the products
        ''')
    option: int = input(':')
    match int(option):
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass


def orders():
    print('''
        choose option:
            1. Add a Orders
            2. Remove a new Orders
            3. Display all the Orders
        ''')
    option: int = input(':')
    
    match int(option):
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

        option: int = input()
        match int(option):
            case 1:
                catagories();
            case 2:
                product();
            case 3:
                orders();
            
