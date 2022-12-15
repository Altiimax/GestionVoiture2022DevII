from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import Car as addCar
import Client as newClient
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

        return self.window

    def stock(self, instance):
        showStock.ShowStock()
        # self.greeting.text = "Hello " + self.user.text + "!"

    def soldVehicle(self, instance):
        showStock.soldVehicle()

    def client(self, instance):
        showClient.listClient()
        # self.greeting.text = "Hello " + self.user.text + "!"

    def addVehicle(self, instance):
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
        self.send.bind(on_press=self.sendVehicleAdd)
        self.window.add_widget(self.send)

        self.window.add_widget(self.brand)
        self.window.add_widget(self.model)
        self.window.add_widget(self.typeVehicle)
        self.window.add_widget(self.color)
        self.window.add_widget(self.hp)

    def sendVehicleAdd(self, instance):
        addCar.addNewCar(self.brand.text, self.model.text, self.typeVehicle.text, self.color.text, self.hp.text)
        print(self.brand.text)
        print(self.model.text)
        print(self.typeVehicle.text)
        print(self.color.text)
        print(self.hp.text)

# run Start class
if __name__ == "__main__":
    Start().run()
