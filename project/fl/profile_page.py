import flet as ft
from project.models import Workout, Exercise, Set
import calendar
from datetime import datetime
from project.client import Client


class Profile_Page:

    def __init__(self, client:Client) -> None:
        self.page = None
        self.client = client

        self.text1 = ft.Text("YOUR Profile Page", size=55, color='#8532B8', weight=ft.FontWeight.W_500,
                             selectable=True, font_family="Elephant")

        self.workout_table = self.return_workout_table()

        self.button_show_info = ft.ElevatedButton(text="show details", on_click=self.show_your_info,
                                                  bgcolor='#8532B8', color='white')

        self.username1 = ft.TextField(label="user name", read_only=True, autofocus=True, border_color='#8532B8')
        self.first_name = ft.TextField(label="first name", autofocus=True, border_color='#8532B8')
        self.last_name = ft.TextField(label="last name", autofocus=True, border_color='#8532B8')
        self.phone_number = ft.TextField(label="phone number", autofocus=True, border_color='#8532B8')
        self.email = ft.TextField(label="email", read_only=True, autofocus=True, border_color='#8532B8')
        self.age = ft.TextField(label="age", autofocus=True, border_color='#8532B8')

        self.massageE = ft.TextField(read_only=True, border="none", color='#A8468C')

        # self.gender = ft.TextField(label="gender", autofocus=True, border_color='#8532B8')
        self.gender = ft.Dropdown(
            label="gender",
            hint_text="Choose your gender",
            options=[
                ft.dropdown.Option("Female"),
                ft.dropdown.Option("Male"),
                ft.dropdown.Option("Other"),
            ]
        )

        self.goals = ft.TextField(label="goals", autofocus=True, border_color='#8532B8')

        self.button1 = ft.ElevatedButton(text="change", on_click=self.change_your_info, bgcolor='#8532B8', color='white')

        self.info_page = ft.Column([
            self.username1,
            self.email,
            self.first_name,
            self.last_name,
            self.phone_number,
            self.age,
            self.gender,
            self.goals,
            self.button1,
            self.massageE
            ]
        )


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

            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

    def show_your_info(self, e: ft.ControlEvent) -> None:

        info1 = self.client.bring_info(self.client.username)

        self.username1.value = self.client.username
        self.email.value = info1["email"]
        self.first_name.value = info1["first_name"]
        self.last_name.value = info1["last_name"]
        self.phone_number.value = info1["phone_num"]
        self.age.value = info1["age"]
        self.gender.value = info1["gender"]
        self.goals.value = info1["goals"]

        self.page.clean()
        self.page.add(self.info_page)
        self.page.update()


    def change_your_info(self, e: ft.ControlEvent):
        username1 = self.client.username
        firstname = self.first_name.value
        lastname = self.last_name.value
        phone_number = self.phone_number.value
        email = self.email.value
        age = int(self.age.value)
        gender = self.gender.value
        goals = self.goals.value

        if firstname and lastname and phone_number and age and gender and goals:
            response = self.client.fill_info(name=username1, first_name=firstname, last_name=lastname,
                                             phone_num=phone_number, email=email, age=age, gender=gender, goals=goals)
            self.massageE.value = response["response"]

            if self.massageE.value == "the information added":
                self.massageE.value = "the information changed"
                # row = ft.Row([self.button_Next])
                # self.page.add(row)
                self.page.update()

        else:
            self.massageE.value = "please fill the all fields"
            self.page.update()


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

        self.page.add(self.text1)
        self.page.add(ft.Row([self.count_workouts]))
        self.page.add(self.button_show_info)

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
    ft.app(target=Profile_Page.main)


if __name__ == "__main__":
    main()


class HomePage:
    def __init__(self, client: Client) -> None:
        self.page = None
        self.client = client

        self.text1 = ft.Text("HomePage", size=55, color='#8532B8', weight=ft.FontWeight.W_500,
                             selectable=True, font_family="Elephant")

        self.m1 = ft.Text("count days", size=20, color='#8532B8')
        self.m2 = ft.Text("week plan", size=20, color='#8532B8')

        self.home_page_panel = ft.Column(
            [
                self.text1,
                self.m1,
                self.m2
            ]
        )

    def main(self, page: ft.Page) -> None:
        self.page = page
        self.page.scroll = ft.ScrollMode.ALWAYS

        row_container = ft.Row([self.home_page_panel])
        row_container.main_alignment = ft.MainAxisAlignment.CENTER

        row_container.width = 920
        self.page.add(row_container)

        self.page.horizontal_alignment = 'CENTER'
        self.page.vertical_alignment = 'CENTER'

        self.page.update()


def main() -> None:
    ft.app(target=HomePage.main)


if __name__ == "__main__":
    main()
