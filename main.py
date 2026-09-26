from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (360, 640)

class ShopApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.label = Label(
            text="Welcome to Shop Zone",
            font_size='22sp',
            halign='center'
        )
        
        btn = Button(
            text="Click Me",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.6, 1, 1)
        )
        btn.bind(on_press=self.on_button_click)
        
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def on_button_click(self, instance):
        self.label.text = "App is working successfully!"

if __name__ == '__main__':
    ShopApp().run()
