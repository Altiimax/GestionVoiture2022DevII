import Car as addCar
import ShowCars as showStock
import MarkVehicleSold as soldVehicle

int_choice = ''

while int_choice != 0:

    print("Veuillez choisir une option:"
          "\n1 Ajouter un véhicule"
          "\n2 Voir le stock de véhicule"
          "\n3 Chercher un véhicule"
          "\n4 Voir les véhicules vendu"
          "\n5 Marquer un véhicule vendu"
          "\n0 Sortir du programme")

    choice = input('Votre choix: ')
    if choice != '':
        int_choice = int(choice)

    if int_choice == 1:
        brand = input('Entrez une marque: ')
        model = input('Entrez un modèle: ')
        typeVehicle = input('Entrez un type: ')
        color = input('Entrez la couleur du véhicule: ')
        hp = input('Entrez la puissance du véhicule: ')
        addCar.addNewCar(brand, model, type, color, hp)

    elif int_choice == 2:
        print(showStock.ShowStock())

    elif int_choice == 3:
        brand = input('Entrez une marque: ')
        model = input('Entrez un modèle: ')
        typeVehicle = input('Entrez un type: ')
        print(showStock.findCar(brand, model, typeVehicle))

    elif int_choice == 4:
        print(showStock.soldVehicle())

    elif int_choice == 5:
        idVehicle = input('entrez l\'id du véhicule: ')
        print(soldVehicle.markVehicleSold(idVehicle))
