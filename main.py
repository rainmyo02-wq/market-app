from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
from kivy.metrics import dp

class ProductCard(MDCard):
    def __init__(self, product_name, price, image_url, add_to_cart_callback, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.padding = dp(10)
        self.spacing = dp(15)
        self.size_hint_y = None
        self.height = dp(140)
        self.elevation = 2  # Shadow effect for the card
        self.radius = [dp(15)]
        self.md_bg_color = (1, 1, 1, 1) # White card background

        # Product Image
        img = AsyncImage(source=image_url, size_hint_x=0.35)
        self.add_widget(img)

        # Product Name and Price
        info_box = MDBoxLayout(orientation="vertical", size_hint_x=0.4, padding=(dp(5), dp(15), dp(5), dp(15)))
        name_lbl = MDLabel(text=f"[b]{product_name}[/b]", markup=True, font_style="Subtitle1", theme_text_color="Primary")
        price_lbl = MDLabel(text=price, font_style="H6", theme_text_color="Custom", text_color=(0.8, 0.2, 0.1, 1))
        info_box.add_widget(name_lbl)
        info_box.add_widget(price_lbl)
        self.add_widget(info_box)

        # Add to Cart Button
        btn_box = MDBoxLayout(orientation="vertical", size_hint_x=0.25, padding=dp(10))
        buy_btn = MDRaisedButton(text="Add to Cart", md_bg_color=(0.1, 0.6, 0.8, 1), pos_hint={"center_y": 0.5})
        buy_btn.bind(on_press=lambda x: add_to_cart_callback(product_name))
        btn_box.add_widget(buy_btn)
        self.add_widget(btn_box)

class ShopZoneApp(MDApp):
    def build(self):
        # UI Colors and Theme
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"
        Window.clearcolor = (0.95, 0.95, 0.95, 1) # Light gray app background

        self.cart_count = 0
        
        self.all_products = [
            {"name": "Wireless Mouse", "price": "$25.00", "image": "https://img.icons8.com/color/150/000000/mouse.png"},
            {"name": "Mechanical Keyboard", "price": "$65.00", "image": "https://img.icons8.com/color/150/000000/keyboard.png"},
            {"name": "Gaming Headset", "price": "$45.00", "image": "https://img.icons8.com/color/150/000000/headphones.png"},
            {"name": "Smart Watch", "price": "$120.00", "image": "https://img.icons8.com/color/150/000000/smart-watch.png"},
            {"name": "Running Shoes", "price": "$55.00", "image": "https://img.icons8.com/color/150/000000/trainers.png"}
        ]

        main_layout = MDBoxLayout(orientation='vertical')

        # 1. Top App Bar
        self.toolbar = MDTopAppBar(
            title="My Own Shop",
            elevation=4,
            right_action_items=[["cart", lambda x: self.on_cart_click()]]
        )
        main_layout.add_widget(self.toolbar)

        # 2. Search Bar Layout
        search_box = MDBoxLayout(orientation='horizontal', size_hint_y=None, height=dp(70), padding=dp(10), spacing=dp(10))
        
        self.search_input = MDTextField(
            hint_text="Search Products...", 
            mode="round", 
            size_hint_x=0.7,
            fill_color_normal=(1, 1, 1, 1)
        )
        
        search_btn = MDRaisedButton(
            text="Search", 
            md_bg_color=self.theme_cls.accent_color, 
            text_color=(0, 0, 0, 1), 
            size_hint_x=0.3, 
            pos_hint={"center_y": 0.5}
        )
        search_btn.bind(on_press=self.on_search)
        
        search_box.add_widget(self.search_input)
        search_box.add_widget(search_btn)
        main_layout.add_widget(search_box)

        # 3. Product List (Scrollable)
        scroll = ScrollView()
        self.products_layout = MDGridLayout(cols=1, adaptive_height=True, padding=dp(15), spacing=dp(15))
        
        self.load_products(self.all_products)
        
        scroll.add_widget(self.products_layout)
        main_layout.add_widget(scroll)

        return main_layout

    def load_products(self, products):
        self.products_layout.clear_widgets()
        for p in products:
            card = ProductCard(p['name'], p['price'], p['image'], self.add_to_cart)
            self.products_layout.add_widget(card)

    def on_search(self, instance):
        query = self.search_input.text.lower()
        filtered = [p for p in self.all_products if query in p['name'].lower()]
        self.load_products(filtered)

    def add_to_cart(self, item_name):
        self.cart_count += 1
        self.toolbar.title = f"My Own Shop ({self.cart_count} in Cart)"

    def on_cart_click(self):
        # You can add cart view logic here later
        pass

if __name__ == '__main__':
    ShopZoneApp().run()
