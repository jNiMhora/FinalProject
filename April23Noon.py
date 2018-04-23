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

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation: "vertical"
        Label:
            size_hint_x: 1
            size_hint_y: .3
            text: "Enter Your E-mail Address Below;"
        TextInput:
            color: 0,0,0,1
            size_hint_x: 1
            size_hint_y: .2
            id: email_id
            on_text: root.email_entered(email_id.text)
            focus: True
        Button:
            text: "Create New List"
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration  = 1
                root.manager.current = 'create_new'
        Button:
            text: "Check Current List"
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
        size_hint_x: 1
        sie_hint_y: 4
        Label:
            size_hint_x: 1
            size_hint_y: .3
            text:"Select Your Items From the Lists Below"
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
            size_hint_y: .5
            Label:
                size_hint_x: 1
                size_hint_y: .1
            Button:
                size_hint_x: 1
                size_hint_y: .2
                text: "Main Menu"
                on_press:
                    root.submit_items()
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'main_menu'
            Button:
                size_hint_x: 1
                size_hint_y: .2
                text: "Check Current List"
                on_press:
                    root.submit_items()
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'check_current'
            Button:
                size_hint_x: 1
                size_hint_y: .2
                text: "Finish + Select Store"
                on_press:
                    root.submit_items()
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'finish'
                    
<ViewCurrentScreen>:
    button : button
    box : box
    BoxLayout:
        orientation: "vertical"
        Label:
            size_hint_x: 1
            size_hint_y: .3
            text: "Your Current Items;"
        Button:
            size_hint_x: 1
            size_hint_y: .5
            id: button
            text: "Press Here to see your Current List of Items"
            on_release: root.get_items()
        BoxLayout:
            id: box
            size_hint_x: 1
            size_hint_y: 4
            orientation: "vertical"
        Button:
            text: "Add More Items"
            size_hint_x: 1
            size_hint_y: .5
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'create_new'
        Button:
            text: "Finish + Select Store"
            size_hint_x: 1
            size_hint_y: .5
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'finish'

<FinishScreen>:
    button : button
    box : box
    BoxLayout:
        orientation: "vertical"
        Label:
            size_hint_x: 1
            size_hint_y: .3
            text: "Choose Your Store;"
        Button:
            id: button
            text: "Press Here to see your Previous Store"
            on_release: root.get_store()
        BoxLayout:
            id: box
            size_hint_y: 0.9
            orientation: "vertical"
        Label:
            size_hint_x: 1
            size_hint_y: .3
            text: "Would You Like to Return to this Store?"
        Button:
            text: "Yes"
            on_release: root.return_to_store()
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'view_finish'
        Label:
            size_hint_x: 1
            size_hint_y: .1
        Button:
            text: "No, Select Another Store"
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'select_store'
                
<SelectStoreScreen>:
    BoxLayout:
        orientation: "vertical"
        Label:
            size_hint_x: 1
            size_hint_y: .3
            text: "Select Your Store From the Lists Below;"
        Spinner:
            size_hint_x: 1
            size_hint_y: .3
            text: "Town"
            values: ["Carlow"]
            id: town_id
            on_text: root.town_clicked(town_id.text)
        Spinner:
            size_hint_x: 1
            size_hint_y: .3
            text: "Store"
            values: ["Aldi, Hanover Rd", "Dunnes Stores, 5 Sleaty Rd", "Lidl, Tullow Rd", "Supervalu, Sandhill Shopping Centre", "Tesco, Fairgreen Shopping Centre"]
            id: store_id
            on_text: root.store_clicked(store_id.text)
        Label:
            size_hint_x: 1
            size_hint_y: .5
        Button:
            size_hint_x: 1
            size_hint_y: .3
            text: "View Shopping List"
            on_press:
                root.submit()
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'view_finish'

<ViewFinishScreen>:
    button : button
    box : box
    BoxLayout:
        orientation: "vertical"
        Label:
            size_hint_x: 1
            size_hint_y: .3
            text: "Your Shopping List;"
        Button:
            id: button
            text: "Press Here to see Your Shopping List"
            on_release: root.match_items()
        Label:
            text:"ITEM : AISLE NO"
        BoxLayout:
            id: box
            size_hint_y: 4
            orientation: "vertical"  
        BoxLayout:
            orientation: "vertical"
            size_hint_x: 1
            Button:
                size_hint_x: 1
                size_hint_y: .3
                text: "Report a Change"
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'report_change'
            Button:
                size_hint_x: 1
                size_hint_y: .3
                text: "Finished"
                on_press:
                    root.delete_items()
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'complete'            

<ReportChangeScreen>:
    BoxLayout:
        orientation: "vertical"
        Label:
            size_hint_x: 1
            size_hint_y: .3
            text: "Enter the Item that has moved;"
        TextInput:
            size_hint_x: 1
            size_hint_y: .2
            color: 0,0,0,1
            focus: True
            id: reportChangeItem_id
            on_text: root.item_change(reportChangeItem_id.text)
        Spinner:
            size_hint_x: 1
            size_hint_y: .3
            text: "moved from aisle: "
            values: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
            id: fromLocation_id
            on_text: root.from_location(fromLocation_id.text)
        Spinner:
            size_hint_x: 1
            size_hint_y: .3
            text: "moved to aisle: "
            values: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
            id: toLocation_id
            on_text: root.to_location(toLocation_id.text)
        Label:
            size_hint_x: 1
            size_hint_y: .1
        BoxLayout:
            orientation: "vertical"
            size_hint_x: 1
            Button:
                size_hint_x: 1
                size_hint_y: None
                text: "Submit + Return to List"
                on_press:
                    root.submit_items()
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'view_finish'
                    
<CompleteScreen>:
    BoxLayout:
        orientation: "vertical"
        Label:
            size_hint_x: 1
            size_hint_y: 2
        Button:
            size_hint_x: 1
            size_hint_y: 2
            text: "Finished! Return to Main Menu"
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'main_menu'
        Label:
            size_hint_x: 1
            size_hint_y: 2
                    
""")
#setting up global email variable and accessible dictionaries
email=''
materials = {}
storeChoice = {}
report = {}

class MenuScreen(Screen):
    def email_entered(self,value):
        #sets the global variable to have the value entered
        global email      
        email = str(value)

#####################################
class CreateNewScreen(Screen):
    # each function here is connected to a category and saves the items selected to a dictionary   
    def bakery_spinner_clicked(self, value):
        userid = str(email)
        #this gives the email in a useful format for saving to the database and using as an identifier
        materials[value] = userid
       
    def fruit_spinner_clicked(self, value):
        userid = str(email)
        materials[value] = userid
        
    def veg_spinner_clicked(self, value):
        userid = str(email)
        materials[value] = userid

    def dairy_spinner_clicked(self, value):
        userid = str(email)
        materials[value] = userid

    def frozen_spinner_clicked(self, value):
        userid = str(email)
        materials[value] = userid

    def snacks_spinner_clicked(self, value):
        userid = str(email)
        materials[value] = userid
        
    def hotBev_spinner_clicked(self, value):
        userid = str(email)
        materials[value] = userid

    def bakEss_spinner_clicked(self, value):
        userid = str(email)
        materials[value] = userid

    def con_spinner_clicked(self, value):
        userid = str(email)
        materials[value] = userid

    def sauce_spinner_clicked(self, value):
        userid = str(email)
        materials[value] = userid

    def grain_spinner_clicked(self, value):
        userid = str(email)
        materials[value] = userid

    #this function sends the dictionary created by the users choices in drop downs to the database
    def submit_items(self):
        payload = materials
        r = requests.post("http://moorej.pythonanywhere.com/receiveItems", data=payload)
        
#############################################################################
class ViewCurrentScreen(Screen):
    def get_items(self):
        self.email = {}
        userid = str(email)
        self.email['userid'] = userid#creating a dictionary for the identifier
        payload = self.email
        r = requests.post("http://moorej.pythonanywhere.com/getItemsCheck", data=payload)
        #returns a string to be displayed
        items = str(r.text)
        items = items.split('/')
        for i in items:
            self.box.add_widget(
                Label(text='{0}'.format(i)))
   
###############################################################################
class FinishScreen(Screen):
    def get_store(self):
        self.email = {}
        userid = str(email)
        self.email['userid'] = userid
        payload = self.email
        r = requests.post("http://moorej.pythonanywhere.com/getPrevStore", data=payload)
        #returns the users previous choice of store if available
        store = str(r.text)
        self.box.add_widget(
            Label(text='{0}'.format(store)))

    #activated if the user wants to return to their previous store, and this choice is saved
    def return_to_store(self):
        self.email = {}
        userid = str(email)
        self.email['userid'] = userid
        payload = self.email
        r = requests.post("http://moorej.pythonanywhere.com/returningToStore", data=payload)
    
##########################################
class SelectStoreScreen(Screen):
    #connected to drop downs to find the users choice of store   
    def town_clicked(self, value):
        value = str(value)
        storeChoice['town'] = value

    def store_clicked(self, value):
        value = str(value)
        storeChoice['store'] = value

    def submit(self):
        userid = str(email)
        storeChoice['userid'] = userid
        payload = storeChoice
        r = requests.post("http://moorej.pythonanywhere.com/selectStore", data=payload)
        

##########################################
class ViewFinishScreen(Screen):
    def match_items(self):
        self.email = {}
        userid = str(email)
        self.email['userid'] = userid
        payload = self.email
        #call to find the list of items and their associated aisle numbers from the database
        r = requests.post("http://moorej.pythonanywhere.com/matchItems", data=payload)
        shoppingList = str(r.text)

        #cleaning up the returned data for output to screen 
        shoppingList = shoppingList.replace('(','')
        shoppingList = shoppingList.replace(')','')
        shoppingList = shoppingList.replace("'", '')
        shoppingList = shoppingList.replace('[','')
        shoppingList = shoppingList.replace(']','')
        shoppingList = shoppingList.replace(',', '')
        shoppingList = shoppingList.split('/')

       #output in vertical list
        for i in shoppingList:
            self.box.add_widget(
                Label(text='{0}'.format(i)))

    #reset the database tables for the current list
    def delete_items(self):
        self.email = {}
        userid = str(email)
        self.email['userid'] = userid
        payload = self.email
        r = requests.post("http://moorej.pythonanywhere.com/clearLists", data=payload)        
        
########################################
class ReportChangeScreen(Screen):
    #connected to above drop downs
    def item_change(self, value):
        value = str(value)
        value = value.lower()
        report['itemChanged'] = value
        
    def from_location(self, value):
        value = int(value)
        report['locationFrom'] = value
        
    def to_location(self, value):
        value = int(value)
        report['locationTo'] = value

    #sending the change to database
    def submit_items(self):
        userid = str(email)
        report['userid'] = userid
        payload = report
        r = requests.post("http://moorej.pythonanywhere.com/reportChange", data=payload)
       

class CompleteScreen(Screen):
    pass
##########################################################################################

#main widget        
screen_manager = ScreenManager()

#children widgets of screen_manager
screen_manager.add_widget(MenuScreen(name="main_menu"))
screen_manager.add_widget(CreateNewScreen(name="create_new"))
screen_manager.add_widget(ViewCurrentScreen(name="check_current"))
screen_manager.add_widget(FinishScreen(name="finish"))
screen_manager.add_widget(SelectStoreScreen(name="select_store"))
screen_manager.add_widget(ViewFinishScreen(name="view_finish"))
screen_manager.add_widget(ReportChangeScreen(name="report_change"))
screen_manager.add_widget(CompleteScreen(name="complete"))

class ScreenApp(App):
    def build(self):
        return screen_manager

sample_app = ScreenApp()
sample_app.run()
