from project.models import Set, Exercise
import json

import calendar
from datetime import datetime

import flet as ft
import calendar
from datetime import datetime
from project.client import Client

from project.menu_page import MenuApp

import project.check_errors as c_e

class LoginPage:
    def __init__(self) -> None:
        self.page = None
        self.client = Client()

        self.text1 = ft.Text("login", size=55, color='#8532B8', weight=ft.FontWeight.W_500, selectable=True,
                             font_family="Elephant")
        self.text2 = ft.Text("WELCOME BACK!", size=55, color='#8532B8', weight=ft.FontWeight.W_500, selectable=True,
                             font_family="Elephant")

        self.email1 = ft.TextField(label="email", autofocus=True, border_color='#8532B8')
        self.username1 = ft.TextField(label="User Name", autofocus=True, border_color='#8532B8')
        self.password1 = ft.TextField(label="Password", autofocus=True, password=True, can_reveal_password=True,
                                      border_color='#8532B8')
        self.button1 = ft.ElevatedButton(text="Login", on_click=self.click1, bgcolor='#8532B8', color='white')
        self.massageL1 = ft.TextField(read_only=True, border="none", color='#A8468C')

        self.button_Next = ft.ElevatedButton(text="continue", on_click=self.go_to_menu, bgcolor='#8532B8',
                                             color='white')

        self.main_panel_login = ft.Column(
            [
                self.text1,
                self.text2,
                self.email1,
                self.username1,
                self.password1,
                self.button1,
                self.massageL1
            ])

    def go_to_menu(self, e: ft.ControlEvent) -> None:
        # Function to navigate to App3 page
        self.page.clean()
        app_instance = MenuApp(client=self.client)
        app_instance.main(self.page)

    # to authenticate
    def click1(self, e: ft.ControlEvent) -> None:
        email = self.email1.value
        username = self.username1.value
        password = self.password1.value

        # error massages
        self.email1.error_text = ""
        self.username1.error_text = ""
        self.password1.error_text = ""

        # if the user put username and password
        if email and username and password:
            if c_e.is_valid_email(email):
                response = self.client.authenticate2(email=email, name=username, password=password)
                self.massageL1.value = response["response"]
                if self.massageL1.value == "user authenticated":
                    self.page.add(self.button_Next)
                self.page.update()

            else:
                self.massageL1.value = "the email is not write correctly"
                self.page.update()

        # if the user put password and not username
        elif password and (not username) and email:
            self.username1.error_text = "Please enter your username"
            self.page.update()

        # if the user put username and not password
        elif (not password) and username and email:
            self.password1.error_text = "Please enter your password"
            self.page.update()

        elif password and username and (not email):
            self.email1.error_text = "Please enter your email"
            self.page.update()

        elif (not password) and (not username) and email:
            self.password1.error_text = "Please enter your password"
            self.username1.error_text = "Please enter your username"
            self.page.update()

        elif (not password) and username and (not email):
            self.password1.error_text = "Please enter your password"
            self.email1.error_text = "Please enter your email"
            self.page.update()

        elif password and (not username) and (not email):
            self.username1.error_text = "Please enter your username"
            self.email1.error_text = "Please enter your email"
            self.page.update()

        # if the user not put username and password
        else:
            self.password1.error_text = "Please enter your password"
            self.username1.error_text = "Please enter your username"
            self.email1.error_text = "Please enter your email"
            self.page.update()

    def main(self, page: ft.Page) -> None:
        self.page = page

        row_container = ft.Row([self.main_panel_login], auto_scroll=True)
        row_container.main_alignment = ft.MainAxisAlignment.CENTER

        row_container.width = 650
        self.page.add(row_container)

        self.page.horizontal_alignment = 'CENTER'
        self.page.vertical_alignment = 'CENTER'

        self.page.update()

def main() -> None:
    ft.app(target=LoginPage().main)


if __name__ == "__main__":
    main()






class SignUpPage:
    def __init__(self) -> None:
        self.page = None
        self.client = Client()

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
        self.massageE = ft.TextField(read_only=True, border="none", color='#A8468C')
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

        self.button_Next = ft.ElevatedButton(text="continue", on_click=self.go_to_menu, bgcolor='#8532B8',
                                             color='white')

        self.button_fill_info = ft.ElevatedButton(text="continue to fill info", on_click=self.go_to_fill_info,
                                                  bgcolor='#8532B8', color='white')


        self.email_panel = ft.Column(
            [
                ft.Text("sign up", size=55, color='#8532B8', weight=ft.FontWeight.W_500, selectable=True,
                        font_family="Elephant"),
                ft.Text("WE HAPPY YOU DECIDED TO ENJOY US", size=55, color='#8532B8', weight=ft.FontWeight.W_500,
                        selectable=True, font_family="Elephant"),
                ft.Text("First, enter your email", size=55, color='#8532B8', weight=ft.FontWeight.W_500, selectable=True,
                        font_family="Elephant"),
                self.email,
                self.massageE,
                ft.ElevatedButton(text="check email", on_click=self.go_to_check_email, bgcolor='#8532B8', color='white')
            ]
        )

        self.main_panel_signup = ft.Column(
            [
                self.text2,
                self.username2,
                self.password2,
                self.button2,
                self.massageS2
            ]
        )


        self.main_panel_signup2 = ft.Column(
            [
                self.text_info_title,
                self.firstname2,
                self.lastname2,
                self.phone_number,
                # self.email,
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


    def go_to_check_email(self, e: ft.ControlEvent) -> None:
        email = self.email.value
        if email:
            if c_e.is_valid_email(email):
                response = self.client.check_email(email)
                self.massageE.value = response["response"]

                if self.massageE.value == "the email is valid":

                    self.page.clean()
                    row = ft.Row([self.main_panel_signup])
                    self.page.add(row)
            else:
                self.massageE.value = "the email is not write correctly"

        else:
            self.massageE.value = "please enter your email"

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

    def go_to_menu(self, e: ft.ControlEvent) -> None:
        # Function to navigate to App3 page
        self.page.clean()
        app_instance = MenuApp(client=self.client)
        app_instance.main(self.page)

    def main(self, page: ft.Page) -> None:
        self.page = page

        row_container = ft.Row([self.email_panel], auto_scroll=True)
        row_container.main_alignment = ft.MainAxisAlignment.CENTER

        row_container.width = 650
        self.page.add(row_container)

        self.page.horizontal_alignment = 'CENTER'
        self.page.vertical_alignment = 'CENTER'

        self.page.update()


def main() -> None:
    ft.app(target=SignUpPage().main)


if __name__ == "__main__":
    main()









