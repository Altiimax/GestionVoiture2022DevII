from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import Car as addCar
import Client
import ShowCars as showStock
import ShowClients as showClient


class Start(App):

    def build(self):
        # Affichage de la fenetre avec tout les éléments
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # image widget
        # self.window.add_widget(Image(source="Image/"))

        # label widget
        self.greeting = Label(
            text="Bienvenue dans le programme de gestion de véhicule",
            font_size=18,
            color='#00FFCE'
        )
        self.window.add_widget(self.greeting)

        # button Ajout véhicule
        self.vehicle = Button(
            text="Ajouter un véhicule",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFCE',
            # remove darker overlay of background colour
            # background_normal = ""
        )
        self.vehicle.bind(on_press=self.addVehicle)
        self.window.add_widget(self.vehicle)

        # button stock
        self.showStock = Button(
            text="Voir Le stock",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFCE',
            # remove darker overlay of background colour
            # background_normal = ""
        )
        self.showStock.bind(on_press=self.stock)
        self.window.add_widget(self.showStock)

        # button soldVehicle
        self.vehicleSold = Button(
            text="Voir les véhicules vendus",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFCE',
            # remove darker overlay of background colour
            # background_normal = ""
        )
        self.vehicleSold.bind(on_press=self.soldVehicle)
        self.window.add_widget(self.vehicleSold)

        # button listClient
        self.showClient = Button(
            text="Voir les clients",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFCE',
            # remove darker overlay of background colour
            # background_normal = ""
        )
        self.showClient.bind(on_press=self.client)
        self.window.add_widget(self.showClient)

        # button listClient
        self.newClient = Button(
            text="Ajouter un nouveau client",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFCE',
            # remove darker overlay of background colour
            # background_normal = ""
        )
        self.newClient.bind(on_press=self.addClient)
        self.window.add_widget(self.newClient)

        return self.window

    def stock(self, instance):
        showStock.ShowStock()
        # l = Label(text='Stock :', markup=True)
        # self.window.add_widget()

    def soldVehicle(self, instance):
        showStock.soldVehicle()

    def addClient(self, instance):
        Client.addClient()
        self.idTitle = Label(
            text="identifiant : ",
            font_size=14,
            color='#00FFCE'
        )
        self.firstNamelTitle = Label(
            text="Prénom : ",
            font_size=14,
            color='#00FFCE'
        )

        self.lastNameTitle = Label(
            text="Nom : ",
            font_size=14,
            color='#00FFCE'
        )
        self.addressTitle = Label(
            text="adresse : ",
            font_size=14,
            color='#00FFCE'
        )
        self.cityTitle = Label(
            text="Ville : ",
            font_size=14,
            color='#00FFCE'
        )
        self.zipTitle = Label(
            text="Code postal : ",
            font_size=14,
            color='#00FFCE'
        )
        self.id = TextInput(
            multiline=False,
            padding_y=(10, 10),
            size_hint=(1, 0.5)
        )
        self.firstName = TextInput(
            multiline=False,
            padding_y=(10, 10),
            size_hint=(1, 0.5)
        )
        self.lastName = TextInput(
            multiline=False,
            padding_y=(10, 10),
            size_hint=(1, 0.5)
        )
        self.address = TextInput(
            multiline=False,
            padding_y=(10, 10),
            size_hint=(1, 0.5)
        )
        self.city = TextInput(
            multiline=False,
            padding_y=(10, 10),
            size_hint=(1, 0.5)
        )
        self.zip = TextInput(
            multiline=False,
            padding_y=(10, 10),
            size_hint=(1, 0.5)
        )

        self.send = Button(
            text="Enregistrer le client",
            size_hint=(0.5, 0.5),
            bold=True,
            background_color='red',

        )
        self.window.add_widget(self.idTitle)
        self.window.add_widget(self.id)
        self.window.add_widget(self.firstNamelTitle)
        self.window.add_widget(self.firstName)
        self.window.add_widget(self.lastNameTitle)
        self.window.add_widget(self.lastName)
        self.window.add_widget(self.addressTitle)
        self.window.add_widget(self.address)
        self.window.add_widget(self.cityTitle)
        self.window.add_widget(self.city)
        self.window.add_widget(self.zipTitle)
        self.window.add_widget(self.zip)
        self.send.bind(on_press=self.sendClient)
        self.window.add_widget(self.send)

        return self.window


    def client(self, instance):
        showClient.listClient()


    def addVehicle(self, instance):
        self.brandTitle = Label(
        text="Marque : ",
        font_size=14,
        color='#00FFCE'
        )
        self.modelTitle = Label(
        text="Modèle : ",
        font_size=14,
        color='#00FFCE'
        )
        self.typeTitle = Label(
        text="Type de véhicule : ",
        font_size=14,
        color='#00FFCE'
        )
        self.colorTitle = Label(
        text="Couleur : ",
        font_size=14,
        color='#00FFCE'
        )
        self.hpTitle = Label(
        text="Puissance (cv) : ",
        font_size=14,
        color='#00FFCE'
        )
        self.brand = TextInput(
        multiline=False,
        padding_y=(10, 10),
        size_hint=(1, 0.5)
        )
        self.model = TextInput(
        multiline=False,
        padding_y=(10, 10),
        size_hint=(1, 0.5)
        )
        self.typeVehicle = TextInput(
        multiline=False,
        padding_y=(10, 10),
        size_hint=(1, 0.5)
        )
        self.color = TextInput(
        multiline=False,
        padding_y=(10, 10),
        size_hint=(1, 0.5)
        )
        self.hp = TextInput(
        multiline=False,
        padding_y=(10, 10),
        size_hint=(1, 0.5)
        )

        self.send = Button(
        text="Ajouter véhicule au stock",
        size_hint=(0.5, 0.5),
        bold=True,
        background_color='red',

        )
        self.window.add_widget(self.brandTitle)
        self.window.add_widget(self.brand)
        self.window.add_widget(self.modelTitle)
        self.window.add_widget(self.model)
        self.window.add_widget(self.typeTitle)
        self.window.add_widget(self.typeVehicle)
        self.window.add_widget(self.colorTitle)
        self.window.add_widget(self.color)
        self.window.add_widget(self.hpTitle)
        self.window.add_widget(self.hp)
        self.send.bind(on_press=self.sendVehicleAdd)
        self.window.add_widget(self.send)

        return self.window


    def sendVehicleAdd(self, instance):
        addCar.addNewCar(self.brand.text, self.model.text, self.typeVehicle.text, self.color.text, self.hp.text)

    def sendClient(self, instance):
        Client.addClient(self.id.text, self.firstName.text, self.lastName.text, self.address.text, self.city.text, self.zip.text)


# run Start class
if __name__ == "__main__":
    Start().run()
