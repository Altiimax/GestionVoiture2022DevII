import csv
import pandas as pd

filename = 'stock.csv'

def ShowStock():
    try:
        with open(filename, 'r') as file:
            csvreader = csv.reader(file)

            for row in csvreader:
                if len(row) == 7:  # add this check
                    print('id:', row[0], 'marque:', row[1], 'modèle:', row[2], 'type:', row[3],
                          'couleur:', row[4], 'puissance (CV) :', row[5], 'vendue:', row[6])
                # else:
                #     print('Aucun véhicule dans le stock')

    except FileNotFoundError:
        print('Fichier introuvable.')
    except IOError:
        print('Erreur IO.')


def findCar(brand, model, typeVehicle):
    try:
        with open(filename, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if len(row) == 7:  # add this check
                    if row[1] == brand or row[2] == model or row[3] == typeVehicle:
                        print('id:', row[0], 'marque:', row[1], 'modèle:', row[2], 'type:', row[3],
                              'couleur:', row[4], 'puissance (CV) :', row[5], 'vendue:', row[6])
                # else:
                #     print('Aucun véhicule dans le stock')

    except FileNotFoundError:
        print('Fichier introuvable.')
    except IOError:
        print('Erreur IO.')


def soldVehicle():
    count = 0
    try:
        with open(filename, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if len(row) == 7:
                    if row[6] == 'true':
                        count += 1
                        print('id:', row[0], 'marque:', row[1], 'modèle:', row[2], 'type:', row[3],
                              'couleur:', row[4], 'puissance (CV) :', row[5], 'vendue:', row[6])
        return count
                # else:
                #     print('Aucun véhicule dans le stock')

    except FileNotFoundError:
        print('Fichier introuvable.')
    except IOError:
        print('Erreur IO.')


def markVehicleSold(idVehicle):
    try:
        with open(filename, 'r') as file:
            csvreader = csv.reader(file)

            for row in csvreader:
                if len(row) == 7:  # add this check
                    if(row[0] == idVehicle and row[6] == 'false'):
                        print(row)
                        # print('id:', row[0], 'marque:', row[1], 'modèle:', row[2], 'type:', row[3],
                        #   'couleur:', row[4], 'puissance (CV) :', row[5], 'vendue:', row[6])
                    elif(row[0] == idVehicle and row[6] == 'true'):
                        print('Le véhicule identifier : ' + idVehicle + ' est déjà vendu')

    except FileNotFoundError:
        print('Fichier introuvable.')
    except IOError:
        print('Erreur IO.')


