import csv

class AddCar:
    def __init__(self, brand, model, type, color, horsePower, sold):
        self.__brand = brand
        self.__model = model
        self.__type = type
        self.__color = color
        self.__horsePower = horsePower
        self.__sold = sold

    @property
    def brand(self):
        return self.__brand
    @property
    def model(self):
        return self.__model
    @property
    def type(self):
        return self.__type
    @property
    def color(self):
        return self.__color
    @property
    def horsePower(self):
        return self.__horsePower
    @property
    def sold(self):
        return self.sold

    @brand.setter
    def brand(self, newBrand):
        self.__brand = newBrand
    @model.setter
    def model(self, newModel):
        self.__brand = newModel
    @type.setter
    def type(self, newType):
        self.__type = newType
    @color.setter
    def color(self, newColor):
        self.__color = newColor
    @horsePower.setter
    def horsePower(self, newHorsePower):
        self.__horsePower = newHorsePower
    @sold.setter
    def sold(self, isSold):
        self.__sold = isSold

def addNewCar(brand, model, type, color, hp, sold='false'):

    newCar= AddCar(brand, model, type, color, hp, sold)
    newCar.brand= brand
    newCar.model= model
    newCar.type= type
    newCar.color= color
    newCar.hp= hp

    filename='stock.csv'
    # csv data
    # header = ['brand', 'model', 'type', 'color', 'hp', 'sold']
    data_header = [
       [ brand, model, type, color, hp, sold]
    ]

    try:
        with open(filename, 'a') as file:
         # Create a CSV dictionary writer and add the student header as field names1
            writer = csv.writer(file)
            writer.writerows(data_header)
            return print('Le véhicule a été correctement enregistré\n')
    except FileNotFoundError:
        print('Fichier introuvable.')
    except IOError:
        print('Erreur IO.')
