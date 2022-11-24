import csv

def ShowStock():
    try:
        with open("stock.csv", 'r') as file:
            csvreader = csv.reader(file)

            for row in csvreader:
                if len(row) == 6:    #add this check
                    print('marque:', row[0], 'modèle:', row[1], 'type:', row[2],
                      'couleur:', row[3],'puissance (CV) :', row[4], 'vendue:', row[5])

    except FileNotFoundError:
        print('Fichier introuvable.')
    except IOError:
        print('Erreur IO.')



