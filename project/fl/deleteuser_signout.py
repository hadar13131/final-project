from project.models import Set, Exercise
import json

import calendar
from datetime import datetime

import flet as ft
import calendar
from datetime import datetime
from project.client import Client

# from login_signup import LoginPage
# from login_signup import SignUpPage
import login_signup
import welcome_page

class DeleteUserPage:
    def __init__(self, client: Client) -> None:
        self.page = None
        self.client = client

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

    def click3(self, e: ft.ControlEvent) -> None:
        username = self.username3.value
        password = self.password3.value

        self.username3.error_text = ""
        self.password3.error_text = ""

        if username and password:
            response = self.client.delete(username, password)
            self.massageD3.value = response["response"]
            self.client = Client()
            self.page.clean()
            app_instance = welcome_page.First_page()
            app_instance.main(self.page)

            # app_instance = login_signup.SignUpPage()
            # app_instance.main(self.page)
            # row_container = ft.Row([app_instance.main_panel_signup])
            # self.page.add(row_container)
            # self.page.update()
            # self.page.update()

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
        self.page.scroll = ft.ScrollMode.ALWAYS

        row_container = ft.Row([self.main_panel_delete], auto_scroll=True)
        row_container.main_alignment = ft.MainAxisAlignment.CENTER

        row_container.width = 650
        self.page.add(self.main_panel_delete)

        self.page.horizontal_alignment = 'CENTER'
        self.page.vertical_alignment = 'CENTER'

        self.page.update()

def main() -> None:
    ft.app(target=DeleteUserPage.main)


if __name__ == "__main__":
    main()

class SignOutPage:
    def __init__(self, client: Client) -> None:
        self.page = None
        self.client = client

        self.text3 = ft.Text("signout", size=55, color='#8532B8', weight=ft.FontWeight.W_500, selectable=True,
                             font_family="Elephant")
        self.username3 = ft.TextField(label="User Name", autofocus=True, border_color='#8532B8')
        self.password3 = ft.TextField(label="Password", autofocus=True, password=True, can_reveal_password=True,
                                      border_color='#8532B8')
        self.button3 = ft.ElevatedButton(text="signout", on_click=self.click3, bgcolor='#8532B8', color='white')
        self.massageD3 = ft.TextField(read_only=True, border="none", color='#A8468C')

        self.main_panel_signout = ft.Column(
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

    def click3(self, e: ft.ControlEvent) -> None:
        username = self.username3.value
        password = self.password3.value

        self.username3.error_text = ""
        self.password3.error_text = ""

        if username and password:
            response = self.client.signout(username, password)
            self.massageD3.value = response["response"]
            self.page.update()

            if self.massageD3.value == "the details are correct":
                self.client = Client()
                self.page.clean()
                app_instance = welcome_page.First_page()
                app_instance.main(self.page)

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
        self.page.scroll = ft.ScrollMode.ALWAYS

        row_container = ft.Row([self.main_panel_signout], auto_scroll=True)
        row_container.main_alignment = ft.MainAxisAlignment.CENTER

        row_container.width = 650
        self.page.add(self.main_panel_signout)

        self.page.horizontal_alignment = 'CENTER'
        self.page.vertical_alignment = 'CENTER'

        self.page.update()

def main() -> None:
    ft.app(target=DeleteUserPage.main)


if __name__ == "__main__":
    main()