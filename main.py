from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
#Window.size = (350, 580)

class Twitter(MDApp):
    def build(self):
        global screen_manager
        self.icon = 't-icon.png'
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file('sign_up.kv'))
        screen_manager.add_widget(Builder.load_file('touch_id.kv'))
        return screen_manager

if __name__ == '__main__':
    LabelBase.register(name='BMontserrat', fn_regular='Montserrat-SemiBold.ttf')
    LabelBase.register(name='MMontserrat', fn_regular='Montserrat-Medium.ttf')
    Twitter().run()
