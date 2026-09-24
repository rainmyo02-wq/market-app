from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
from kivy.metrics import dp

# Amazon Dark Mode Theme Colors
Window.clearcolor = (0.09, 0.11, 0.15, 1)

class CustomCard(BoxLayout):
    """ Custom Card with Responsive Height and Rounded Background """
    def __init__(self, bg_color=(0.14, 0.18, 0.24, 1), radius=[8], **kwargs):
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
        
        # Center Content Container
        main_box = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        # Centered Inner Form
        form_box = BoxLayout(orientation='vertical', size_hint_y=None, spacing=dp(12))
        form_box.bind(minimum_height=form_box.setter('height'))

        # Header
        logo = Label(
            text="[b][color=ff9900]amazon[/color][color=ffffff] zone[/color][/b]",
            markup=True,
            font_size='32sp',
            size_hint_y=None,
            height=dp(50)
        )
        
        welcome_label = Label(
            text="Sign in to your account",
            font_size='15sp',
            size_hint_y=None,
            height=dp(25),
            color=(0.8, 0.8, 0.8, 1)
        )

        # Input Box
        input_card = CustomCard(
            orientation='vertical', 
            size_hint_y=None,
            height=dp(110),
            padding=dp(10), 
            spacing=dp(8),
            bg_color=(0.14, 0.18, 0.24, 1)
        )
        
        self.email_input = TextInput(
            hint_text="Email or Phone Number",
            multiline=False,
            size_hint_y=None,
            height=dp(40),
            padding=[dp(10), dp(10)],
            background_color=(0.09, 0.11, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            hint_text_color=(0.5, 0.5, 0.5, 1)
        )
        
        self.pass_input = TextInput(
            hint_text="Password",
            password=True,
            multiline=False,
            size_hint_y=None,
            height=dp(40),
            padding=[dp(10), dp(10)],
            background_color=(0.09, 0.11, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            hint_text_color=(0.5, 0.5, 0.5, 1)
        )
        
        input_card.add_widget(self.email_input)
        input_card.add_widget(self.pass_input)

        # Buttons
        login_btn = Button(
            text="Continue",
            size_hint_y=None,
            height=dp(45),
            background_color=(0.99, 0.6, 0, 1),
            color=(0, 0, 0, 1),
            bold=True
        )
        login_btn.bind(on_release=self.go_to_home)

        google_btn = Button(
            text="Sign in with Google (Gmail)",
            size_hint_y=None,
            height=dp(45),
            background_color=(0.2, 0.2, 0.25, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        google_btn.bind(on_release=self.go_to_home)

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
        form_box.add_widget(input_card)
        form_box.add_widget(login_btn)
        form_box.add_widget(google_btn)
        form_box.add_widget(guest_btn)

        # Push to middle
        main_box.add_widget(Label(size_hint_y=0.15))
        main_box.add_widget(form_box)
        main_box.add_widget(Label(size_hint_y=0.15))

        self.add_widget(main_box)

    def go_to_home(self, instance):
        self.manager.current = 'home'


# ================= 2. HOME SCREEN =================
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main_layout = BoxLayout(orientation='vertical')

        # ---------------- TOP BAR ----------------
        top_bar = BoxLayout(size_hint_y=None, height=dp(55), padding=[dp(8), dp(5)], spacing=dp(8))
        with top_bar.canvas.before:
            Color(0.14, 0.18, 0.24, 1)
            RoundedRectangle(pos=top_bar.pos, size=top_bar.size)

        logo = Label(
            text="[b][color=ff9900]amazon[/color][/b]",
            markup=True,
            font_size='18sp',
            size_hint_x=0.3,
            halign='center',
            valign='middle'
        )

        search_input = TextInput(
            hint_text="Search Amazon...",
            multiline=False,
            size_hint_x=0.5,
            padding=[dp(8), dp(8)],
            background_color=(0.09, 0.11, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            hint_text_color=(0.5, 0.5, 0.5, 1)
        )

        cart_btn = Button(
            text="Cart (3)",
            size_hint_x=0.2,
            background_color=(0.99, 0.6, 0, 1),
            color=(0, 0, 0, 1),
            bold=True
        )

        top_bar.add_widget(logo)
        top_bar.add_widget(search_input)
        top_bar.add_widget(cart_btn)
        main_layout.add_widget(top_bar)

        # ---------------- MAIN CONTENT ----------------
        scroll = ScrollView()
        content_layout = BoxLayout(orientation='vertical', size_hint_y=None, padding=dp(10), spacing=dp(12))
        content_layout.bind(minimum_height=content_layout.setter('height'))

        # BANNER
        banner = CustomCard(
            bg_color=(0.99, 0.6, 0, 1),
            size_hint_y=None,
            height=dp(75),
            padding=dp(8),
            orientation='vertical'
        )
        banner.add_widget(Label(text="[b]TODAY'S BIG DEALS[/b]", markup=True, font_size='16sp', color=(0,0,0,1)))
        banner.add_widget(Label(text="Up to 50% OFF on Electronics", font_size='12sp', color=(0.1,0.1,0.1,1)))
        content_layout.add_widget(banner)

        # CATEGORIES HORIZONTAL SCROLL
        cat_scroll = ScrollView(size_hint_y=None, height=dp(38), do_scroll_y=False)
        cat_grid = BoxLayout(spacing=dp(8), size_hint_x=None)
        cat_grid.bind(minimum_width=cat_grid.setter('width'))

        categories = ["Deals", "Electronics", "Fashion", "Home", "Gaming"]
        for cat in categories:
            btn = Button(
                text=cat,
                size_hint_x=None,
                width=dp(95),
                background_color=(0.14, 0.18, 0.24, 1),
                color=(1, 1, 1, 1)
            )
            cat_grid.add_widget(btn)

        cat_scroll.add_widget(cat_grid)
        content_layout.add_widget(cat_scroll)

        # PRODUCTS GRID WITH IMAGES
        grid = GridLayout(cols=2, spacing=dp(10), size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        products = [
            {
                "name": "Echo Dot Smart", 
                "price": "$39.99", 
                "orig": "$49.99", 
                "stars": "Rating: 4.6",
                "img": "https://m.media-amazon.com/images/I/6182S7MYCBL._AC_SL1000_.jpg"
            },
            {
                "name": "Kindle Paperwhite", 
                "price": "$129.99", 
                "orig": "$149.99", 
                "stars": "Rating: 4.9",
                "img": "https://m.media-amazon.com/images/I/61fI1A07dSL._AC_SL1000_.jpg"
            },
            {
                "name": "Headphones", 
                "price": "$89.00", 
                "orig": "$119.00", 
                "stars": "Rating: 4.7",
                "img": "https://m.media-amazon.com/images/I/51+u4+h36QL._AC_SL1000_.jpg"
            },
            {
                "name": "Fitness Watch", 
                "price": "$55.50", 
                "orig": "$70.00", 
                "stars": "Rating: 4.5",
                "img": "https://m.media-amazon.com/images/I/61ZjlBOp+rL._AC_SL1500_.jpg"
            },
        ]

        for p in products:
            card = CustomCard(
                orientation='vertical',
                size_hint_y=None,
                height=dp(230),
                padding=dp(8),
                spacing=dp(4)
            )
            
            # Product Image
            p_img = AsyncImage(
                source=p["img"],
                size_hint_y=None,
                height=dp(85),
                allow_stretch=True,
                keep_ratio=True
            )

            stars = Label(
                text=p["stars"], 
                font_size='10sp', 
                size_hint_y=None, 
                height=dp(18),
                color=(0.99, 0.6, 0, 1), 
                halign='left', 
                valign='middle'
            )
            stars.bind(size=stars.setter('text_size'))
            
            title = Label(
                text=f"[b]{p['name']}[/b]", 
                markup=True, 
                font_size='12sp', 
                size_hint_y=None, 
                height=dp(32),
                halign='left', 
                valign='top'
            )
            title.bind(size=title.setter('text_size'))

            price = Label(
                text=f"[color=ff9900][b]{p['price']}[/b][/color]  [color=888888][s]{p['orig']}[/s][/color]", 
                markup=True, 
                font_size='12sp', 
                size_hint_y=None, 
                height=dp(22),
                halign='left',
                valign='middle'
            )
            price.bind(size=price.setter('text_size'))

            add_btn = Button(
                text="Add to Cart",
                size_hint_y=None,
                height=dp(32),
                background_color=(0.99, 0.6, 0, 1),
                color=(0, 0, 0, 1),
                bold=True
            )

            card.add_widget(p_img)
            card.add_widget(stars)
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
