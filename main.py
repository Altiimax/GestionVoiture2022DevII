import Car as addCar
import Client as newClient
import ShowCars as showStock
import ShowClients as showClient

int_choice = ''

while int_choice != 0:

    print("Veuillez choisir une option:"
          "\n1 Ajouter un véhicule"
          "\n2 Voir le stock de véhicule"
          "\n3 Chercher un véhicule"
          "\n4 Voir les véhicules vendu"
          "\n6 Ajouter un client"
          "\n7 Consulter la liste des clients"
          "\n8 Rechercher un client"
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

    elif int_choice == 6:
        id = input('Entrez un identifiant unique: ')
        firstName = input('Prénom: ')
        lastName = input('Nom: ')
        address = input('Adresse: ')
        city = input('Ville: ')
        zip = input('Code postal: ')
        newClient.addClient(id, firstName, lastName, address, city, zip)

    elif int_choice == 7:
        print(showClient.listClient())

    elif int_choice == 8:
        id = input('Identifiant: ')
        firstName = input('Prénom: ')
        lastName = input('Nom: ')
        print(showClient.findClient(id, firstName, lastName))


