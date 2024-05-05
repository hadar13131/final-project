import flet as ft
from client import Client

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


    lst = []
    f = 200
    n = ft.ListTile(title=ft.Text(f"This is sub-tile number 311111111 {str(f)} "))
    lst.append(n)
    n = ft.ListTile(title=ft.Text("This is sub-tile number 311111111"))
    lst.append(n)
    n = ft.ListTile(title=ft.Text("This is sub-tile number 311"))
    lst.append(n)


    hi = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Workout name- ", size=20, color=ft.colors.BLACK,
                                weight=ft.FontWeight.W_500, selectable=True, font_family="Elephant",
                                text_align=ft.alignment.center),

                        ft.Text("date- ", size=20, color=ft.colors.BLACK,
                                weight=ft.FontWeight.W_500, selectable=True, font_family="Elephant",
                                text_align=ft.alignment.center)
                    ]
                ),

                ft.ExpansionTile(
                    title=ft.Text("exercises-"),
                    subtitle=ft.Text("Leading expansion arrow icon"),
                    affinity=ft.TileAffinity.LEADING,
                    # initially_expanded=True,
                    collapsed_text_color=ft.colors.BLUE,
                    text_color=ft.colors.BLUE,
                    controls=[
                        ft.ExpansionTile(
                            title=ft.Text("exercise 1- "),
                            subtitle=ft.Text("Leading expansion arrow icon"),
                            affinity=ft.TileAffinity.LEADING,
                            # initially_expanded=True,
                            collapsed_text_color=ft.colors.BLUE,
                            text_color=ft.colors.BLUE,
                            controls=[
                                ft.ExpansionTile(
                                    title=ft.Text("exer info- "),
                                    subtitle=ft.Text("Leading expansion arrow icon"),
                                    affinity=ft.TileAffinity.LEADING,
                                    # initially_expanded=True,
                                    collapsed_text_color=ft.colors.BLUE,
                                    text_color=ft.colors.BLUE,
                                    controls=[
                                        ft.ListTile(title=ft.Text("This is sub-tile number 3")),
                                        ft.ListTile(title=ft.Text("This is sub-tile number 4")),
                                        ft.ListTile(title=ft.Text("This is sub-tile number 5")),
                                    ],
                                ),
                                ft.ExpansionTile(
                                    title=ft.Text("sets-"),
                                    subtitle=ft.Text("Leading expansion arrow icon"),
                                    affinity=ft.TileAffinity.LEADING,
                                    # initially_expanded=True,
                                    collapsed_text_color=ft.colors.BLUE,
                                    text_color=ft.colors.BLUE,
                                    controls=[
                                        ft.ListTile(title=ft.Text("This is sub-tile number 3")),
                                        ft.ListTile(title=ft.Text("This is sub-tile number 4")),
                                        ft.ListTile(title=ft.Text("This is sub-tile number 5")),
                                    ],
                                ),
                                ft.ListTile(title=ft.Text("This is sub-tile number 5")),
                            ],
                        ),
                        ft.ExpansionTile(
                            title=ft.Text("exercise 2- "),
                            subtitle=ft.Text("Leading expansion arrow icon"),
                            affinity=ft.TileAffinity.LEADING,
                            # initially_expanded=True,
                            collapsed_text_color=ft.colors.BLUE,
                            text_color=ft.colors.BLUE,
                            controls=[
                                ft.ExpansionTile(
                                    title=ft.Text("exer info- "),
                                    subtitle=ft.Text("Leading expansion arrow icon"),
                                    affinity=ft.TileAffinity.LEADING,
                                    # initially_expanded=True,
                                    collapsed_text_color=ft.colors.BLUE,
                                    text_color=ft.colors.BLUE,
                                    controls=lst,
                                ),
                                ft.ExpansionTile(
                                    title=ft.Text("sets-"),
                                    subtitle=ft.Text("Leading expansion arrow icon"),
                                    affinity=ft.TileAffinity.LEADING,
                                    # initially_expanded=True,
                                    collapsed_text_color=ft.colors.BLUE,
                                    text_color=ft.colors.BLUE,
                                    controls=[
                                        ft.ListTile(title=ft.Text("This is sub-tile number 3")),
                                        ft.ListTile(title=ft.Text("This is sub-tile number 4")),
                                        ft.ListTile(title=ft.Text("This is sub-tile number 5")),
                                    ],
                                ),
                                ft.ListTile(title=ft.Text("This is sub-tile number 5")),
                            ],
                        )

                    ],
                ),


            ]
        )

    )

    page.add(hi)



ft.app(target=main)