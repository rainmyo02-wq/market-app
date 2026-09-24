from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window

# Set background color to dark slate
Window.clearcolor = (0.07, 0.09, 0.15, 1)

class CardContainer(BoxLayout):
    """ Rounded Card Effect for Products """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0.12, 0.16, 0.23, 1) # Dark card background
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[12])
        self.bind(pos=self._update_rect, size=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class ShopZoneApp(App):
    def build(self):
        self.title = "Shop Zone"
        
        # Main Container
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=15)

        # ---------------- 1. TOP HEADER ----------------
        header = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        logo_label = Label(
            text="[b][color=3b82f6]SHOP[/color] ZONE[/b]", 
            markup=True, 
            font_size='24sp',
            size_hint_x=0.7,
            halign='left',
            valign='middle'
        )
        logo_label.bind(size=logo_label.setter('text_size'))
        
        cart_btn = Button(
            text="🛒 Cart (0)", 
            size_hint_x=0.3, 
            background_color=(0.23, 0.51, 0.96, 1),
            bold=True
        )
        
        header.add_widget(logo_label)
        header.add_widget(cart_btn)
        main_layout.add_widget(header)

        # ---------------- 2. SEARCH BAR ----------------
        search_box = TextInput(
            hint_text="🔍 Search products...",
            size_hint_y=None,
            height=45,
            multiline=False,
            padding=[15, 12, 15, 12],
            background_color=(0.12, 0.16, 0.23, 1),
            foreground_color=(1, 1, 1, 1),
            hint_text_color=(0.6, 0.6, 0.6, 1)
        )
        main_layout.add_widget(search_box)

        # ---------------- 3. CATEGORY BUTTONS ----------------
        categories = ["All", "Electronics", "Fashion", "Gadgets"]
        cat_layout = BoxLayout(size_hint_y=None, height=40, spacing=8)
        
        for cat in categories:
            btn = Button(
                text=cat,
                size_hint_x=1/len(categories),
                background_color=(0.23, 0.51, 0.96, 1) if cat == "All" else (0.12, 0.16, 0.23, 1),
                color=(1, 1, 1, 1)
            )
            cat_layout.add_widget(btn)
            
        main_layout.add_widget(cat_layout)

        # ---------------- 4. PRODUCT LIST (GRID VIEW) ----------------
        scroll = ScrollView()
        grid = GridLayout(cols=2, spacing=15, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        # Products List
        products = [
            {"name": "Wireless Headphones", "price": "$49.99", "rating": "⭐ 4.8"},
            {"name": "Smart Watch V2", "price": "$89.99", "rating": "⭐ 4.9"},
            {"name": "Leather Backpack", "price": "$35.00", "rating": "⭐ 4.6"},
            {"name": "Running Shoes", "price": "$65.00", "rating": "⭐ 4.7"},
            {"name": "Bluetooth Speaker", "price": "$29.99", "rating": "⭐ 4.5"},
            {"name": "Classic Sunglasses", "price": "$15.50", "rating": "⭐ 4.4"},
        ]

        for item in products:
            card = CardContainer(
                orientation='vertical',
                size_hint_y=None,
                height=180,
                padding=12,
                spacing=6
            )

            # Rating
            rating_label = Label(
                text=item["rating"], 
                font_size='12sp', 
                color=(0.95, 0.77, 0.05, 1),
                size_hint_y=0.2,
                halign='left'
            )
            rating_label.bind(size=rating_label.setter('text_size'))

            # Product Name
            name_label = Label(
                text=f"[b]{item['name']}[/b]", 
                markup=True, 
                font_size='15sp',
                size_hint_y=0.3,
                halign='left',
                valign='top'
            )
            name_label.bind(size=name_label.setter('text_size'))

            # Price
            price_label = Label(
                text=f"[color=10b981]{item['price']}[/color]", 
                markup=True, 
                font_size='16sp',
                size_hint_y=0.2,
                halign='left'
            )
            price_label.bind(size=price_label.setter('text_size'))

            # Add to Cart Button
            add_btn = Button(
                text="Add to Cart",
                size_hint_y=0.3,
                background_color=(0.23, 0.51, 0.96, 1),
                bold=True
            )

            card.add_widget(rating_label)
            card.add_widget(name_label)
            card.add_widget(price_label)
            card.add_widget(add_btn)

            grid.add_widget(card)

        scroll.add_widget(grid)
        main_layout.add_widget(scroll)

        return main_layout

if __name__ == '__main__':
    ShopZoneApp().run()
