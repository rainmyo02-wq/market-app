from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import AsyncImage
from kivy.core.window import Window

class ShopZoneApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1) 
        self.cart_count = 0
        
        self.all_products = [
            {"name": "Wireless Mouse", "price": "$25.00", "image": "https://cdn-icons-png.flaticon.com/512/2685/2685810.png"},
            {"name": "Mechanical Keyboard", "price": "$65.00", "image": "https://cdn-icons-png.flaticon.com/512/10002/10002366.png"},
            {"name": "Gaming Headset", "price": "$45.00", "image": "https://cdn-icons-png.flaticon.com/512/3043/3043888.png"},
            {"name": "Smart Watch", "price": "$120.00", "image": "https://cdn-icons-png.flaticon.com/512/3233/3233515.png"},
            {"name": "Running Shoes", "price": "$55.00", "image": "https://cdn-icons-png.flaticon.com/512/2553/2553742.png"}
        ]

        root_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        header_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), spacing=5)
        self.search_input = TextInput(hint_text='Search items...', multiline=False, size_hint=(0.5, 1))
        search_btn = Button(text='Search', size_hint=(0.25, 1), background_color=(1, 0.6, 0, 1))
        search_btn.bind(on_press=self.on_search)
        
        self.cart_btn = Button(text='Cart (0)', size_hint=(0.25, 1), background_color=(0.2, 0.8, 0.2, 1))
        
        header_layout.add_widget(self.search_input)
        header_layout.add_widget(search_btn)
        header_layout.add_widget(self.cart_btn)
        root_layout.add_widget(header_layout)

        scroll = ScrollView(size_hint=(1, 0.9))
        self.products_layout = GridLayout(cols=1, spacing=15, size_hint_y=None)
        self.products_layout.bind(minimum_height=self.products_layout.setter('height'))
        
        self.load_products(self.all_products)
        
        scroll.add_widget(self.products_layout)
        root_layout.add_widget(scroll)

        return root_layout

    def load_products(self, products):
        self.products_layout.clear_widgets() 
        
        for p in products:
            item_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=100, spacing=10)
            
            img = AsyncImage(source=p['image'], size_hint=(0.3, 1))
            
            info_box = BoxLayout(orientation='vertical', size_hint=(0.4, 1))
            name_lbl = Label(text=f"[b]{p['name']}[/b]", markup=True, halign='left', valign='bottom')
            name_lbl.bind(size=name_lbl.setter('text_size'))
            price_lbl = Label(text=f"[color=ff9900]{p['price']}[/color]", markup=True, halign='left', valign='top')
            price_lbl.bind(size=price_lbl.setter('text_size'))
            
            info_box.add_widget(name_lbl)
            info_box.add_widget(price_lbl)
            
            buy_btn = Button(text='Add to Cart', size_hint=(0.3, 0.6), pos_hint={'center_y': 0.5}, background_color=(0.2, 0.6, 1, 1))
            buy_btn.bind(on_press=lambda inst, n=p['name']: self.add_to_cart(n))
            
            item_box.add_widget(img)
            item_box.add_widget(info_box)
            item_box.add_widget(buy_btn)
            
            self.products_layout.add_widget(item_box)

    def on_search(self, instance):
        query = self.search_input.text.lower()
        filtered_products = [p for p in self.all_products if query in p['name'].lower()]
        self.load_products(filtered_products)

    def add_to_cart(self, item_name):
        self.cart_count += 1
        self.cart_btn.text = f'Cart ({self.cart_count})'

if __name__ == '__main__':
    ShopZoneApp().run()
