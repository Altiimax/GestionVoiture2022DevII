import AddCar as addCar
import ShowCars as showStock

int_choice=''

while(int_choice != 0):

      print("Veuillez choisir une option:"
            "\n1 Ajouter un véhicule"
            "\n2 voir le stocke de véhicule"
            "\n0 Sortir du programme")

      choice = input('Votre choix: ')
      int_choice = int(choice)

      if( int_choice == 1):
            brand = input('Entrez une marque: ')
            model = input('Entrez un modèle: ')
            type = input('Entrez un type: ')
            color = input('Entrez la couleur du véhicule: ')
            hp = input('Entrez la puissance du véhicule: ')
            addCar.addNewCar(brand, model, type, color, hp)

      elif(int_choice == 2):
            print(showStock.ShowStock())
