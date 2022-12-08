import csv
from tempfile import NamedTemporaryFile
import shutil
import csv

filename = 'stock.csv'
tempfile = NamedTemporaryFile(mode='w', delete=False)

fields = ['brand', 'model', 'typeVehicle', 'color', 'hp', 'sold']


def markVehicleSold(idVehicle):

    try:
        with open(filename, 'r') as file:
            # reader = csv.DictReader(csvfile, fieldnames=fields)
            # writer = csv.DictWriter(tempfile, fieldnames=fields)
            csvreader = csv.reader(filename)
            for row in csvreader:
                if len(row) == 6:  # add this check
                    print(row)
    except FileNotFoundError:
        print('Fichier introuvable.')
    except IOError:
        print('Erreur IO.')
