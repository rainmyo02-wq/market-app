from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, RoundedRectangle, Ellipse
from kivy.core.window import Window
from kivy.metrics import dp

# Shop Zone Dark Theme Colors
Window.clearcolor = (0.07, 0.09, 0.15, 1)

class CustomCard(BoxLayout):
    """ Custom Card Component """
    def __init__(self, bg_color=(0.12, 0.16, 0.23, 1), radius=[8], **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*bg_color)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=radius)
        self.bind(pos=self._update_rect, size=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class ProductImageGraphic(BoxLayout):
    """ Offline Reliable Image Holder Graphics """
    def __init__(self, color=(0.23, 0.51, 0.96, 1), **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*color)
            self.circle = Ellipse(pos=self.pos, size=self.size)
        self.bind(pos=self._update, size=self._update)

    def _update(self, instance, value):
        self.circle.pos = (instance.pos[0] + instance.size[0]*0.25, instance.pos[1] + instance.size[1]*0.1)
        self.circle.size = (instance.size[0]*0.5, instance.size[1]*0.8)

# ================= 1. LOGIN SCREEN =================
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main_box = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        
        form_box = BoxLayout(orientation='vertical', size_hint_y=None, spacing=dp(10))
        form_box.bind(minimum_height=form_box.setter('height'))

        # Header
        logo = Label(
            text="[b][color=3b82f6]SHOP[/color] [color=ffffff]ZONE[/color][/b]",
            markup=True,
            font_size='32sp',
            size_hint_y=None,
            height=dp(50)
        )
        
        welcome_label = Label(
            text="Sign in to your Shop Zone Account",
            font_size='14sp',
            size_hint_y=None,
            height=dp(20),
            color=(0.8, 0.8, 0.8, 1)
        )

        self.error_label = Label(
            text="",
            font_size='12sp',
            color=(1, 0.3, 0.3, 1),
            size_hint_y=None,
            height=dp(20)
        )

        # Input Box
        input_card = CustomCard(
            orientation='vertical', 
            size_hint_y=None,
            height=dp(100),
            padding=dp(8), 
            spacing=dp(6),
            bg_color=(0.12, 0.16, 0.23, 1)
        )
        
        self.email_input = TextInput(
            hint_text="Email or Phone Number",
            multiline=False,
            size_hint_y=None,
            height=dp(40),
            padding=[dp(10), dp(8)],
            background_color=(0.07, 0.09, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            hint_text_color=(0.5, 0.5, 0.5, 1)
        )
        
        self.pass_input = TextInput(
            hint_text="Password (min 6 characters)",
            password=True,
            multiline=False,
            size_hint_y=None,
            height=dp(40),
            padding=[dp(10), dp(8)],
            background_color=(0.07, 0.09, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            hint_text_color=(0.5, 0.5, 0.5, 1)
        )
        
        input_card.add_widget(self.email_input)
        input_card.add_widget(self.pass_input)

        # Remember Me Option
        remember_box = BoxLayout(size_hint_y=None, height=dp(30), spacing=dp(5))
        self.remember_cb = CheckBox(size_hint_x=None, width=dp(30), active=True)
        rem_label = Label(text="Remember Password", font_size='12sp', color=(0.8,0.8,0.8,1), halign='left')
        rem_label.bind(size=rem_label.setter('text_size'))
        remember_box.add_widget(self.remember_cb)
        remember_box.add_widget(rem_label)

        # Buttons
        login_btn = Button(
            text="Sign In",
            size_hint_y=None,
            height=dp(42),
            background_color=(0.23, 0.51, 0.96, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        login_btn.bind(on_release=self.validate_login)

        guest_btn = Button(
            text="Skip & Continue as Guest >",
            size_hint_y=None,
            height=dp(35),
            background_color=(0, 0, 0, 0),
            color=(0.6, 0.8, 1, 1)
        )
        guest_btn.bind(on_release=self.go_to_home)

        form_box.add_widget(logo)
        form_box.add_widget(welcome_label)
        form_box.add_widget(self.error_label)
        form_box.add_widget(input_card)
        form_box.add_widget(remember_box)
        form_box.add_widget(login_btn)
        form_box.add_widget(guest_btn)

        main_box.add_widget(Label(size_hint_y=0.1))
        main_box.add_widget(form_box)
        main_box.add_widget(Label(size_hint_y=0.1))

        self.add_widget(main_box)

    def validate_login(self, instance):
        email = self.email_input.text.strip()
        pwd = self.pass_input.text.strip()

        if not email or "@" not in email:
            self.error_label.text = "Please enter a valid Gmail / Email!"
        elif len(pwd) < 6:
            self.error_label.text = "Password must be at least 6 characters!"
        else:
            self.error_label.text = ""
            self.go_to_home(instance)

    def go_to_home(self, instance):
        self.manager.current = 'home'


# ================= 2. HOME SCREEN =================
class HomeScreen(Screen):
    cart_count = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main_layout = BoxLayout(orientation='vertical')

        # ---------------- TOP BAR ----------------
        top_bar = BoxLayout(size_hint_y=None, height=dp(55), padding=[dp(8), dp(5)], spacing=dp(8))
        with top_bar.canvas.before:
            Color(0.12, 0.16, 0.23, 1)
            RoundedRectangle(pos=top_bar.pos, size=top_bar.size)

        logo = Label(
            text="[b][color=3b82f6]SHOP[/color] ZONE[/b]",
            markup=True,
            font_size='18sp',
            size_hint_x=0.35,
            halign='center',
            valign='middle'
        )

        search_input = TextInput(
            hint_text="Search Shop Zone...",
            multiline=False,
            size_hint_x=0.45,
            padding=[dp(8), dp(8)],
            background_color=(0.07, 0.09, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            hint_text_color=(0.5, 0.5, 0.5, 1)
        )

        self.cart_btn = Button(
            text="Cart (0)",
            size_hint_x=0.2,
            background_color=(0.23, 0.51, 0.96, 1),
            color=(1, 1, 1, 1),
            bold=True
        )

        top_bar.add_widget(logo)
        top_bar.add_widget(search_input)
        top_bar.add_widget(self.cart_btn)
        main_layout.add_widget(top_bar)

        # ---------------- MAIN CONTENT ----------------
        scroll = ScrollView()
        content_layout = BoxLayout(orientation='vertical', size_hint_y=None, padding=dp(10), spacing=dp(12))
        content_layout.bind(minimum_height=content_layout.setter('height'))

        # BANNER
        banner = CustomCard(
            bg_color=(0.23, 0.51, 0.96, 1),
            size_hint_y=None,
            height=dp(70),
            padding=dp(8),
            orientation='vertical'
        )
        banner.add_widget(Label(text="[b]SHOP ZONE SPECIAL DEALS[/b]", markup=True, font_size='16sp', color=(1,1,1,1)))
        banner.add_widget(Label(text="Up to 50% OFF on Electronics", font_size='12sp', color=(0.9,0.9,0.9,1)))
        content_layout.add_widget(banner)

        # PRODUCTS GRID
        grid = GridLayout(cols=2, spacing=dp(10), size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        products = [
            {"name": "Echo Dot Smart", "price": "$39.99", "orig": "$49.99", "color": (0.9, 0.3, 0.3, 1)},
            {"name": "Kindle Paperwhite", "price": "$129.99", "orig": "$149.99", "color": (0.3, 0.7, 0.4, 1)},
            {"name": "Headphones", "price": "$89.00", "orig": "$119.00", "color": (0.2, 0.6, 0.9, 1)},
            {"name": "Fitness Watch", "price": "$55.50", "orig": "$70.00", "color": (0.9, 0.6, 0.2, 1)},
        ]

        for p in products:
            card = CustomCard(
                orientation='vertical',
                size_hint_y=None,
                height=dp(210),
                padding=dp(8),
                spacing=dp(4)
            )
            
            p_img = ProductImageGraphic(color=p["color"], size_hint_y=None, height=dp(70))

            rating = Label(
                text="Rating: 4.8 ⭐", 
                font_size='10sp', 
                size_hint_y=None, 
                height=dp(18),
                color=(0.95, 0.77, 0.05, 1), 
                halign='left', 
                valign='middle'
            )
            rating.bind(size=rating.setter('text_size'))
            
            title = Label(
                text=f"[b]{p['name']}[/b]", 
                markup=True, 
                font_size='12sp', 
                size_hint_y=None, 
                height=dp(30),
                halign='left', 
                valign='top'
            )
            title.bind(size=title.setter('text_size'))

            price = Label(
                text=f"[color=3b82f6][b]{p['price']}[/b][/color]  [color=888888][s]{p['orig']}[/s][/color]", 
                markup=True, 
                font_size='12sp', 
                size_hint_y=None, 
                height=dp(20),
                halign='left',
                valign='middle'
            )
            price.bind(size=price.setter('text_size'))

            add_btn = Button(
                text="Add to Cart",
                size_hint_y=None,
                height=dp(32),
                background_color=(0.23, 0.51, 0.96, 1),
                color=(1, 1, 1, 1),
                bold=True
            )
            add_btn.bind(on_release=self.add_to_cart_action)

            card.add_widget(p_img)
            card.add_widget(rating)
            card.add_widget(title)
            card.add_widget(price)
            card.add_widget(add_btn)

            grid.add_widget(card)

        content_layout.add_widget(grid)
        scroll.add_widget(content_layout)
        main_layout.add_widget(scroll)

        # ---------------- BOTTOM NAVIGATION BAR ----------------
        bottom_nav = BoxLayout(size_hint_y=None, height=dp(45), spacing=dp(2))
        nav_items = ["Home", "Categories", "Alerts", "Profile"]
        
        for nav in nav_items:
            btn = Button(
                text=nav,
                background_color=(0.12, 0.16, 0.23, 1),
                color=(1, 1, 1, 1),
                font_size='11sp'
            )
            bottom_nav.add_widget(btn)

        main_layout.add_widget(bottom_nav)

        self.add_widget(main_layout)

    def add_to_cart_action(self, instance):
        self.cart_count += 1
        self.cart_btn.text = f"Cart ({self.cart_count})"


# ================= 3. MAIN APP MANAGER =================
class ShopZoneApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        return sm

if __name__ == '__main__':
    ShopZoneApp().run()
