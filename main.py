from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

class ShopZoneApp(App):
    def build(self):
        root_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 1. Top Header (Search Bar)
        header_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), spacing=5)
        self.search_input = TextInput(hint_text='Search Amazon / Shop Zone...', multiline=False)
        search_btn = Button(text='Search', size_hint=(0.3, 1), background_color=(1, 0.6, 0, 1))
        search_btn.bind(on_press=self.on_search)
        
        header_layout.add_widget(self.search_input)
        header_layout.add_widget(search_btn)
        root_layout.add_widget(header_layout)

        # 2. Body / Products List
        scroll = ScrollView(size_hint=(1, 0.75))
        products_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        products_layout.bind(minimum_height=products_layout.setter('height'))

        self.items = [
            ("Wireless Mouse", "$25.00"),
            ("Mechanical Keyboard", "$65.00"),
            ("Gaming Headset", "$45.00"),
            ("Smart Watch", "$120.00"),
            ("Running Shoes", "$55.00")
        ]

        for name, price in self.items:
            item_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=60, padding=5, spacing=10)
            lbl = Label(text=f"{name}\n[color=ff9900]{price}[/color]", markup=True, halign='left', valign='middle')
            lbl.bind(size=lbl.setter('text_size'))
            
            buy_btn = Button(text='Add to Cart', size_hint=(0.4, 1), background_color=(0.2, 0.6, 1, 1))
            buy_btn.bind(on_press=lambda inst, n=name: self.add_to_cart(n))
            
            item_box.add_widget(lbl)
            item_box.add_widget(buy_btn)
            products_layout.add_widget(item_box)

        scroll.add_widget(products_layout)
        root_layout.add_widget(scroll)

        # 3. Bottom Status / Cart Bar
        self.status_label = Label(text='Cart: 0 items', size_hint=(1, 0.1), font_size='16sp')
        root_layout.add_widget(self.status_label)

        return root_layout

    def on_search(self, instance):
        query = self.search_input.text
        self.status_label.text = f"Searching for: '{query}'"

    def add_to_cart(self, item_name):
        self.status_label.text = f"Added to Cart: {item_name}"

if __name__ == '__main__':
    ShopZoneApp().run()
