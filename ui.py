from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import AsyncImage
from kivy.metrics import dp

class ProductCard(MDCard):
    def __init__(self, product_name, price, image_url, add_to_cart_callback, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.padding = dp(10)
        self.spacing = dp(15)
        self.size_hint_y = None
        self.height = dp(140)
        self.elevation = 2 
        self.radius = [dp(15)]
        self.md_bg_color = (1, 1, 1, 1) 

        img = AsyncImage(source=image_url, size_hint_x=0.35)
        self.add_widget(img)

        info_box = MDBoxLayout(orientation="vertical", size_hint_x=0.4, padding=(dp(5), dp(15), dp(5), dp(15)))
        name_lbl = MDLabel(text=f"[b]{product_name}[/b]", markup=True, font_style="Subtitle1", theme_text_color="Primary")
        price_lbl = MDLabel(text=price, font_style="H6", theme_text_color="Custom", text_color=(0.8, 0.2, 0.1, 1))
        info_box.add_widget(name_lbl)
        info_box.add_widget(price_lbl)
        self.add_widget(info_box)

        btn_box = MDBoxLayout(orientation="vertical", size_hint_x=0.25, padding=dp(10))
        buy_btn = MDRaisedButton(text="Add to Cart", md_bg_color=(0.1, 0.6, 0.8, 1), pos_hint={"center_y": 0.5})
        buy_btn.bind(on_press=lambda x: add_to_cart_callback(product_name))
        btn_box.add_widget(buy_btn)
        self.add_widget(btn_box)

def create_main_ui(app_instance):
    main_layout = MDBoxLayout(orientation='vertical')

    app_instance.toolbar = MDTopAppBar(
        title="Shop Zone",
        elevation=4
    )
    main_layout.add_widget(app_instance.toolbar)

    search_box = MDBoxLayout(orientation='horizontal', size_hint_y=None, height=dp(70), padding=dp(10), spacing=dp(10))
    search_input = MDTextField(
        hint_text="Search Products...", 
        mode="round", 
        size_hint_x=0.7,
        fill_color_normal=(1, 1, 1, 1)
    )
    search_btn = MDRaisedButton(
        text="Search", 
        md_bg_color=app_instance.theme_cls.accent_color, 
        text_color=(0, 0, 0, 1), 
        size_hint_x=0.3, 
        pos_hint={"center_y": 0.5}
    )
    search_box.add_widget(search_input)
    search_box.add_widget(search_btn)
    main_layout.add_widget(search_box)

    scroll = ScrollView()
    products_layout = MDGridLayout(cols=1, adaptive_height=True, padding=dp(15), spacing=dp(15))
    
    all_products = [
        {"name": "Wireless Mouse", "price": "$25.00", "image": "https://img.icons8.com/color/150/000000/mouse.png"},
        {"name": "Mechanical Keyboard", "price": "$65.00", "image": "https://img.icons8.com/color/150/000000/keyboard.png"},
        {"name": "Gaming Headset", "price": "$45.00", "image": "https://img.icons8.com/color/150/000000/headphones.png"}
    ]

    for p in all_products:
        card = ProductCard(p['name'], p['price'], p['image'], app_instance.add_to_cart)
        products_layout.add_widget(card)
    
    scroll.add_widget(products_layout)
    main_layout.add_widget(scroll)

    return main_layout
