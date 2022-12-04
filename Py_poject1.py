
from itertools import product
import json
from re import M
import string


class Product:
    def __init__(self, name: string):
        self.name = name

    def __str__(self):
        return self.__dict__

    def __repr__(self):
        return self.__str__()

class Categories(Product):
    def __init__(self, name: string, type: string, exist: bool):
        Product.__init__(self, name)
        self.type = type
        self.exist = exist


class Amplifier(Categories):
    def __init__(self, name: string, power: int, ChannelNumbers: int, size:int):
        Product.__init__(self, name)
        self.type = "amplifier"
        self.power = power
        self.channelNumbers = ChannelNumbers


class Receiver(Categories):
    def __init__(self, name: string, size: int, color: string, ChannelNumbers: int):
        Product.__init__(self, name)
        self.type = "receiver"
        self.size = size
        self.channelNumbers = ChannelNumbers
        self.color = color

    def __str__(self):
        return self.__dict__

    def __repr__(self):
        return self.__str__()

    # def __iter__(self):
    #     yield {
    #         "name": self.name,
    #         "size": self.size,
    #         "color": self.color,
    #         "ChannelNumbers": self.channelNumbers,
    #         "type": self.type
    #     }


def AddProduct():
    print('''
        type of product info:''')
    Type = input('type:');
    if not Type:
        print('please insert string..');
        return -1;
    inpS = input('name:');
    if not inpS:
        print('please insert string..');
        return -1;
    size = int(input('size:'));
    if size < 1:
        print('please insert digit');
        return -1;
    color = input('color:');
    if not color:
        print('please insert color..');
        return -1;
    ch = int(input('channels:'));
    if ch < 1:
        print('please insert digit');
        return -1;
    if Type.lower() == "receiver":
        Rec = Receiver(inpS, size, color, ch);
        appendData(Rec);
    if Type.lower() == "amplifier":
        power = int(input('power:'));
        if ch < 1:
            print('please insert digit');
            return -1;
        Rec = Amplifier(inpS, power, ch, size);
        appendData(Rec);

def loadData():
    with open('data.json', 'r') as f:
        saveIn = json.load(f);
        return saveIn;

def appendData(Cate):
    with open('data.json', 'r', encoding='utf-8') as file:
        d = [];
        # str = "";
        try:
            d = json.load(file);
        except ValueError:
            print('error here');
        d.append(Cate.__dict__);
        saveData(d);

def saveData(data):
    with open('data.json', 'w') as f:
        saveIn = json.dumps(data);
        f.write(saveIn);

# def searchForType(data, targetName, targetType):
#     for i in data:
#         if i['type'] == targetType and i['name'] == targetName.lower():
#             return True;
#     return False;

def deleteEntry(nameToDelete, typeToDelete):
    try:
        data = loadData();
    except ValueError:
            print('error here 2');
    for idx, dictionary in enumerate(data):
        if dictionary['type'].lower() == typeToDelete and dictionary['name'].lower() == nameToDelete.lower():
            data.pop(idx)
            saveData(data)
            return;
    print('entry %s not found', nameToDelete);



def RemoveProduct():
    name = input('category name:');
    if not name:
        print('please insert string..');
        return -1;
    type = input('category type:');
    if not type:
        print('please insert color..');
        return -1;
    deleteEntry(name, type)

def DisplayAllProduct():
    print(loadData());

def Products():
    print('''
        choose option:
            1. Add a products
            2. Remove a products
            3. Display all the products
        ''')
    option: int = input(':')
    match int(option):
        case 1:
            AddProduct();
        case 2:
            RemoveProduct();
        case 3:
            DisplayAllProduct();




if __name__ == '__main__':

    while True:
        print('''
        Sekelton Store:
        choose option:
            1. Products
            2. Exit
        ''')

        option: int = input()
        match int(option):
            case 1:
                Products();
            case 2:
                break;
            
