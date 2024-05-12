from project.models import Set, Exercise
import json

import calendar
from datetime import datetime

import flet as ft
import math

# from login_signup import LoginPage
# from login_signup import SignUpPage

import login_signup
import learn_more_page



class First_page:

    def __init__(self) -> None:
        self.page = None
        # self.client = client

        # Create a button to navigate to App3 page
        self.text = ft.Text("Welcome To The Fitness App :)", size=55, color='#8532B8', weight=ft.FontWeight.W_500,
                            selectable=True, font_family="Elephant")

        self.button_to_login = ft.ElevatedButton(text="To login", on_click=self.go_to_login, bgcolor='#8532B8',
                                                 color='white')
        self.button_to_login = ft.CupertinoFilledButton(text="To login", on_click=self.go_to_login)

        self.button_to_signup = ft.ElevatedButton(text="To sign up", on_click=self.go_to_signup, bgcolor='#8532B8',
                                                  color='white')
        self.button_to_signup = ft.CupertinoFilledButton(text="To sign up", on_click=self.go_to_signup)

        self.button_to_learnmore = ft.ElevatedButton(text="To learn more", on_click=self.go_to_learnmore,
                                                     bgcolor='#8532B8',
                                                     color='white')


        self.main_panel = ft.Column(
            # width=600,
            controls=[
                ft.Row([
                    ft.Text("Welcome To ", size=55, color=ft.colors.BLACK, weight=ft.FontWeight.W_500,
                            selectable=True, font_family="Century Gothic"),
                    ft.Text("POWER APP ", size=80, color=ft.colors.BLACK, weight=ft.FontWeight.W_500,
                            selectable=True, font_family="Century Gothic")
                ]),
            ],
        )

        self.main_panel1 = ft.Row(
            # width=600,
            controls=[
                ft.Container(
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    # bgcolor='#CC99FF',
                    content=ft.Row(
                        [

                            self.button_to_login,
                            self.button_to_signup,
                            # self.button_to_learnmore
                        ]
                    )
                )
            ],
        )



    def go_to_login(self, e: ft.ControlEvent) -> None:
        # Function to navigate to App3 page
        self.page.clean()
        app_instance = login_signup.LoginPage()
        app_instance.main(self.page)

    def go_to_signup(self, e: ft.ControlEvent) -> None:
        # Function to navigate to App3 page
        self.page.clean()
        app_instance = login_signup.SignUpPage()
        app_instance.main(self.page)

    def go_to_learnmore(self, e: ft.ControlEvent) -> None:
        # Function to navigate to App3 page
        self.page.clean()
        app_instance = learn_more_page.LearnMorePage()
        app_instance.main(self.page)

    def main(self, page: ft.Page) -> None:
        self.page = page
        self.page.bgcolor = ft.colors.WHITE
        row_container = ft.Row([self.main_panel], auto_scroll=True)
        row_container.main_alignment = ft.MainAxisAlignment.CENTER

        row_container.width = 920
        self.page.add(row_container)
        self.page.update()


        row_container = ft.Row([self.main_panel1], auto_scroll=True)
        row_container.main_alignment = ft.MainAxisAlignment.CENTER

        row_container.width = 920
        self.page.add(row_container)
        self.page.update()


        # self.page.add(self.main_panel_login, self.main_panel_signup)
        # self.page.add(self.main_panel_signup)

        self.page.horizontal_alignment = 'CENTER'
        self.page.vertical_alignment = 'CENTER'

        self.page.add(self.main_panel)
        self.page.add(self.main_panel1)
        self.page.update()


def main() -> None:
    ft.app(target=First_page().main)


if __name__ == "__main__":
    main()
