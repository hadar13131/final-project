import flet as ft
from client4 import Client

class Workout_info:
    def __init__(self, client: Client) -> None:
        self.page = None
        self.client = client

        self.workouts = self.client.user_workout_lst

        self.main_panel_workout = ft.Column(
            [
                self.text1,
                # self.userid1,
                self.workout_name,
                self.day,
                self.month,
                self.year,
                self.button1,
                self.massage2
            ]
        )
    def check_date(self, workouts, date):

        for i in workouts:
            d1 = i["date"].strftime('%Y-%m-%d')
            if date == d1:
                return True

        return False


def main(page: ft.Page):
    page.spacing = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = ft.padding.only(top=0)

    def handle_expansion_tile_change(e):
        page.show_snack_bar(
            ft.SnackBar(ft.Text(f"ExpansionTile was {'expanded' if e.data=='true' else 'collapsed'}"), duration=1000)
        )
        if e.control.trailing:
            e.control.trailing.name = (
                ft.icons.ARROW_DROP_DOWN
                if e.control.trailing.name == ft.icons.ARROW_DROP_DOWN_CIRCLE
                else ft.icons.ARROW_DROP_DOWN_CIRCLE
            )
            page.update()

    page.add(
        ft.ExpansionTile(
            title=ft.Text("ExpansionTile 3"),
            subtitle=ft.Text("Leading expansion arrow icon"),
            affinity=ft.TileAffinity.LEADING,
            initially_expanded=True,
            collapsed_text_color=ft.colors.BLUE,
            text_color=ft.colors.BLUE,
            controls=[
                ft.ListTile(title=ft.Text("This is sub-tile number 3")),
                ft.ListTile(title=ft.Text("This is sub-tile number 4")),
                ft.ListTile(title=ft.Text("This is sub-tile number 5")),
            ],
        ),
    )


ft.app(target=main)