import kivy
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from view.mainmenu import MainMenu
from view.rig import Rig
from view.polarview import PolarView
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.core.window import Window

from kivy.utils import platform


kivy.require('2.1.0') 
KV = '''
MDScreen:

    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "orange"
        text_color_active: "lightgrey"

        MDBottomNavigationItem:
            id:screen_1
            name: 'Main'
            text: 'Main'
            icon: 'view-list'

        MDBottomNavigationItem:
            id:screen_2
            name: 'Polar'
            text: 'Polar'
            icon: 'crosshairs'
        
        MDBottomNavigationItem:
            id:screen_3
            name: 'Rig'
            text: 'Rig'
            icon: 'radio-handheld'
'''
class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class SatTrekApp(MDApp):
    title = 'SatCTRL-D72'
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.icon='assets/FP_Satellite_icon.png'

        if platform == "android":
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        return Builder.load_string(KV)
    
    def on_start(self):
        Window.size = (450, 800)
        # mainTab = Tab(title='Main', icon='view-list', tab_label_text='Main')
        # mainTab.add_widget(MainMenu())
        self.root.ids.screen_1.add_widget(MainMenu())
        self.root.ids.screen_2.add_widget(MainMenu())
        self.root.ids.screen_3.add_widget(MainMenu())

        # self.root.ids.screen_1.add_widget(MainMenu())
        # self.root.ids.screen_2.add_widget(PolarView())
        # self.root.ids.screen_3.add_widget(Rig())
        
        # polarTab = Tab(title='Polar', icon='crosshairs', tab_label_text='Polar')
        # polarTab.add_widget(PolarView())
        # self.root.ids.tabs.add_widget(polarTab)

        # rigTab = Tab(title='Rig',icon='radio-handheld', tab_label_text='Rig')
        # rigTab.add_widget(Rig())
        # self.root.ids.tabs.add_widget(rigTab)
        
    def callback(self, instance_action_top_appbar_button):
        print(instance_action_top_appbar_button)
    
if __name__ == '__main__':
    app = SatTrekApp()
    app.run()
    