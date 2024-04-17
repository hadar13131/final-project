import flet as ft
from client import Client
from models import Set, Exercise
import json

import calendar
from datetime import datetime
from fl4 import AddWorkout
from fl4 import Add_Exercise
from fl4 import App5
from fl4 import HomePage
from fl4 import CalendarApp
from fl4 import Profile_Page


class MenuApp:
    def __init__(self, client: Client) -> None:
        self.page = None
        self.client = client

    def profile_page(self):
        app_instance = Profile_Page(client=self.client)
        row_container = ft.Row([app_instance.profile_page_panel])
        return row_container
    def workout_calnder_page(self):
        app_instance = CalendarApp(self.client)
        return ft.SafeArea(ft.Text("workout calnder page"))
    def show_improvement_page(self):
        app_instance = App5(client=self.client)
        row_container = ft.Row([app_instance.show_improvement_panel])
        return row_container
        # return ft.SafeArea(ft.Text("show_improvement_page"))

    def handle_home_click(self, e=None):
        self.show_home_page()

    def show_home_page(self):
        self.page.clean()
        app_instance = HomePage(self.client)
        row_container = ft.Row([app_instance.home_page_panel])
        self.page.add(row_container)
        self.page.update()

        # row_container = ft.Row([app_instance.home_page_panel])
        # self.page.add(row_container)

    def change_page(self, e: ft.ControlEvent, page: ft.Page):
        selected_index = e.control.selected_index
        self.page = page
        if selected_index == 0: #profile page
            self.page.clean()
            app_instance = Profile_Page(client=self.client)
            app_instance.main(self.page)
            # self.page.add(ft.SafeArea(self.profile_page()))
            # app_instance = App3()
            # page = app_instance.main(page)
            # page.clean()

            # page.add(add_workout_page(page))  # Replace the current page with Commute Page

        elif selected_index == 1: #calendar
            self.page.clean()
            app_instance = CalendarApp(client=self.client)
            app_instance.main(self.page, self.client)

        elif selected_index == 2: #improvment
            self.page.clean()
            app_instance = App5(client=self.client)
            app_instance.main(self.page)
            # self.page.add(ft.SafeArea(self.show_improvement_page()))

    def main(self, page: ft.Page):
        self.page = page
        # app_instance = App3()
        self.page.title = "CupertinoNavigationBar Example"
        self.page.navigation_bar = ft.CupertinoNavigationBar(
            icon_size=30,
            bgcolor="#BB77F9",
            inactive_color=ft.colors.WHITE,
            active_color=ft.colors.BLACK,
            on_change=lambda e: self.change_page(e, self.page),
            destinations=[
                ft.NavigationDestination(icon=ft.icons.ADD_CIRCLE_OUTLINE, label="Add workout"),
                ft.NavigationDestination(icon=ft.icons.CALENDAR_TODAY, label="Calendar"),
                ft.NavigationDestination(icon=ft.icons.TRENDING_UP_ROUNDED, label="progress"),
            ]
        )

        # def check_item_clicked(e):
        #     e.control.checked = not e.control.checked
        #     self.page.update()

        self.page.appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.PALETTE),
            leading_width=40,
            title=ft.Text("START THE ACTION"),
            center_title=True,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(ft.icons.HOME, on_click=self.handle_home_click),
                ft.IconButton(ft.icons.FILTER_3),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Item 1"),
                        ft.PopupMenuItem(),  # divider
                        # ft.PopupMenuItem(
                        #     text="Checked item", checked=False, on_click=check_item_clicked
                        # ),
                    ]
                ),
            ],
        )

        self.handle_home_click()

    # ft.app(target=main)


def main() -> None:
    ft.app(target=MenuApp.main)


if __name__ == "__main__":
    main()

