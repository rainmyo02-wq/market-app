from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage
from kivy.uix.checkbox import CheckBox
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
from kivy.metrics import dp

# Shop Zone Dark Theme Colors
Window.clearcolor = (0.07, 0.09, 0.15, 1)

class CustomCard(BoxLayout):
    def __init__(self, bg_color=(0.12, 0.16, 0.23, 1), radius=[8], **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*bg_color)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=radius)
        self.bind(pos=self._update_rect, size=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

# ALL PRODUCTS DATA
ALL_PRODUCTS = [
    {"name": "Echo Dot Smart", "price": "$39.99", "orig": "$49.99", "cat": "Electronics", "img": "https://picsum.photos/id/100/200/200"},
    {"name": "Kindle Paperwhite", "price": "$129.99", "orig": "$149.99", "cat": "Electronics", "img": "https://picsum.photos/id/101/200/200"},
    {"name": "Headphones Wireless", "price": "$89.00", "orig": "$119.00", "cat": "Electronics", "img": "https://picsum.photos/id/102/200/200"},
    {"name": "Fitness Smart Watch", "price": "$55.50", "orig": "$70.00", "cat": "Electronics", "img": "https://picsum.photos/id/103/200/200"},
    {"name": "Leather Jacket", "price": "$120.00", "orig": "$150.00", "cat": "Fashion", "img": "https://picsum.photos/id/104/200/200"},
    {"name": "Running Shoes", "price": "$75.00", "orig": "$95.00", "cat": "Fashion", "img": "https://picsum.photos/id/106/200/200"},
]

# ================= 1. LOGIN SCREEN =================
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_box = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        form_box = BoxLayout(orientation='vertical', size_hint_y=None, spacing=dp(10))
        form_box.bind(minimum_height=form_box.setter('height'))

        logo = Label(
            text="[b][color=3b82f6]SHOP[/color] [color=ffffff]ZONE[/color][/b]",
            markup=True, font_size='32sp', size_hint_y=None, height=dp(50)
        )
        welcome_label = Label(text="Sign in to your Shop Zone Account", font_size='14sp', size_hint_y=None, height=dp(20), color=(0.8, 0.8, 0.8, 1))
        self.error_label = Label(text="", font_size='12sp', color=(1, 0.3, 0.3, 1), size_hint_y=None, height=dp(20))

        input_card = CustomCard(orientation='vertical', size_hint_y=None, height=dp(100), padding=dp(8), spacing=dp(6))
        self.email_input = TextInput(hint_text="Email or Phone Number", multiline=False, size_hint_y=None, height=dp(40), padding=[dp(10), dp(8)], background_color=(0.07, 0.09, 0.15, 1), foreground_color=(1, 1, 1, 1))
        self.pass_input = TextInput(hint_text="Password (min 6 chars)", password=True, multiline=False, size_hint_y=None, height=dp(40), padding=[dp(10), dp(8)], background_color=(0.07, 0.09, 0.15, 1), foreground_color=(1, 1, 1, 1))
        
        input_card.add_widget(self.email_input)
        input_card.add_widget(self.pass_input)

        login_btn = Button(text="Sign In", size_hint_y=None, height=dp(42), background_color=(0.23, 0.51, 0.96, 1), bold=True)
        login_btn.bind(on_release=self.validate_login)

        guest_btn = Button(text="Skip & Continue as Guest >", size_hint_y=None, height=dp(35), background_color=(0,0,0,0), color=(0.6, 0.8, 1, 1))
        guest_btn.bind(on_release=self.go_to_home)

        form_box.add_widget(logo)
        form_box.add_widget(welcome_label)
        form_box.add_widget(self.error_label)
        form_box.add_widget(input_card)
        form_box.add_widget(login_btn)
        form_box.add_widget(guest_btn)

        main_box.add_widget(Label(size_hint_y=0.1))
        main_box.add_widget(form_box)
        main_box.add_widget(Label(size_hint_y=0.1))
        self.add_widget(main_box)

    def validate_login(self, instance):
        if not self.email_input.text.strip() or "@" not in self.email_input.text:
            self.error_label.text = "Please enter a valid Gmail / Email!"
        elif len(self.pass_input.text.strip()) < 6:
            self.error_label.text = "Password must be at least 6 characters!"
        else:
            self.go_to_home(instance)

    def go_to_home(self, instance):
        self.manager.current = 'home'

# ================= 2. HOME SCREEN =================
class HomeScreen(Screen):
    cart_count = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_layout = BoxLayout(orientation='vertical')

        # TOP BAR
        top_bar = BoxLayout(size_hint_y=None, height=dp(55), padding=[dp(8), dp(5)], spacing=dp(8))
        with top_bar.canvas.before:
            Color(0.12, 0.16, 0.23, 1)
            RoundedRectangle(pos=top_bar.pos, size=top_bar.size)

        logo = Label(text="[b][color=3b82f6]SHOP[/color] ZONE[/b]", markup=True, font_size='18sp', size_hint_x=0.35)
        
        # SEARCH BAR (WORKING)
        self.search_input = TextInput(
            hint_text="Search Shop Zone...", multiline=False, size_hint_x=0.45,
            padding=[dp(8), dp(8)], background_color=(0.07, 0.09, 0.15, 1), foreground_color=(1, 1, 1, 1)
        )
        self.search_input.bind(text=self.filter_products)

        self.cart_btn = Button(text="Cart (0)", size_hint_x=0.2, background_color=(0.23, 0.51, 0.96, 1), bold=True)

        top_bar.add_widget(logo)
        top_bar.add_widget(self.search_input)
        top_bar.add_widget(self.cart_btn)
        self.main_layout.add_widget(top_bar)

        # MAIN SCROLL AREA
        scroll = ScrollView()
        content_layout = BoxLayout(orientation='vertical', size_hint_y=None, padding=dp(10), spacing=dp(12))
        content_layout.bind(minimum_height=content_layout.setter('height'))

        # BANNER
        banner = CustomCard(bg_color=(0.23, 0.51, 0.96, 1), size_hint_y=None, height=dp(65), padding=dp(8), orientation='vertical')
        banner.add_widget(Label(text="[b]SHOP ZONE SPECIAL DEALS[/b]", markup=True, font_size='15sp'))
        banner.add_widget(Label(text="Up to 50% OFF on Selected Items", font_size='11sp'))
        content_layout.add_widget(banner)

        # PRODUCT GRID
        self.grid = GridLayout(cols=2, spacing=dp(10), size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        
        self.display_products(ALL_PRODUCTS)

        content_layout.add_widget(self.grid)
        scroll.add_widget(content_layout)
        self.main_layout.add_widget(scroll)

        # BOTTOM NAVIGATION (WORKING)
        self.main_layout.add_widget(self.build_bottom_nav())
        self.add_widget(self.main_layout)

    def display_products(self, product_list):
        self.grid.clear_widgets()
        for p in product_list:
            card = CustomCard(orientation='vertical', size_hint_y=None, height=dp(210), padding=dp(8), spacing=dp(4))
            
            p_img = AsyncImage(source=p["img"], size_hint_y=None, height=dp(80), allow_stretch=True, keep_ratio=True)
            rating = Label(text="Rating: 4.8 ⭐", font_size='10sp', size_hint_y=None, height=dp(18), color=(0.95, 0.77, 0.05, 1), halign='left')
            rating.bind(size=rating.setter('text_size'))
            
            title = Label(text=f"[b]{p['name']}[/b]", markup=True, font_size='12sp', size_hint_y=None, height=dp(28), halign='left', valign='top')
            title.bind(size=title.setter('text_size'))

            price = Label(text=f"[color=3b82f6][b]{p['price']}[/b][/color]  [color=888888][s]{p['orig']}[/s][/color]", markup=True, font_size='12sp', size_hint_y=None, height=dp(20), halign='left')
            price.bind(size=price.setter('text_size'))

            add_btn = Button(text="Add to Cart", size_hint_y=None, height=dp(30), background_color=(0.23, 0.51, 0.96, 1), bold=True)
            add_btn.bind(on_release=self.add_to_cart_action)

            card.add_widget(p_img)
            card.add_widget(rating)
            card.add_widget(title)
            card.add_widget(price)
            card.add_widget(add_btn)
            self.grid.add_widget(card)

    def filter_products(self, instance, text):
        query = text.lower().strip()
        filtered = [p for p in ALL_PRODUCTS if query in p["name"].lower() or query in p["cat"].lower()]
        self.display_products(filtered)

    def add_to_cart_action(self, instance):
        self.cart_count += 1
        self.cart_btn.text = f"Cart ({self.cart_count})"

    def build_bottom_nav(self):
        bottom_nav = BoxLayout(size_hint_y=None, height=dp(45), spacing=dp(2))
        nav_items = [("Home", 'home'), ("Categories", 'categories'), ("Alerts", 'alerts'), ("Profile", 'profile')]
        
        for name, screen_name in nav_items:
            btn = Button(text=name, background_color=(0.12, 0.16, 0.23, 1), color=(1, 1, 1, 1), font_size='11sp')
            btn.bind(on_release=lambda x, s=screen_name: self.switch_screen(s))
            bottom_nav.add_widget(btn)
        return bottom_nav

    def switch_screen(self, screen_name):
        self.manager.current = screen_name

# ================= OTHER NAV SCREENS =================
class SimpleScreen(Screen):
    def __init__(self, title_text, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        
        # Header
        top_bar = BoxLayout(size_hint_y=None, height=dp(50), padding=dp(10))
        top_bar.add_widget(Label(text=f"[b]{title_text}[/b]", markup=True, font_size='20sp'))
        layout.add_widget(top_bar)
        
        # Body
        layout.add_widget(Label(text=f"Welcome to {title_text} Page", font_size='16sp', color=(0.7,0.7,0.7,1)))

        # Bottom Nav
        bottom_nav = BoxLayout(size_hint_y=None, height=dp(45), spacing=dp(2))
        nav_items = [("Home", 'home'), ("Categories", 'categories'), ("Alerts", 'alerts'), ("Profile", 'profile')]
        for name, screen_name in nav_items:
            btn = Button(text=name, background_color=(0.12, 0.16, 0.23, 1), color=(1, 1, 1, 1), font_size='11sp')
            btn.bind(on_release=lambda x, s=screen_name: self.switch_screen(s))
            bottom_nav.add_widget(btn)
        
        layout.add_widget(bottom_nav)
        self.add_widget(layout)

    def switch_screen(self, screen_name):
        self.manager.current = screen_name

# ================= 3. MAIN APP MANAGER =================
class ShopZoneApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(SimpleScreen(title_text="Categories", name='categories'))
        sm.add_widget(SimpleScreen(title_text="Notifications & Alerts", name='alerts'))
        sm.add_widget(SimpleScreen(title_text="User Profile", name='profile'))
        return sm

if __name__ == '__main__':
    ShopZoneApp().run()
