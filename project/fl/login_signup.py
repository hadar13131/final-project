from project.models import Set, Exercise
import json
import hashlib

import calendar
from datetime import datetime

import flet as ft
import calendar
from datetime import datetime
from project.client import Client

from menu_page import MenuApp
import welcome_page
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
        self.button1 = ft.ElevatedButton(text="Login", on_click=self.click1, bgcolor='#E1F3F1', color='black')
        self.massageL1 = ft.TextField(read_only=True, border="none", color='#A8468C')

        self.button_Next = ft.ElevatedButton(text="continue", on_click=self.go_to_menu, bgcolor='#E1F3F1',
                                             color='black')

        self.button_Back = ft.ElevatedButton(text="BACK", on_click=self.back_to_welcome, bgcolor='#CC99FF', color='black')


        self.main_panel_login = ft.Column(
            alignment=ft.alignment.top_left,
            controls=[
                self.button_Back,
                ft.Container(
                    margin=20,
                    padding=20,
                    # height=10,
                    # width=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    border=ft.border.all(30, '#E1F3F1'),
                    content=ft.Column(
                        [

                            ft.Text("WELCOME BACK!", size=55, color=ft.colors.BLACK, weight=ft.FontWeight.W_500,
                                    selectable=True, font_family="Century Gothic"),

                                        ft.Text("login-", size=30, color=ft.colors.BLACK, weight=ft.FontWeight.W_500,
                                                selectable=True,
                                                font_family="Century Gothic"),
                                        self.email1,
                                        self.username1,
                                        self.password1,
                                        self.button1,
                                        self.massageL1
                                    ]
                                )
                            )

                        ]
                    )




    def back_to_welcome(self, e: ft.ControlEvent) -> None:
        self.page.clean()
        app_instance = welcome_page.First_page()
        app_instance.main(self.page)

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
        password = hashlib.sha256(password.encode()).hexdigest()

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
                    self.page.clean()
                    app_instance = MenuApp(client=self.client)
                    app_instance.main(self.page)
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
        self.page.bgcolor = "#DEE5FE"

        self.page.update()

def main() -> None:
    ft.app(target=LoginPage().main)


if __name__ == "__main__":
    main()


class SignUpPage:
    def __init__(self) -> None:
        self.page = None
        self.client = Client()

        self.button_Back = ft.ElevatedButton(text="BACK", on_click=self.back_to_welcome, bgcolor='#CC99FF', color='black')

        self.button_Back_to_email = ft.ElevatedButton(text="BACK TO EMAIL", on_click=self.back_to_email,
                                                      bgcolor='#CC99FF', color='black')

        self.button_Back_to_password = ft.ElevatedButton(text="BACK", on_click=self.back_to_password,
                                                      bgcolor='#CC99FF', color='black')

        self.button_go_to_login = ft.ElevatedButton(text="go to login", on_click=self.go_to_login,
                                                         bgcolor='#CC99FF', color='black')


        self.username2 = ft.TextField(label="User Name", autofocus=True, border_color='#8532B8')
        self.password2 = ft.TextField(label="Password", autofocus=True, password=True, can_reveal_password=True,
                                      border_color='#8532B8')

        self.button2 = ft.ElevatedButton(text="Sign Up", on_click=self.click2, bgcolor='#E1F3F1', color='black')
        self.massageS2 = ft.TextField(read_only=True, border="none", color='#A8468C')


        self.firstname2 = ft.TextField(label="first name", autofocus=True, border_color='#8532B8')
        self.lastname2 = ft.TextField(label="last name", autofocus=True, border_color='#8532B8')
        self.phone_number = ft.TextField(label="phone number", autofocus=True, border_color='#8532B8')
        self.email = ft.TextField(label="email", autofocus=True, border_color='#8532B8')
        self.massageE = ft.TextField(read_only=True, border="none", color='#A8468C')
        self.age = ft.TextField(label="age", autofocus=True, border_color='#8532B8')

        # self.gender = ft.TextField(label="gender", autofocus=True, border_color='#8532B8')
        self.gender = ft.Dropdown(
            label="gender",
            border_color='#8532B8',
            width=100,
            options=[
                ft.dropdown.Option("Female"),
                ft.dropdown.Option("Male"),
                ft.dropdown.Option("Other"),
            ],
        )

        self.goals = ft.TextField(label="goals", autofocus=True, border_color='#8532B8')

        self.button_send_info = ft.ElevatedButton(text="Send", on_click=self.click_info, bgcolor='#E1F3F1', color='black')
        self.massageF1 = ft.TextField(read_only=True, border="none", color='#A8468C')

        self.button_Next = ft.ElevatedButton(text="continue", on_click=self.go_to_menu, bgcolor='#8532B8',
                                             color='white')


        self.email_panel = ft.Column(
            alignment=ft.alignment.top_left,
            controls=[
                self.button_Back,
                ft.Container(
                    margin=20,
                    padding=20,
                    # height=10,
                    # width=10,
                    # alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    border=ft.border.all(30, '#E1F3F1'),
                    content=ft.Column(
                        [
                            ft.Text("sign up", size=30, color='black', weight=ft.FontWeight.W_500, selectable=True,
                                    font_family="Century Gothic"),

                            ft.Text("First, enter your email", size=20, color='black', weight=ft.FontWeight.W_500,
                                    selectable=True,
                                    font_family="Century Gothic"),
                            self.email,
                            self.massageE,
                            ft.ElevatedButton(text="check email", on_click=self.go_to_check_email, bgcolor='#E1F3F1',
                                              color='black'),
                        ]
                    )
                )

            ]
        )


        self.main_panel_signup = ft.Column(
            alignment=ft.alignment.top_left,
            controls=[
                self.button_Back_to_email,
                ft.Container(
                    margin=20,
                    padding=20,
                    # height=10,
                    # width=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    border=ft.border.all(30, '#E1F3F1'),
                    content=ft.Column(
                        [

                            ft.Text("sign up", size=55, color='#8532B8', weight=ft.FontWeight.W_500, selectable=True,
                                    font_family="Elephant"),
                            self.username2,
                            self.password2,
                            self.button2,
                            self.massageS2,

                        ]
                    )
                )

            ]
        )


        self.main_panel_signup2 = ft.Column(
            alignment=ft.alignment.top_left,
            controls=[
                self.button_Back_to_password,
                ft.Container(
                    margin=20,
                    padding=20,
                    # height=10,
                    # width=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    border=ft.border.all(30, '#E1F3F1'),
                    content=ft.Column(
                        [
                            ft.Text("Enter your details", size=55, color=ft.colors.BLACK, weight=ft.FontWeight.W_500,
                                    selectable=True, font_family="Century Gothic"),
                            self.firstname2,
                            self.lastname2,
                            self.phone_number,
                            # self.email,
                            self.age,
                            self.gender,
                            self.goals,
                            self.button_send_info,
                            self.massageF1

                        ]
                    )
                )

            ]
        )

    def go_to_login(self, e: ft.ControlEvent):
        self.page.clean()
        app_instance = LoginPage()
        app_instance.main(self.page)


    def back_to_welcome(self, e: ft.ControlEvent) -> None:
        self.page.clean()
        app_instance = welcome_page.First_page()
        app_instance.main(self.page)

    def back_to_email(self, e: ft.ControlEvent) -> None:
        self.page.clean()
        row_container = ft.Row([self.email_panel], auto_scroll=True)
        row_container.main_alignment = ft.MainAxisAlignment.CENTER

        row_container.width = 650
        self.page.add(row_container)

        self.page.horizontal_alignment = 'CENTER'
        self.page.vertical_alignment = 'CENTER'

        self.page.update()

    def back_to_password(self, e: ft.ControlEvent) -> None:
        #delete the username and the password theye fill at the last page and insert to the database
        response = self.client.delete(self.username2.value, self.password2.value)
        # self.massageS2.value = response["response"]
        self.client = Client()
        self.page.clean()

        row_container = ft.Row([self.main_panel_signup], auto_scroll=True)
        row_container.main_alignment = ft.MainAxisAlignment.CENTER

        row_container.width = 650
        self.page.add(row_container)

        self.page.horizontal_alignment = 'CENTER'
        self.page.vertical_alignment = 'CENTER'

        self.page.update()



    def go_to_check_email(self, e: ft.ControlEvent) -> None:
        email = self.email.value
        if email:
            if c_e.is_valid_email(email):
                response = self.client.check_email(email)
                self.massageE.value = response["response"]

                if self.massageE.value == "the email is valid":

                    self.page.clean()
                    row_container = ft.Row([self.main_panel_signup], auto_scroll=True)
                    row_container.main_alignment = ft.MainAxisAlignment.CENTER

                    row_container.width = 650
                    self.page.add(row_container)

                    self.page.horizontal_alignment = 'CENTER'
                    self.page.vertical_alignment = 'CENTER'
                    self.page.update()

                else:
                    self.page.add(self.button_go_to_login)
                    self.page.update()

            else:
                self.massageE.value = "the email is not write correctly"

        else:
            self.massageE.value = "please enter your email"

        self.page.update()

    # def go_to_fill_info(self, e: ft.ControlEvent) -> None:
    #     self.page.clean()
    #     row = ft.Row([self.main_panel_signup2])
    #     self.page.add(row)
    #
    #     self.page.update()

    # to signup
    def click2(self, e: ft.ControlEvent) -> None:
        username = self.username2.value
        password = self.password2.value
        password = hashlib.sha256(password.encode()).hexdigest()

        self.username2.error_text = ""
        self.password2.error_text = ""

        if username and password:
            response = self.client.signup(username, password)
            self.massageS2.value = response["response"]

            if self.massageS2.value == "signup success":
                self.page.clean()
                row_container = ft.Row([self.main_panel_signup2], auto_scroll=True)
                row_container.main_alignment = ft.MainAxisAlignment.CENTER

                row_container.width = 650
                self.page.add(row_container)

                self.page.horizontal_alignment = 'CENTER'
                self.page.vertical_alignment = 'CENTER'
                self.page.update()

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
            if c_e.is_valid_phone_number(phone_number):
                response = self.client.fill_info(name=username1, first_name=firstname, last_name=lastname,
                                                 phone_num=phone_number, email=email, age=age, gender=gender, goals=goals)
                self.massageF1.value = response["response"]

                if self.massageF1.value == "the information added":
                    self.page.clean()
                    app_instance = MenuApp(client=self.client)
                    app_instance.main(self.page)
                    # row = ft.Row([self.button_Next])
                    # self.page.add(row)
                self.page.update()

            else:
                self.massageF1.value = "the phone number is not write correctly"
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
        self.page.bgcolor = "#DEE5FE"

        self.page.update()


def main() -> None:
    ft.app(target=SignUpPage().main)


if __name__ == "__main__":
    main()









