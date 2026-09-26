from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window

Window.size = (360, 640)

class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.label = MDLabel(
            text="Welcome to Shop Zone",
            halign="center",
            font_style="H5"
        )
        
        btn = MDRaisedButton(
            text="Click Me",
            pos_hint={"center_x": .5},
            on_release=self.on_click
        )
        
        layout.add_widget(self.label)
        layout.add_widget(btn)
        self.add_widget(layout)

    def on_click(self, instance):
        self.label.text = "Button Clicked Successfully!"

class ShopApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return MainScreen()

if __name__ == "__main__":
    ShopApp().run()
