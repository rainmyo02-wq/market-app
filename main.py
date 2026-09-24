import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class ShopZoneApp(App):
    def build(self):
        self.title = "Shop Zone"
        
        # Main Layout
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header Label
        header = Label(
            text="Welcome to Shop Zone",
            font_size='24sp',
            bold=True,
            size_hint=(1, 0.1)
        )
        main_layout.add_widget(header)
        
        # Product List Area (ScrollView)
        scroll = ScrollView(size_hint=(1, 0.9))
        grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        # Example Products
        products = [
            {"name": "Product 1", "price": "$10"},
            {"name": "Product 2", "price": "$20"},
            {"name": "Product 3", "price": "$30"},
        ]
        
        for item in products:
            btn = Button(
                text=f"{item['name']} - {item['price']}",
                size_hint_y=None,
                height=60,
                font_size='18sp'
            )
            grid.add_widget(btn)
            
        scroll.add_widget(grid)
        main_layout.add_widget(scroll)
        
        return main_layout

if __name__ == '__main__':
    ShopZoneApp().run()
