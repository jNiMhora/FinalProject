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
        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .25
            size_hint_y: .1
	    Spinner:
	        size_hint_x: 1
	        size_hint_y: None
	        text: "apple"
	        values: ["apple", "banana", "grape", "lemon", "melon"]
	        id: spinner_id
	        on_text: root.spinner_clicked(spinner_id.text)
        BoxLayout:
            orientation: "horizontal"
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
        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .25
            size_hint_y: .1
	    Spinner:
	        size_hint_x: 1
	        size_hint_y: None
	        text: "county"
	        values: ["Carlow", "Wicklow", "Wexford"]
	        id: spinner_id
	        on_text: root.county_clicked(spinner_id.text)
""")

class MenuScreen(Screen):
    pass

class CreateNewScreen(Screen):
    
    def spinner_clicked(self, value):
        print("Spinner value " + value)
        item = value
        amount = 1
        with DBcm.UseDatabase(config) as cursor:
            _SQL = """INSERT INTO selecteditems (itemName, quantity) values (%s, %s) """
            cursor.execute(_SQL, (item, amount))

class ViewCurrentScreen(Screen):
    def get_items(self):
        with DBcm.UseDatabase(config) as cursor:
            result = cursor.execute("""SELECT itemName FROM selecteditems""")
            response = [row[0] for row in result.fetchall()
            print(result)
            #response = [row[0] for row in result.fetchall()]
        

class FinishScreen(Screen):
    pass

class SelectStoreScreen(Screen):
      def county_clicked(self, value):
        print("Spinner value " + value)
        
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
