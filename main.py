from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty
import json
import os

Window.size = (360, 640)

KV = '''
ScreenManager:
    LoginChoiceScreen:
    PhoneLoginScreen:
    OTPVerificationScreen:
    MainScreen:
    CartScreen:

<LoginChoiceScreen>:
    name: "login_choice"
    MDBoxLayout:
        orientation: "vertical"
        padding: "20dp"
        spacing: "20dp"
        pos_hint: {"center_x": .5, "center_y": .5}
        adaptive_height: True
        
        MDLabel:
            text: "Welcome to Shop Zone"
            font_style: "H5"
            halign: "center"
            
        MDRaisedButton:
            text: "Login with Phone Number"
            pos_hint: {"center_x": .5}
            on_release: app.root.current = "phone_login"

<PhoneLoginScreen>:
    name: "phone_login"
    MDBoxLayout:
        orientation: "vertical"
        padding: "20dp"
        spacing: "20dp"
        pos_hint: {"center_x": .5, "center_y": .5}
        adaptive_height: True
        
        MDLabel:
            text: "Enter Phone Number"
            font_style: "H5"
            halign: "center"
            
        MDTextField:
            id: phone_input
            hint_text: "+959..."
            mode: "rectangle"
            icon_left: "phone"
            
        MDRaisedButton:
            text: "Send SMS Code"
            pos_hint: {"center_x": .5}
            on_release: app.send_sms_code(phone_input.text)
            
        MDFlatButton:
            text: "Back"
            pos_hint: {"center_x": .5}
            on_release: app.root.current = "login_choice"

<OTPVerificationScreen>:
    name: "otp_verify"
    MDBoxLayout:
        orientation: "vertical"
        padding: "20dp"
        spacing: "20dp"
        pos_hint: {"center_x": .5, "center_y": .5}
        adaptive_height: True
        
        MDLabel:
            text: "Enter 6-digit Code"
            font_style: "H5"
            halign: "center"
            
        MDTextField:
            id: otp_input
            hint_text: "123456"
            mode: "rectangle"
            icon_left: "message-processing"
            
        MDRaisedButton:
            text: "Verify & Login"
            pos_hint: {"center_x": .5}
            on_release: app.verify_otp(otp_input.text)

<ProductCard>:
    orientation: "vertical"
    padding: "12dp"
    spacing: "8dp"
    size_hint_y: None
    height: "180dp"
    elevation: 2
    md_bg_color: 1, 1, 1, 1
    radius: [10, 10, 10, 10]
    
    MDIcon:
        icon: "image"
        font_size: "48sp"
        halign: "center"
        size_hint_y: None
        height: "60dp"
        pos_hint: {"center_x": .5}
        
    MDLabel:
        text: root.title
        theme_text_color: "Primary"
        font_style: "Subtitle1"
        halign: "center"
        
    MDLabel:
        text: root.price_str
        theme_text_color: "Secondary"
        halign: "center"
        
    MDRaisedButton:
        text: "Add to Cart"
        pos_hint: {"center_x": .5}
        on_release: app.add_to_cart(root.title, root.price)

<MainScreen>:
    name: "main"
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Shop Zone"
            elevation: 3
            right_action_items: [["cart", lambda x: app.goto_cart()], ["logout", lambda x: app.logout()]]
            
        ScrollView:
            MDGridLayout:
                id: product_grid
                cols: 2
                padding: "10dp"
                spacing: "10dp"
                size_hint_y: None
                height: self.minimum_height

<CartScreen>:
    name: "cart"
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Shopping Cart"
            elevation: 3
            left_action_items: [["arrow-left", lambda x: app.goto_main()]]
            
        ScrollView:
            MDList:
                id: cart_list
                
        MDBoxLayout:
            size_hint_y: None
            height: "80dp"
            padding: "20dp"
            spacing: "20dp"
            md_bg_color: 0.95, 0.95, 0.95, 1
            
            MDLabel:
                id: total_label
                text: "Total: $0"
                font_style: "H6"
                
            MDRaisedButton:
                text: "Checkout"
                pos_hint: {"center_y": .5}
                on_release: app.checkout()
'''

class LoginChoiceScreen(MDScreen):
    pass

class PhoneLoginScreen(MDScreen):
    pass

class OTPVerificationScreen(MDScreen):
    pass

class MainScreen(MDScreen):
    pass

class CartScreen(MDScreen):
    pass

class ProductCard(MDCard):
    title = StringProperty()
    price_str = StringProperty()
    price = NumericProperty()

class ShopApp(MDApp):
    cart_items = []

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def on_start(self):
        if os.path.exists("user_token.json"):
            self.goto_main()
            self.load_products()
        else:
            self.root.current = "login_choice"

    def load_products(self):
        products = [
            {"title": "Smartphone", "price": 299, "price_str": "$299"},
            {"title": "Laptop", "price": 899, "price_str": "$899"},
            {"title": "Headphones", "price": 50, "price_str": "$50"},
            {"title": "Smart Watch", "price": 120, "price_str": "$120"},
            {"title": "Wireless Mouse", "price": 25, "price_str": "$25"},
            {"title": "Keyboard", "price": 45, "price_str": "$45"}
        ]
        
        main_screen = self.root.get_screen('main')
        main_screen.ids.product_grid.clear_widgets()
        for item in products:
            card = ProductCard(title=item["title"], price_str=item["price_str"], price=item["price"])
            main_screen.ids.product_grid.add_widget(card)

    def send_sms_code(self, phone_number):
        if phone_number == "":
            return
        self.root.current = "otp_verify"

    def verify_otp(self, otp_code):
        mock_token = {"phone_logged_in": True}
        with open("user_token.json", "w") as f:
            json.dump(mock_token, f)
        self.goto_main()
        self.load_products()

    def goto_main(self):
        self.root.current = "main"

    def goto_cart(self):
        self.root.current = "cart"
        self.update_cart_ui()

    def add_to_cart(self, title, price):
        self.cart_items.append({"title": title, "price": price})

    def update_cart_ui(self):
        cart_screen = self.root.get_screen('cart')
        cart_list = cart_screen.ids.cart_list
        cart_list.clear_widgets()
        
        total = 0
        for item in self.cart_items:
            total += item["price"]
            item_row = TwoLineAvatarIconListItem(
                text=item["title"],
                secondary_text=f"${item['price']}"
            )
            cart_list.add_widget(item_row)
            
        cart_screen.ids.total_label.text = f"Total: ${total}"

    def checkout(self):
        if not self.cart_items:
            return
        self.cart_items.clear()
        self.update_cart_ui()
        self.goto_main()

    def logout(self):
        if os.path.exists("user_token.json"):
            os.remove("user_token.json")
        self.cart_items.clear()
        self.root.current = "login_choice"

if __name__ == "__main__":
    ShopApp().run()
