import csv

fileName = 'clients.csv'


def listClient():
    try:
        with open(fileName, 'r') as file:
            csvreader = csv.reader(file)

            for row in csvreader:
                if len(row) == 7:  # add this check
                    print('id:', row[0], 'prénom:', row[1], 'nom:', row[2],
                          'adresse:', row[3], 'ville :', row[4], 'code postal:', row[5])
                # else:
                #     print('Aucun véhicule dans le stock')

    except FileNotFoundError:
        print('Fichier introuvable.')
    except IOError:
        print('Erreur IO.')


def findClient(id, firstName, lastName):
    try:
        with open(fileName, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if len(row) == 7:  # add this check
                    if row[0] == id or row[1] == firstName or row[2] == lastName:
                        print('identifiant:', row[0], 'prénom:', row[1], 'nom:', row[2],
                              'adresse :', row[3], 'ville (CV) :', row[4], 'code postal:', row[5])
                # else:
                #     print('Aucun véhicule dans le stock')

    except FileNotFoundError:
        print('Fichier introuvable.')
    except IOError:
        print('Erreur IO.')
