import flet as ft
from project.client import Client
from project.models import Set, Exercise
import json

import calendar
from datetime import datetime
import show_improvement
import add_workout
import profile_page

import login_signup
import deleteuser_signout

class MenuApp:
    def __init__(self, client: Client) -> None:
        self.page = None
        self.client = client

    def handel_signout_user(self, e=None):
        self.page.navigation_bar = None
        self.page.appbar = None
        self.page.clean()
        app_instance = deleteuser_signout.SignOutPage(self.client)
        app_instance.main(self.page)
        # row_container = ft.Row([app_instance.main_panel_delete])
        # self.page.add(row_container)
        # self.page.update()

    def handel_delete_user(self, e=None):
        self.page.navigation_bar = None
        self.page.appbar = None
        self.page.clean()
        app_instance = deleteuser_signout.DeleteUserPage(self.client)
        app_instance.main(self.page)
        # row_container = ft.Row([app_instance.main_panel_delete])
        # self.page.add(row_container)
        # self.page.update()

    def handle_home_click(self, e=None):
        self.show_home_page()

    def show_home_page(self):
        self.page.clean()
        app_instance = profile_page.HomePage(self.client)
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
            app_instance = profile_page.Profile_Page(client=self.client)
            app_instance.main(self.page)

        elif selected_index == 1: #calendar
            self.page.clean()
            app_instance = add_workout.CalendarApp(client=self.client)
            app_instance.main(self.page, self.client)

        elif selected_index == 2: #improvment
            self.page.clean()
            app_instance = show_improvement.ShowImproveGraps(client=self.client)
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
                ft.NavigationDestination(icon=ft.icons.PERSON_OUTLINE_ROUNDED, label="Profile Page"),
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
            title=ft.Text("START TO MOVE"),
            center_title=True,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(ft.icons.HOME, on_click=self.handle_home_click),
                ft.Text(""),
                ft.Text(datetime.now().strftime("%x")),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="delete my user", on_click=self.handel_delete_user),
                        ft.PopupMenuItem(),  # divider
                        ft.PopupMenuItem(text="sign out", on_click=self.handel_signout_user),
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

