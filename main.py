from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window

# Amazon Dark Mode Theme Colors
Window.clearcolor = (0.09, 0.11, 0.15, 1)

class CustomCard(BoxLayout):
    """ Rounded Card with Custom Background """
    def __init__(self, bg_color=(0.14, 0.18, 0.24, 1), radius=[10], **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*bg_color)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=radius)
        self.bind(pos=self._update_rect, size=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

# ================= 1. LOGIN SCREEN =================
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=25, spacing=15)

        # Amazon Logo Header
        logo = Label(
            text="[b][color=ff9900]amazon[/color][color=ffffff] zone[/color][/b]",
            markup=True,
            font_size='32sp',
            size_hint_y=0.2
        )
        
        welcome_label = Label(
            text="[b]Sign in to your account[/b]",
            markup=True,
            font_size='18sp',
            size_hint_y=0.1,
            color=(0.9, 0.9, 0.9, 1)
        )

        # Input Box Layout
        input_box = CustomCard(
            orientation='vertical', 
            size_hint_y=0.35, 
            padding=15, 
            spacing=10,
            bg_color=(0.14, 0.18, 0.24, 1)
        )
        
        self.email_input = TextInput(
            hint_text="Email or Phone Number",
            multiline=False,
            size_hint_y=0.45,
            padding=[10, 10],
            background_color=(0.09, 0.11, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            hint_text_color=(0.6, 0.6, 0.6, 1)
        )
        
        self.pass_input = TextInput(
            hint_text="Password",
            password=True,
            multiline=False,
            size_hint_y=0.45,
            padding=[10, 10],
            background_color=(0.09, 0.11, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            hint_text_color=(0.6, 0.6, 0.6, 1)
        )
        
        input_box.add_widget(self.email_input)
        input_box.add_widget(self.pass_input)

        # Buttons
        btn_box = BoxLayout(orientation='vertical', size_hint_y=0.35, spacing=10)

        # Standard Login Button
        login_btn = Button(
            text="Continue",
            size_hint_y=0.3,
            background_color=(0.99, 0.6, 0, 1), # Amazon Orange
            color=(0, 0, 0, 1),
            bold=True
        )
        login_btn.bind(on_release=self.go_to_home)

        # Google Sign-In Button
        google_btn = Button(
            text="🌐 Sign in with Google (Gmail)",
            size_hint_y=0.3,
            background_color=(0.2, 0.2, 0.25, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        google_btn.bind(on_release=self.go_to_home)

        # Skip / Guest Button
        guest_btn = Button(
            text="Skip & Continue as Guest >",
            size_hint_y=0.25,
            background_color=(0, 0, 0, 0), # Transparent
            color=(0.6, 0.8, 1, 1)
        )
        guest_btn.bind(on_release=self.go_to_home)

        btn_box.add_widget(login_btn)
        btn_box.add_widget(google_btn)
        btn_box.add_widget(guest_btn)

        layout.add_widget(logo)
        layout.add_widget(welcome_label)
        layout.add_widget(input_box)
        layout.add_widget(btn_box)

        self.add_widget(layout)

    def go_to_home(self, instance):
        self.manager.current = 'home'


# ================= 2. HOME SCREEN =================
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main_layout = BoxLayout(orientation='vertical')

        # ---------------- TOP BAR ----------------
        top_bar = BoxLayout(size_hint_y=None, height=55, padding=[10, 5], spacing=10)
        with top_bar.canvas.before:
            Color(0.14, 0.18, 0.24, 1)
            RoundedRectangle(pos=top_bar.pos, size=top_bar.size)

        logo = Label(
            text="[b][color=ff9900]amazon[/color][color=ffffff] zone[/color][/b]",
            markup=True,
            font_size='20sp',
            size_hint_x=0.35,
            halign='left',
            valign='middle'
        )
        logo.bind(size=logo.setter('text_size'))

        search_input = TextInput(
            hint_text="🔍 Search...",
            multiline=False,
            size_hint_x=0.5,
            padding=[10, 8],
            background_color=(0.09, 0.11, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            hint_text_color=(0.6, 0.6, 0.6, 1)
        )

        cart_btn = Button(
            text="🛒 3",
            size_hint_x=0.15,
            background_color=(0.99, 0.6, 0, 1),
            bold=True
        )

        top_bar.add_widget(logo)
        top_bar.add_widget(search_input)
        top_bar.add_widget(cart_btn)
        main_layout.add_widget(top_bar)

        # ---------------- MAIN SCROLLABLE CONTENT ----------------
        scroll = ScrollView()
        content_layout = BoxLayout(orientation='vertical', size_hint_y=None, padding=10, spacing=15)
        content_layout.bind(minimum_height=content_layout.setter('height'))

        # BANNER
        banner = CustomCard(
            bg_color=(0.99, 0.6, 0, 1),
            size_hint_y=None,
            height=90,
            padding=15,
            orientation='vertical'
        )
        banner.add_widget(Label(text="[b]TODAY'S BIG DEALS[/b]", markup=True, font_size='18sp', color=(0,0,0,1)))
        banner.add_widget(Label(text="Up to 50% OFF on Electronics & Fashion", font_size='13sp', color=(0.1,0.1,0.1,1)))
        content_layout.add_widget(banner)

        # CATEGORIES HORIZONTAL SCROLL
        cat_scroll = ScrollView(size_hint_y=None, height=40, do_scroll_y=False)
        cat_grid = BoxLayout(spacing=10, size_hint_x=None)
        cat_grid.bind(minimum_width=cat_grid.setter('width'))

        categories = ["🔥 Deals", "📱 Electronics", "👗 Fashion", "🏠 Home", "🎮 Gaming"]
        for cat in categories:
            btn = Button(
                text=cat,
                size_hint_x=None,
                width=110,
                background_color=(0.14, 0.18, 0.24, 1),
                color=(1, 1, 1, 1)
            )
            cat_grid.add_widget(btn)

        cat_scroll.add_widget(cat_grid)
        content_layout.add_widget(cat_scroll)

        # PRODUCTS GRID
        grid = GridLayout(cols=2, spacing=12, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        products = [
            {"name": "Echo Dot Smart Speaker", "price": "$39.99", "orig": "$49.99", "stars": "⭐⭐⭐⭐☆ 4.6"},
            {"name": "Kindle Paperwhite 16GB", "price": "$129.99", "orig": "$149.99", "stars": "⭐⭐⭐⭐⭐ 4.9"},
            {"name": "Wireless Headphones", "price": "$89.00", "orig": "$119.00", "stars": "⭐⭐⭐⭐☆ 4.7"},
            {"name": "Smart Fitness Watch", "price": "$55.50", "orig": "$70.00", "stars": "⭐⭐⭐⭐☆ 4.5"},
        ]

        for p in products:
            card = CustomCard(
                orientation='vertical',
                size_hint_y=None,
                height=180,
                padding=10,
                spacing=5
            )
            
            stars = Label(text=p["stars"], font_size='11sp', size_hint_y=0.15, color=(0.99, 0.6, 0, 1), halign='left')
            stars.bind(size=stars.setter('text_size'))
            
            title = Label(text=f"[b]{p['name']}[/b]", markup=True, font_size='13sp', size_hint_y=0.35, halign='left', valign='top')
            title.bind(size=title.setter('text_size'))

            price = Label(text=f"[color=ff9900][b]{p['price']}[/b][/color]  [color=888888][s]{p['orig']}[/s][/color]", markup=True, font_size='13sp', size_hint_y=0.2, halign='left')
            price.bind(size=price.setter('text_size'))

            add_btn = Button(
                text="Add to Cart",
                size_hint_y=0.3,
                background_color=(0.99, 0.6, 0, 1),
                color=(0, 0, 0, 1),
                bold=True
            )

            card.add_widget(stars)
            card.add_widget(title)
            card.add_widget(price)
            card.add_widget(add_btn)

            grid.add_widget(card)

        content_layout.add_widget(grid)
        scroll.add_widget(content_layout)
        main_layout.add_widget(scroll)

        # ---------------- BOTTOM NAVIGATION BAR ----------------
        bottom_nav = BoxLayout(size_hint_y=None, height=50, spacing=2)
        nav_items = ["🏠 Home", "📂 Categories", "🔔 Alerts", "👤 Profile"]
        
        for nav in nav_items:
            btn = Button(
                text=nav,
                background_color=(0.14, 0.18, 0.24, 1),
                color=(1, 1, 1, 1),
                font_size='11sp'
            )
            bottom_nav.add_widget(btn)

        main_layout.add_widget(bottom_nav)

        self.add_widget(main_layout)


# ================= 3. MAIN APP MANAGER =================
class AmazonApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        return sm

if __name__ == '__main__':
    AmazonApp().run()
