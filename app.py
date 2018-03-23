import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import DBcm

config = {
    'host': '127.0.0.1',
    'database':'finalproject',
    'user':'root',
    'password':'root',
    }

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: "Create New"
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration  = 1
                root.manager.current = 'create_new'
        Button:
            text: "Check Current"
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'check_current'
        Button:
            text: "Finish + Select Store"
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'finish'
<CreateNewScreen>:
    BoxLayout:
        orientation:"vertical"
        Spinner:
            size_hint_x: 1
            size_hint_y: .1
            text: "Bakery"
            values: ["bread", "buns", "cake", "muffins", "pastries"]
            id: bakery_id
            on_text: root.bakery_spinner_clicked(bakery_id.text)
        Spinner:
            size_hint_x: 1
            size_hint_y: .1
            text: "Fruit"
            values: ["apple", "banana", "grape", "lemon", "melon"]
            id: fruit_id
            on_text: root.fruit_spinner_clicked(fruit_id.text)
        Spinner:
            size_hint_x: 1
            size_hint_y: .1
            text: "Vegetables"
            values: ["artichoke", "broccoli", "carrot", "peas", "sweet potato"]
            id: veg_id
            on_text: root.veg_spinner_clicked(veg_id.text)
        Spinner:
            size_hint_x: 1
            size_hint_y: .1
            text: "Dairy"
            values: ["butter", "cheese", "eggs", "milk", "yogurts"]
            id: dairy_id
            on_text: root.dairy_spinner_clicked(dairy_id.text)
        Spinner:
            size_hint_x: 1
            size_hint_y: .1
            text: "Frozen"
            values: ["chicken burgers", "chips", "frozen veg", "icecream", "pizza"]
            id: frozen_id
            on_text: root.frozen_spinner_clicked(frozen_id.text)
        Spinner:
            size_hint_x: 1
            size_hint_y: .1
            text: "Snacks"
            values: ["biscuits", "chocolate", "crisps", "cordial", "minerals"]
            id: snacks_id
            on_text: root.snacks_spinner_clicked(snacks_id.text)
        Spinner:
            size_hint_x: 1
            size_hint_y: .1
            text: "Hot beverages"
            values: ["coffee beans", "hot chocolate", "herbal tea", "instant coffee", "tea bags"]
            id: hotBev_id
            on_text: root.hotBev_spinner_clicked(hotBev_id.text)
        Spinner:
            size_hint_x: 1
            size_hint_y: .1
            text: "baking essentials"
            values: ["castor sugar", "icing sugar", "mixed peel", "plain flour", "self-raising flour"]
            id: bakEss_id
            on_text: root.bakEss_spinner_clicked(bakEss_id.text)
        Spinner:
            size_hint_x: 1
            size_hint_y: .1
            text: "condiments"
            values: ["brown sauce","gravy","pepper","tomato sauce","vinegar"]
            id: con_id
            on_text: root.con_spinner_clicked(con_id.text)
        Spinner:
            size_hint_x: 1
            size_hint_y: .1
            text: "sauce jars"
            values: ["curry","lasanga","pasta bake","spaghetti bolognese","sweet and sour"]
            id: sauce_id
            on_text: root.sauce_spinner_clicked(sauce_id.text)
        Spinner:
            size_hint_x: 1
            size_hint_y: .1
            text: "Grains"
            values: ["brown rice", "easy cook rice", "lasanga sheets", "noodles", "pasta" ]
            id: grain_id
            on_text: root.grain_spinner_clicked(grain_id.text)
        BoxLayout:
            orientation: "vertical"
            size_hint_x: 1
            Button:
                size_hint_x: 1
                size_hint_y: None
                text: "Main Menu"
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'main_menu'
<ViewCurrentScreen>:
    BoxLayout:
        orientation: "vertical"
        Label:
            font_size: 20
            text: "Check Current"
            color: 0, 0, 0, 1
            size_hint_x: 1
        Button:
            text: "display items"
            on_press: root.get_items()
        Button:
            text: "add more items"
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'create_new'
        Button:
            text: "finish + select store"
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'finish'

<FinishScreen>:
    BoxLayout:
        orientation: "vertical"
        Label:
            font_size: 20
            text: "You were previously at..."
            color: 0, 0, 0, 1
            size_hint_x: 1
        TextInput:
            text: "(previous store)"
        Label:
            font_size: 20
            text: "Would you like to return to this store?"
            color: 0, 0, 0, 1
            size_hint_x: 1
        Button:
            text: "Yes"
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'view_finish'
        Button:
            text: "No, select another store"
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'select_store'
<SelectStoreScreen>:
    BoxLayout:
        orientation: "vertical"
        Spinner:
            size_hint_x: 1
            size_hint_y: .4
            text: "County"
            values: ["Carlow", "Dublin", "Kilkenny", "Wicklow", "Wexford"]
            id: county_id
            on_text: root.county_clicked(county_id.text)
        Spinner:
            size_hint_x: 1
            size_hint_y: .4
            text: "Town"
            values: ["dropdown depending on selection above"]
            id: town_id
            on_text: root.get_towns()
        Spinner:
            size_hint_x: 1
            size_hint_y: .4
            text: "Store"
            values: ["dropdown depending on selection above"]
            id: store_id
            on_text: root.store_clicked(store_id.text)
        BoxLayout:
            orientation: "vertical"
            size_hint_x: 1
            Button:
                size_hint_x: 1
                size_hint_y: None
                text: "Main Menu"
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'main_menu'
""")

class MenuScreen(Screen):
    pass

class CreateNewScreen(Screen):
    
    def bakery_spinner_clicked(self, value):
        print("Bakery value " + value)
            #item = value
            #amount = 1
            #with DBcm
       # item = value
        #amount = 1
        #with DBcm.UseDatabase(config) as cursor:
        #   _SQL = """INSERT INTO selecteditems (itemName, quantity) values (%s, %s) """
           # cursor.execute(_SQL, (item, amount))
    def fruit_spinner_clicked(self, value):
        print("Fruit value " + value)

    def veg_spinner_clicked(self, value):
        print("Veg value " + value)

    def dairy_spinner_clicked(self, value):
        print("Dairy value " + value)

    def frozen_spinner_clicked(self, value):
        print("Frozen value " + value)

    def snacks_spinner_clicked(self, value):
        print("Snack value " + value)

    def hotBev_spinner_clicked(self, value):
       print("Hot beverage value " + value)

    def bakEss_spinner_clicked(self, value):
       print("Baking essentials value " + value)

    def con_spinner_clicked(self, value):
       print("Condiments value " + value)

    def sauce_spinner_clicked(self, value):
       print("Sauce value " + value)

    def grain_spinner_clicked(self, value):
       print("Grain value " + value)
    
    
    
    
    
     
class ViewCurrentScreen(Screen):
    pass
    #def get_items(self):
     #   with DBcm.UseDatabase(config) as cursor:
      #      result = cursor.execute("""SELECT itemName FROM selecteditems""")
       #     response = [row[0] for row in result.fetchall()]
        #    print(result)
            #response = [row[0] for row in result.fetchall()]
        

class FinishScreen(Screen):
    pass

class SelectStoreScreen(Screen):
      def county_clicked(self, value):
        print("County value " + value)
        countyValue = value

      def get_towns(self):
          with DBcm.UseDatabase(config) as cursor:
              cursor.execute("""SELECT storeTown FROM store WHERE storeCounty = countyValue""")
              rows = cursor.fetchall()
              self.label_lang.values = map(str, rows)
      def town_clicked(self, value):
        print("Town value " + value)

      def store_clicked(self, value):
        print("Store value " + value)
        
screen_manager = ScreenManager()

screen_manager.add_widget(MenuScreen(name="main_menu"))
screen_manager.add_widget(CreateNewScreen(name="create_new"))
screen_manager.add_widget(ViewCurrentScreen(name="check_current"))
screen_manager.add_widget(FinishScreen(name="finish"))
screen_manager.add_widget(SelectStoreScreen(name="select_store"))

class ScreenApp(App):
    def build(self):

        #set background colour for the window
        Window.clearcolor = (1,1,1,1)
        return screen_manager

sample_app = ScreenApp()
sample_app.run()
