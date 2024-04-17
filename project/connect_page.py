from models import Set, Exercise
import json

import calendar
from datetime import datetime

import flet as ft
import calendar
from datetime import datetime
from client import Client

import menu_page


# import organize_fl3

# from organize_fl3 import main as main6

class App:  # login, signup, delete user

    def __init__(self) -> None:
        self.page = None
        self.client = Client()

        # Create a button to navigate to App3 page
        self.button_Next = ft.ElevatedButton(text="continue", on_click=self.go_to_menu, bgcolor='#8532B8',
                                             color='white')

        self.button_fill_info = ft.ElevatedButton(text="continue to fill info", on_click=self.go_to_fill_info,
                                                  bgcolor='#8532B8', color='white')

        self.text1 = ft.Text("login", size=55, color='#8532B8', weight=ft.FontWeight.W_500, selectable=True,
                             font_family="Elephant")
        self.username1 = ft.TextField(label="User Name", autofocus=True, border_color='#8532B8')
        self.password1 = ft.TextField(label="Password", autofocus=True, password=True, can_reveal_password=True,
                                      border_color='#8532B8')
        self.button1 = ft.ElevatedButton(text="Login", on_click=self.click1, bgcolor='#8532B8', color='white')
        self.massageL1 = ft.TextField(read_only=True, border="none", color='#A8468C')

        self.main_panel_login = ft.Column(
            [
                self.text1,
                self.username1,
                self.password1,
                self.button1,
                self.massageL1
            ]
            # ,
            # scroll=ft.ScrollMode.ALWAYS,
            # height=1000
        )

        self.text2 = ft.Text("sign up", size=55, color='#8532B8', weight=ft.FontWeight.W_500, selectable=True,
                             font_family="Elephant")
        self.username2 = ft.TextField(label="User Name", autofocus=True, border_color='#8532B8')
        self.password2 = ft.TextField(label="Password", autofocus=True, password=True, can_reveal_password=True,
                                      border_color='#8532B8')
        self.button2 = ft.ElevatedButton(text="Sign Up", on_click=self.click2, bgcolor='#8532B8', color='white')
        self.massageS2 = ft.TextField(read_only=True, border="none", color='#A8468C')

        self.text_info_title = ft.Text("Enter your info", size=55, color='#8532B8', weight=ft.FontWeight.W_500,
                                       selectable=True, font_family="Elephant")
        self.firstname2 = ft.TextField(label="first name", autofocus=True, border_color='#8532B8')
        self.lastname2 = ft.TextField(label="last name", autofocus=True, border_color='#8532B8')
        self.phone_number = ft.TextField(label="phone number", autofocus=True, border_color='#8532B8')
        self.email = ft.TextField(label="email", autofocus=True, border_color='#8532B8')
        self.age = ft.TextField(label="age", autofocus=True, border_color='#8532B8')

        # self.gender = ft.TextField(label="gender", autofocus=True, border_color='#8532B8')
        self.gender = ft.Dropdown(
            width=100,
            options=[
                ft.dropdown.Option("Female"),
                ft.dropdown.Option("Male"),
                ft.dropdown.Option("Other"),
            ],
        )


        self.goals = ft.TextField(label="goals", autofocus=True, border_color='#8532B8')

        self.button_send_info = ft.ElevatedButton(text="Send", on_click=self.click_info, bgcolor='#8532B8',
                                                  color='white')
        self.massageF1 = ft.TextField(read_only=True, border="none", color='#A8468C')

        self.main_panel_signup = ft.Column(
            [
                self.text2,
                self.username2,
                self.password2,
                self.button2,
                self.massageS2
            ]
            # ,
            # scroll=ft.ScrollMode.ALWAYS,
            # height=100
        )

        self.main_panel_signup2 = ft.Column(
            [
                self.text_info_title,
                self.firstname2,
                self.lastname2,
                self.phone_number,
                self.email,
                self.age,
                self.gender,
                self.goals,
                self.button_send_info,
                self.massageF1,
                self.button_Next
            ]
            # ,
            # scroll=ft.ScrollMode.ALWAYS,
            # height=100
        )

        self.main_panel_bottom = ft.Column(
            [
                self.button_Next
            ])

        self.main_panel_add_info = ft.Column(
            [
                self.button_fill_info
            ])

        self.text3 = ft.Text("delete", size=55, color='#8532B8', weight=ft.FontWeight.W_500, selectable=True,
                             font_family="Elephant")
        self.username3 = ft.TextField(label="User Name", autofocus=True, border_color='#8532B8')
        self.password3 = ft.TextField(label="Password", autofocus=True, password=True, can_reveal_password=True,
                                      border_color='#8532B8')
        self.button3 = ft.ElevatedButton(text="Delete", on_click=self.click3, bgcolor='#8532B8', color='white')
        self.massageD3 = ft.TextField(read_only=True, border="none", color='#A8468C')

        self.main_panel_delete = ft.Column(
            [
                self.text3,
                self.username3,
                self.password3,
                self.button3,
                self.massageD3
            ]
            # ,
            # scroll=ft.ScrollMode.ALWAYS,
            # height=100
        )

    def go_to_menu(self, e: ft.ControlEvent) -> None:
        # Function to navigate to App3 page
        self.page.clean()
        app_instance = menu_page.MenuApp(client=self.client)
        app_instance.main(self.page)

    # to authenticate
    def click1(self, e: ft.ControlEvent) -> None:
        username = self.username1.value
        password = self.password1.value

        # error massages
        self.username1.error_text = ""
        self.password1.error_text = ""

        # if the user put username and password
        if username and password:
            response = self.client.authenticate(name=username, password=password)
            self.massageL1.value = response["response"]
            if self.massageL1.value == "user authenticated":
                self.page.add(self.button_Next)
            self.page.update()

        # if the user put password and not username
        elif (not username) and password:
            self.username1.error_text = "Please enter your username"
            self.page.update()

        # if the user put username and not password
        elif (not password) and username:
            self.password1.error_text = "Please enter your password"
            self.page.update()

        # if the user not put username and password
        else:
            self.password1.error_text = "Please enter your password"
            self.username1.error_text = "Please enter your username"
            self.page.update()

    def go_to_fill_info(self, e: ft.ControlEvent) -> None:
        self.page.clean()
        row = ft.Row([self.main_panel_signup2])
        self.page.add(row)

        self.page.update()

    # to signup
    def click2(self, e: ft.ControlEvent) -> None:
        username = self.username2.value
        password = self.password2.value

        self.username2.error_text = ""
        self.password2.error_text = ""

        if username and password:
            response = self.client.signup(username, password)
            self.massageS2.value = response["response"]

            if self.massageS2.value == "signup success":
                row = ft.Row([self.button_fill_info])
                self.page.add(row)

            self.page.update()

        elif (not username) and password:
            self.username2.error_text = "Please enter your username"
            self.page.update()

        elif (not password) and username:
            self.password2.error_text = "Please enter your password"
            self.page.update()

        else:
            self.password2.error_text = "Please enter your password"
            self.username2.error_text = "Please enter your username"
            self.page.update()

    def click_info(self, e: ft.ControlEvent) -> None:
        # self.client = client
        username1 = self.client.username

        firstname = self.firstname2.value
        lastname = self.lastname2.value
        phone_number = self.phone_number.value
        email = self.email.value
        age = int(self.age.value)
        gender = self.gender.value
        goals = self.goals.value

        if firstname and lastname and phone_number and email and age and gender and goals:
            response = self.client.fill_info(name=username1, first_name=firstname, last_name=lastname,
                                             phone_num=phone_number, email=email, age=age, gender=gender, goals=goals)
            self.massageF1.value = response["response"]

            if self.massageF1.value == "the information added":
                row = ft.Row([self.button_Next])
                self.page.add(row)
            self.page.update()

        else:
            self.massageF1.value = "please fill the all fields"
            self.page.update()

    # to delete
    def click3(self, e: ft.ControlEvent) -> None:
        username = self.username3.value
        password = self.password3.value

        self.username3.error_text = ""
        self.password3.error_text = ""

        if username and password:
            response = self.client.delete(username, password)
            self.massageD3.value = response["response"]

            self.page.update()

        elif (not username) and password:
            self.username3.error_text = "Please enter your username"
            self.page.update()

        elif (not password) and username:
            self.password3.error_text = "Please enter your password"
            self.page.update()

        else:
            self.password3.error_text = "Please enter your password"
            self.username3.error_text = "Please enter your username"
            self.page.update()

    def main(self, page: ft.Page) -> None:
        self.page = page

        row_container = ft.Row([self.main_panel_login, self.main_panel_signup], auto_scroll=True)
        row_container.main_alignment = ft.MainAxisAlignment.CENTER

        row_container.width = 650
        self.page.add(row_container)

        # row_container2 = ft.Row([self.main_panel_bottom])
        # row_container2.width = 200
        # self.page.add(row_container2)

        # self.page.add(self.main_panel_login, self.main_panel_signup)
        # self.page.add(self.main_panel_signup)

        self.page.horizontal_alignment = 'CENTER'
        self.page.vertical_alignment = 'CENTER'

        self.page.update()


def main() -> None:
    ft.app(target=App().main)


if __name__ == "__main__":
    main()
