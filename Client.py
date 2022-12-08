import csv


class Client:
    def __init__(self, id, firstName, lastName, address, city, zip, deleted):
        self.__id = id
        self.__firstName = firstName
        self.__lastName = lastName
        self.__address = address
        self.__city = city
        self.__zip = zip
        self.__deleted = deleted

    @property
    def id(self):
        return self.__id

    @property
    def firstName(self):
        return self.__firstName

    @property
    def lastName(self):
        return self.__lastName

    @property
    def address(self):
        return self.__address

    @property
    def city(self):
        return self.__city

    @property
    def zip(self):
        return self.__zip

    @id.setter
    def id(self, newId):
        self.__id = newId

    @firstName.setter
    def firstName(self, newFirstName):
        self.__firstName = newFirstName

    @lastName.setter
    def lastName(self, newLastName):
        self.__lastName = newLastName

    @address.setter
    def address(self, newAddress):
        self.__address = newAddress

    @city.setter
    def city(self, newCity):
        self.__city = newCity

    @zip.setter
    def zip(self, newZip):
        self.__zip = newZip


def addClient(id, firstName, lastName, address, city, zip, deleted='false'):

    newClient = Client(id, firstName, lastName, address, city, zip, deleted)
    newClient.id = id
    newClient.firstName = firstName
    newClient.lastName = lastName
    newClient.address = address
    newClient.city = city
    newClient.zip = zip
    newClient.deleted = deleted

    filename = 'clients.csv'
    # csv data
    # header = ['brand', 'model', 'typeVehicle', 'color', 'hp', 'sold']
    data_header = [
        [id, firstName, lastName, address, city, zip, deleted]
    ]

    try:
        with open(filename, 'a') as file:
            # Create a CSV dictionary writer and add the student header as field names1
            writer = csv.writer(file)
            writer.writerows(data_header)
            print('Le client a été correctement enregistré\n')
    except FileNotFoundError:
        print('Fichier introuvable.')
    except IOError:
        print('Erreur IO.')
