import csv


class Car:
    def __init__(self, brand, model, typeVehicleVehicle, color, horsePower, sold):
        self.__brand = brand
        self.__model = model
        self.__typeVehicle = typeVehicleVehicle
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
    def typeVehicle(self):
        return self.__typeVehicle

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

    @typeVehicle.setter
    def typeVehicle(self, newtypeVehicle):
        self.__typeVehicle = newtypeVehicle

    @color.setter
    def color(self, newColor):
        self.__color = newColor

    @horsePower.setter
    def horsePower(self, newHorsePower):
        self.__horsePower = newHorsePower

    @sold.setter
    def sold(self, isSold):
        self.__sold = isSold


def addNewCar(brand, model, typeVehicle, color, hp, sold='false'):

    newCar = Car(brand, model, typeVehicle, color, hp, sold)
    newCar.brand = brand
    newCar.model = model
    newCar.typeVehicle = typeVehicle
    newCar.color = color
    newCar.hp = hp

    filename = 'stock.csv'
    # csv data
    # header = ['brand', 'model', 'typeVehicle', 'color', 'hp', 'sold']
    data_header = [
       [brand, model, typeVehicle, color, hp, sold]
    ]

    try:
        with open(filename, 'a') as file:
            # Create a CSV dictionary writer and add the student header as field names1
            writer = csv.writer(file)
            writer.writerows(data_header)
            print('Le véhicule a été correctement enregistré\n')
    except FileNotFoundError:
        print('Fichier introuvable.')
    except IOError:
        print('Erreur IO.')
