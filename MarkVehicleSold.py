import csv
from tempfile import NamedTemporaryFile
import shutil
import csv

filename = 'stock.csv'
tempfile = NamedTemporaryFile(mode='w', delete=False)

fields = ['brand', 'model', 'typeVehicle', 'color', 'hp', 'sold']


def markVehicleSold(idVehicle):

    try:
        with open(filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            csvreader = csv.reader(filename)
            for row in csvreader:
                print(row[1])
                # if row[6] == idVehicle:
                #     print(row)
                #     print('updating row', row[6])
                #     row['Name'], row['Course'], row['Year'] = stud_name, stud_course, stud_year
                # row = {'ID': row['ID'], 'Name': row['Name'], 'Course': row['Course'], 'Year': row['Year']}
                # writer.writerow(row)

        shutil.move(tempfile.name, filename)


    except FileNotFoundError:
        print('Fichier introuvable.')
    except IOError:
        print('Erreur IO.')
