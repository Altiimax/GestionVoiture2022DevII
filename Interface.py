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
        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # image widget
        # self.window.add_widget(Image(source="Image/"))

        # label widget
        self.greeting = Label(
            text= "Bienvenue dans le programme de gestion de véhicule",
            font_size= 18,
            color= '#00FFCE'
        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
            multiline= False,
            padding_y= (20,20),
            size_hint= (1, 0.5)
        )

        self.window.add_widget(self.user)

        # button stock
        self.showStock = Button(
            text= "Voir Le stock",
            size_hint= (1,0.5),
            bold= True,
            background_color ='#00FFCE',
            #remove darker overlay of background colour
            # background_normal = ""
        )
        self.showStock.bind(on_press=self.stock)
        self.window.add_widget(self.showStock)

        # button soldVehicle
        self.vehichleSold = Button(
            text= "Voir les véhicules vendus",
            size_hint= (1,0.5),
            bold= True,
            background_color ='#00FFCE',
            #remove darker overlay of background colour
            # background_normal = ""
        )
        self.vehichleSold.bind(on_press=self.soldVehicle)
        self.window.add_widget(self.vehichleSold)

        # button listClient
        self.showClient = Button(
            text= "Voir les clients",
            size_hint= (1,0.5),
            bold= True,
            background_color ='#00FFCE',
            #remove darker overlay of background colour
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

# run Say Hello App Calss
if __name__ == "__main__":
    Start().run()
