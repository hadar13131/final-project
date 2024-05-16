from project.models import Set, Exercise
import json
import hashlib

import flet as ft
import calendar
from datetime import datetime
from project.client import Client
from menu_page import MenuApp
import welcome_page
import project.check_errors as c_e


class SendMassages:
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