import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition


class MenuScreen(Screen):
    print("Hi")
    pass

class ArticlesScreen(Screen):
    pass 

class AnalyticsScreen(Screen):
    pass 

class RewardsScreen(Screen):
    pass 

class SlotmachineScreen(Screen):
    pass 

class TestApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(ArticlesScreen(name='articles'))   
        sm.add_widget(AnalyticsScreen(name='analytics')) 
        sm.add_widget(RewardsScreen(name='rewards')) 
        sm.add_widget(SlotmachineScreen(name='slotmachine'))  
        return sm

if __name__ == '__main__':
    TestApp().run()
    