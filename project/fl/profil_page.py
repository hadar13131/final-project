import flet as ft
from project.models import Workout, Exercise, Set
import calendar
from datetime import datetime
from project.client import Client


class Profile_Page:
    def __init__(self, client:Client) -> None:
        self.page = None
        self.client = client

        self.text1 = ft.Text("Profile Page", size=55, color='#8532B8', weight=ft.FontWeight.W_500,
                             selectable=True, font_family="Elephant")

        self.m1 = ft.Text("name", size=20, color='#8532B8')
        self.m2 = ft.Text("user information", size=20, color='#8532B8')
        self.m3 = ft.Text("YOUR WORKOUTS PLAN:", size=20, color='#8532B8')

        self.workout_table = self.return_workout_table()

        self.profile_page_panel = ft.Column(
            [
                self.text1,
                self.m1,
                self.m2,
                self.m3,
                self.workout_table
            ]
        )

        self.titel1 = ft.Text("PROFILE PAGE", size=30, color='#8532B8', weight=ft.FontWeight.W_500,
                                selectable=True, font_family="Elephant", text_align=ft.alignment.center)

        self.count_workouts = ft.Column(

            controls=[
                ft.Column([
                    ft.Text("WORKOUT COUNTER", size=30, color='#8532B8', weight=ft.FontWeight.W_500,
                            selectable=True, font_family="Elephant", text_align=ft.alignment.center)
                ]),

            ft.Container(

                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor='#CC99FF',
                    border_radius=360,
                    content=ft.Column(
                        [
                            ft.Row([
                                ft.Text("YOU DID- " + str(len(self.client.user_workout_lst)) + " workouts", size=20, color='#8532B8',
                                        weight=ft.FontWeight.W_500,
                                        selectable=True, font_family="Arial Rounded MT Bold"),
                            ])
                        ]
                    )
                )]
        )


        self.table1 = ft.Column(
            # width=600,
            controls=[
                ft.Container(
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor='#CC99FF',
                    content=ft.Column(
                        [
                            ft.Row([
                                ft.Text("YOUR WORKOUTS PLAN:", size=20, color='#8532B8',
                                        weight=ft.FontWeight.W_500,
                                        selectable=True, font_family="Arial Rounded MT Bold"),
                            ]),

                            ft.Row([
                                self.workout_table,
                                ft.ElevatedButton(text="change details", on_click=self.change_your_info,
                                                  bgcolor='#8532B8',
                                                  color='white'),
                            ]),

                        ]
                    )
                ),

                ft.Column([]),

                # ft.Row(
                #     controls=[
                #         chart1
                #     ],
                # )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

    def change_your_info(self):
        ...

    def return_workout_table(self):

        # the values is the place in the database.
        date_lst = [] #value = 3
        name_lst = [] #value = 2
        workoutinfo_lst = [] #value = 4

        date_lst = self.future_workouts_by_value(value=3)
        name_lst = self.future_workouts_by_value(value=2)
        workoutinfo_lst = self.future_workouts_by_value(value=4)

        row_lst = []

        for i in range(len(date_lst)):
            row_lst.append(
            ft.DataRow(
                on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                selected=True,
                cells=[
                    ft.DataCell(ft.Text(date_lst[i].strftime('%Y-%m-%d'))),
                    ft.DataCell(ft.Text(name_lst[i])),
                    ft.DataCell(ft.Text(workoutinfo_lst[i])),
                ],
            ))


        table1 = ft.DataTable(
            show_checkbox_column=True,

            columns=[
                ft.DataColumn(ft.Text("date")),
                ft.DataColumn(ft.Text("workout name")),
                ft.DataColumn(ft.Text("workout info"), numeric=True),
            ],
            rows=row_lst
        )

        return table1

    def future_workouts_by_value(self, value):
        workout_lst = self.client.user_workout_lst

        lst = []
        for i in workout_lst:
            if i[3] >= datetime.now():
                lst.append(i[value])

        return lst

    def main(self, page: ft.Page) -> None:
        self.page = page
        self.page.scroll = ft.ScrollMode.ALWAYS

        self.page.add(self.titel1)
        self.page.add(ft.Row([self.count_workouts]))

        self.page.add(ft.Column([self.table1]))

        # row_container = ft.Row([self.profile_page_panel])
        # row_container.main_alignment = ft.MainAxisAlignment.CENTER
        #
        # row_container.width = 920
        # self.page.add(row_container)
        #
        # self.page.horizontal_alignment = 'CENTER'
        # self.page.vertical_alignment = 'CENTER'

        self.page.update()


def main() -> None:
    ft.app(target=Profile_Page().main)


if __name__ == "__main__":
    main()