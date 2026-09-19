from kivymd.app import MDApp
from kivymd.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy import platform
from kivy.core.window import Window


class MainScreen(MDScreen):
    ...

class GameScreen(MDScreen):
    ...

class ShooterApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Pink"

        self.sm = MDScreenManager()

        self.sm.add_widget(MainScreen(name="main"))
        self.sm.add_widget(MainScreen(name="game"))

        return self.sm


if platform != "android":
    Window.size = (450,900)
    Window.top = 100
    Window.left = 600

app = ShooterApp()
app.run()