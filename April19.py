import kivy
import urllib.request
import requests

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import DBcm

getItemsURL = 'https://www.pythonanywhere.com/getItemsCheck'
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
            values: ["apples", "bananas", "grapes", "lemons", "melons"]
            id: fruit_id
            on_text: root.fruit_spinner_clicked(fruit_id.text)
        Spinner:
            size_hint_x: 1
            size_hint_y: .1
            text: "Vegetables"
            values: ["artichokes", "broccoli", "carrots", "peas", "sweet potato"]
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
            values: ["chicken burgers", "chips", "frozen veg", "icecreaam", "pizza"]
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
                size_hint_y: .2
                text: "Start List"
                on_press: root.start()
            Button:
                size_hint_x: 1
                size_hint_y: None
                text: "Submit"
                on_press: root.submit_items()
            Button:
                size_hint_x: 1
                size_hint_y: .2
                text: "Main Menu"
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'main_menu'
            Button:
                size_hint_x: 1
                size_hint_y: .2
                text: "Check Current"
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'check_current'
            Button:
                size_hint_x: 1
                size_hint_y: .2
                text: "Select Store"
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'finish'
<ViewCurrentScreen>:
    button : button
    box : box
    BoxLayout:
        orientation: "vertical"
        Label:
            font_size: 20
            text: "Check Current"
            size_hint_x: 1
        Button:
            id: button
            text: "display items"
            on_release: root.get_items()
        BoxLayout:
            id: box
            size_hint_y: 0.9
            orientation: "vertical"
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
            size_hint_x: 1
        TextInput:
            text: "Carlow, Hanover Rd"
        Label:
            font_size: 20
            text: "Would you like to return to this store?"
            size_hint_x: 1
        Button:
            text: "Yes"
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'view_finish'
        Button:
            text: "No, select another store"
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'select_store'
        Button:
            size_hint_x: 1
            size_hint_y: None
            text: "Main Menu"
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'main_menu'
<SelectStoreScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            size_hint_x: 1
            size_hint_y: None
            text: "Start"
            on_press: root.start()
        Spinner:
            size_hint_x: 1
            size_hint_y: .4
            text: "County"
            values: ["Carlow"]
            id: county_id
            on_text: root.county_clicked(county_id.text)
        Spinner:
            size_hint_x: 1
            size_hint_y: .4
            text: "Town"
            values: ["Carlow"]
            id: town_id
            on_text: root.town_clicked(town_id.text)
        Spinner:
            size_hint_x: 1
            size_hint_y: .4
            text: "Store"
            values: ["Aldi, Hanover Rd", "Dunnes Stores, 5 Sleaty Rd", "Lidl, Tullow Rd", "Supervalu, Sandhill Shopping Centre", "Tesco, Fairgreen Shopping Centre"]
            id: store_id
            on_text: root.store_clicked(store_id.text)
        Button:
            size_hint_x: 1
            size_hint_y: None
            text: "Submit"
            on_press: root.submit()
        BoxLayout:
            orientation: "vertical"
            size_hint_x: 1
            Button:
                size_hint_x: 1
                size_hint_y: None
                text: "View Finished List"
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'view_finish'

<ViewFinishScreen>:
    button : button
    box : box
    BoxLayout:
        orientation: "vertical"
        Label:
            font_size: 20
            text: "Your current list of items"
            size_hint_x: 1
        Button:
            id: button
            text: "display items"
            on_release: root.match_items()
        BoxLayout:
            id: box
            size_hint_y: 0.9
            orientation: "vertical"  
        BoxLayout:
            orientation: "vertical"
            size_hint_x: 1
            Button:
                size_hint_x: 1
                size_hint_y: None
                text: "Report a Change"
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'report_change'

<ReportChangeScreen>:
    BoxLayout:
        orientation: "vertical"
        Label:
            font_size: 20
            text: "Report a Change"
            size_hint_x: 1
            size_hint_y: .1
        Button:
            size_hint_x: 1
            size_hint_y: None
            text: "Start"
            on_press: root.start()
        TextInput:
            size_hint_x: 1
            size_hint_y: .2
            text: "item changed"
            id: reportChangeItem_id
            on_text: root.item_change(reportChangeItem_id.text)
        Spinner:
            size_hint_x: 1
            size_hint_y: .4
            text: "moved from aisle: "
            values: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
            id: fromLocation_id
            on_text: root.from_location(fromLocation_id.text)
        Spinner:
            size_hint_x: 1
            size_hint_y: .4
            text: "moved to aisle: "
            values: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
            id: toLocation_id
            on_text: root.to_location(toLocation_id.text)
        BoxLayout:
            orientation: "vertical"
            size_hint_x: 1
            Button:
                size_hint_x: 1
                size_hint_y: None
                text: "submit"
                on_press: root.submit_items()
            Button:
                size_hint_x: 1
                size_hint_y: None
                text: "Return to list"
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'view_finish'     
""")

class MenuScreen(Screen):
    pass

#####################################
class CreateNewScreen(Screen):
    def start(self):   
        self.materials = {}
        
    def bakery_spinner_clicked(self, value):
        quantity = 1
        self.materials[value] = quantity
       
    def fruit_spinner_clicked(self, value):
        quantity = 1
        self.materials[value] = quantity

    def veg_spinner_clicked(self, value):
        quantity = 1
        self.materials[value] = quantity

    def dairy_spinner_clicked(self, value):
        quantity = 1
        self.materials[value] = quantity

    def frozen_spinner_clicked(self, value):
        quantity = 1
        self.materials[value] = quantity

    def snacks_spinner_clicked(self, value):
        quantity = 1
        self.materials[value] = quantity
        
    def hotBev_spinner_clicked(self, value):
        quantity = 1
        self.materials[value] = quantity

    def bakEss_spinner_clicked(self, value):
        quantity = 1
        self.materials[value] = quantity

    def con_spinner_clicked(self, value):
        quantity = 1
        self.materials[value] = quantity

    def sauce_spinner_clicked(self, value):
        quantity = 1
        self.materials[value] = quantity

    def grain_spinner_clicked(self, value):
        quantity = 1
        self.materials[value] = quantity

    def submit_items(self):
        payload = self.materials
        r = requests.post("http://moorej.pythonanywhere.com/receiveItems", data=payload)
        print(r.text)
        
################################         
class ViewCurrentScreen(Screen):
    def get_items(self):
        with urllib.request.urlopen('http://moorej.pythonanywhere.com/getItemsCheck') as response:
            items = response.read()
        items = str(items)

        self.box.add_widget(
            Label(text='{0}'.format(items)))
   
#############################################
class FinishScreen(Screen):
    pass

##########################################
class SelectStoreScreen(Screen):
    def start(self):
        self.storeChoice = {}
        
    def county_clicked(self, value):
        value = str(value)
        self.storeChoice['county'] = value
        
    def town_clicked(self, value):
        value = str(value)
        self.storeChoice['town'] = value

    def store_clicked(self, value):
        value = str(value)
        self.storeChoice['store'] = value

    def submit(self):
        payload = self.storeChoice
        r = requests.post("http://moorej.pythonanywhere.com/selectStore", data=payload)
        print(r.text)

##########################################
class ViewFinishScreen(Screen):
    def match_items(self):
        with urllib.request.urlopen('http://moorej.pythonanywhere.com/matchItems') as response:
            l = response.read()

        l = str(l)
        self.box.add_widget(
            Label(text='{0}'.format(l)))
           
            
########################################
class ReportChangeScreen(Screen):
    def start(self):   
        self.report = {}
      
    def item_change(self, value):
        value = str(value)
        value = value.lower()
        self.report['itemChanged'] = value
        
    def from_location(self, value):
        value = int(value)
        self.report['locationFrom'] = value
        
    def to_location(self, value):
        value = int(value)
        self.report['locationTo'] = value

    def submit_items(self):
        payload = self.report
        r = requests.post("http://moorej.pythonanywhere.com/reportChange", data=payload)
        print(r.text)

##########################################################################################
        
screen_manager = ScreenManager()

screen_manager.add_widget(MenuScreen(name="main_menu"))
screen_manager.add_widget(CreateNewScreen(name="create_new"))
screen_manager.add_widget(ViewCurrentScreen(name="check_current"))
screen_manager.add_widget(FinishScreen(name="finish"))
screen_manager.add_widget(SelectStoreScreen(name="select_store"))
screen_manager.add_widget(ViewFinishScreen(name="view_finish"))
screen_manager.add_widget(ReportChangeScreen(name="report_change"))

class ScreenApp(App):
    def build(self):

        #set background colour for the window
        #Window.clearcolor = (1,1,1,1)
        return screen_manager

sample_app = ScreenApp()
sample_app.run()
