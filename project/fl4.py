import time

from models import Set, Exercise, Workout
import json

import calendar
from datetime import datetime

import flet as ft
import calendar
from datetime import datetime
from client import Client


class AddWorkout:  # add workout
    def __init__(self, client: Client) -> None:
        self.page = None
        self.client = client

        self.text1 = ft.Text("add workout:", size=35, color='#8532B8', weight=ft.FontWeight.W_500, selectable=True,
                             font_family="Elephant")
        # self.userid1 = ft.TextField(label="userid", autofocus=True, border_color='#8532B8')

        self.workout_name = ft.TextField(label="name of workout", autofocus=True, border_color='#8532B8')

        self.day = ft.TextField(label="day", autofocus=True, border_color='#8532B8')
        self.month = ft.TextField(label="month", autofocus=True, border_color='#8532B8')
        self.year = ft.TextField(label="year", autofocus=True, border_color='#8532B8')

        self.button1 = ft.ElevatedButton(text="add exercise", on_click=self.go_to_add_exercise, bgcolor='#8532B8',
                                         color='white')
        self.massage2 = ft.TextField(read_only=True, border="none", color='#A8468C')

        # self.exerciselist = ft.Text("add exercise:")
        # self.exer_name = ft.TextField(label="name of exercise", autofocus=True, border_color='#8532B8')
        # self.power1 = ft.TextField(label="power", autofocus=True, border_color='#8532B8')
        # # self.sets1 = ft.TextField(label="sets", autofocus=True, border_color='#8532B8')
        #
        # self.setsM = ft.Text("add set:")
        # self.repetitionsS1 = ft.TextField(label="repetitions", autofocus=True, border_color='#8532B8')
        # self.timeS1 = ft.TextField(label="time", autofocus=True, border_color='#8532B8')
        # self.weightS1 = ft.TextField(label="weight", autofocus=True, border_color='#8532B8')
        # self.distance_KMS1 = ft.TextField(label="distance_KM", autofocus=True, border_color='#8532B8')
        #
        # self.button1 = ft.ElevatedButton(text="add", on_click=self.click1, bgcolor='#8532B8', color='white')
        # self.massage1 = ft.TextField(read_only=True, border="none", color='#A8468C')
        # self.massage2 = ft.TextField(read_only=True, border="none", color='#A8468C')

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
                # self.exerciselist,
                # self.exer_name,
                # self.power1,
                # # self.sets1,
                # self.setsM,
                # self.repetitionsS1,
                # self.timeS1,
                # self.weightS1,
                # self.distance_KMS1,
                # self.button1,
                # self.massage2,
                # self.massage1
            ],
            # scroll=ft.ScrollMode.ALWAYS,
            # height=800
        )

    def go_to_add_exercise(self, e: ft.ControlEvent) -> None:
        # save part of the informarion of the workout
        userid1 = self.client.username

        workout_name = self.workout_name.value

        day = int(self.day.value)
        month = int(self.month.value)
        year = int(self.year.value)

        date = datetime(year, month, day)

        response2 = self.client.addworkout(userid=userid1, workout_name=workout_name, date=date, exerciselist="")
        self.massage2.value = response2["response"]

        d1 = date.strftime('%Y-%m-%d')
        workout = Workout(d1, workout_name, [])
        workout11 = json.dumps(workout.dump())

        self.page.clean()
        app_instance = Add_Exercise(client=self.client, workout=workout11)
        app_instance.main(self.page)

    def main(self, page: ft.Page) -> None:
        self.page = page
        self.page.scroll = ft.ScrollMode.ALWAYS

        row_container = ft.Row([self.main_panel_workout])
        self.page.add(row_container)
        self.page.update()


def main() -> None:
    ft.app(target=AddWorkout.main)


if __name__ == "__main__":
    main()


class Add_Exercise:
    def __init__(self, client: Client, workout: str) -> None:
        self.page = None
        self.client = client
        self.workout11 = workout
        self.workout = json.loads(workout)
        self.date = self.workout["date"]
        self.workout_name = self.workout["workout_name"]

        self.text1 = ft.Text("add the exercise:")
        self.name1 = ft.TextField(label="name", autofocus=True, border_color='#8532B8')
        self.power1 = ft.TextField(label="power", autofocus=True, border_color='#8532B8')

        self.text2 = ft.Text("add a set:")
        self.repetitionsS1 = ft.TextField(label="repetitions", autofocus=True, border_color='#8532B8')
        self.timeS1 = ft.TextField(label="time", autofocus=True, border_color='#8532B8')
        self.weightS1 = ft.TextField(label="weight", autofocus=True, border_color='#8532B8')
        self.distance_KMS1 = ft.TextField(label="distance_KM", autofocus=True, border_color='#8532B8')

        self.button4 = ft.ElevatedButton(text="add the exercise to workout", on_click=self.click, bgcolor='#8532B8',
                                         color='white')
        self.addexerciseM = ft.TextField(read_only=True, border="none", color='#A8468C')

        self.addexercise = ft.Column(
            [
                self.text1,
                self.name1,
                self.power1,
                self.text2,
                self.repetitionsS1,
                self.timeS1,
                self.weightS1,
                self.distance_KMS1,
                self.button4,
                self.addexerciseM
            ]
        )

    def click(self, e: ft.ControlEvent):
        userid1 = self.client.username
        date = self.date
        workout_name = self.workout_name

        name1 = self.name1.value
        power1 = self.power1.value

        repetitionsS1 = self.repetitionsS1.value
        timeS1 = self.timeS1.value
        weightS1 = self.weightS1.value
        distance_KMS1 = self.distance_KMS1.value

        sets2 = Set(repetitions=repetitionsS1, time=timeS1, weight=weightS1, distance_KM=distance_KMS1)
        print("*********///////*********")
        print(json.dumps(sets2.dump()))

        exerlst = Exercise(name=name1, power=power1, sets=[sets2])
        exerlst = json.dumps(exerlst.dump())
        print("ok2")
        response2 = self.client.addexercisetoworkout(userid=userid1, date=date, workout_name=workout_name,
                                                     exercise=exerlst)
        print("ok3")
        self.addexerciseM.value = response2["response"]
        print("worked")
        self.page.update()

        self.page.clean()
        app_instance = Add_Set(client=self.client, workout=self.workout11, execrise=exerlst)
        app_instance.main(self.page)

    def main(self, page: ft.Page) -> None:
        self.page = page
        self.page.scroll = ft.ScrollMode.ALWAYS

        row_container = ft.Row([self.addexercise])
        row_container.main_alignment = ft.MainAxisAlignment.CENTER

        row_container.width = 920
        self.page.add(row_container)

        self.page.horizontal_alignment = 'CENTER'
        self.page.vertical_alignment = 'CENTER'

        self.page.update()


def main() -> None:
    ft.app(target=Profile_Page.main)


if __name__ == "__main__":
    main()


class Add_Set:
    def __init__(self, client: Client, workout: str, execrise: str) -> None:
        self.page = None
        self.client = client

        self.workout = json.loads(workout)
        self.workout_name = self.workout["workout_name"]
        self.date = self.workout["date"]
        self.exec_list = execrise

        self.text2 = ft.Text("add a set:")
        self.repetitionsS1 = ft.TextField(label="repetitions", autofocus=True, border_color='#8532B8')
        self.timeS1 = ft.TextField(label="time", autofocus=True, border_color='#8532B8')
        self.weightS1 = ft.TextField(label="weight", autofocus=True, border_color='#8532B8')
        self.distance_KMS1 = ft.TextField(label="distance_KM", autofocus=True, border_color='#8532B8')

        self.button4 = ft.ElevatedButton(text="add the set to exercise", on_click=self.click, bgcolor='#8532B8',
                                         color='white')

        self.addsetM = ft.TextField(read_only=True, border="none", color='#A8468C')

        self.addset = ft.Column(
            [
                self.text2,
                self.repetitionsS1,
                self.timeS1,
                self.weightS1,
                self.distance_KMS1,
                self.button4,
                self.addsetM
            ]
        )

    def click(self, e: ft.ControlEvent):
        userid = self.client.username

        repetitionsS1 = self.repetitionsS1.value
        timeS1 = self.timeS1.value
        weightS1 = self.weightS1.value
        distance_KMS1 = self.distance_KMS1.value

        sets2 = Set(repetitions=repetitionsS1, time=timeS1, weight=weightS1, distance_KM=distance_KMS1)
        print("*********///////*********")
        print(json.dumps(sets2.dump()))

        response = self.client.addsettoexercise(userid=userid, date=self.date, workout_name=self.workout_name,
                                                exercise=self.exec_list, sets=json.dumps(sets2.dump()))

        print(response)
        self.addsetM.value = response["response"]
        # self.massage3.value = response.get("response", "Default Value")
        self.page.update()

    def main(self, page: ft.Page) -> None:
        self.page = page
        self.page.scroll = ft.ScrollMode.ALWAYS

        row_container = ft.Row([self.addset])
        row_container.main_alignment = ft.MainAxisAlignment.CENTER

        row_container.width = 920
        self.page.add(row_container)

        self.page.horizontal_alignment = 'CENTER'
        self.page.vertical_alignment = 'CENTER'

        self.page.update()


def main() -> None:
    ft.app(target=Profile_Page.main)


if __name__ == "__main__":
    main()


class CalendarApp:
    cal = calendar.Calendar()

    def __init__(self, client: Client):
        self.client = client
        self.cal = calendar.Calendar()
        # self.fixed_date = datetime.now().date()

        self.date_class = {
            6: "Sunday",
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday"
        }

        self.month_class = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }

    class Settings:
        year = datetime.now().year
        month = datetime.now().month

        @staticmethod
        def get_year():
            return CalendarApp.Settings.year

        @staticmethod
        def get_month():
            return CalendarApp.Settings.month

        @staticmethod
        def get_date(delta: int):
            if delta == 1:
                if CalendarApp.Settings.month + delta > 12:
                    CalendarApp.Settings.month = 1
                    CalendarApp.Settings.year += 1
                else:
                    CalendarApp.Settings.month += 1

            if delta == -1:
                if CalendarApp.Settings.month + delta < 1:
                    CalendarApp.Settings.month = 12
                    CalendarApp.Settings.year -= 1
                else:
                    CalendarApp.Settings.month -= 1

    date_box_style = {
        "width": 75, "height": 30, "alignment": ft.alignment.center, "shape": ft.BoxShape("rectangle"),
        "animate": ft.Animation(400, "ease"), "border_radius": 5
    }

    class DateBox(ft.Container):
        def __init__(
                self,
                day: int,
                event: bool = False,
                date: str = None,
                date_instnace: ft.Column = None,
                task_instnace: ft.Column = None,
                opacity: float | int = None,
        ) -> None:
            super(CalendarApp.DateBox, self).__init__(
                **CalendarApp.date_box_style,
                data=date,
                opacity=opacity,
                on_click=self.selected,
            )

            self.day: int = day
            self.event = event
            self.date_instnace = date_instnace
            self.task_instnace = task_instnace

            if self.event == False:
                self.content = ft.Text(self.day, text_align="center")
            else:
                self.content = ft.Text(f"{self.day} \n**", text_align="center")

        def selected(self, e: ft.TapEvent):
            if self.date_instnace:
                for row in self.date_instnace.controls[1:]:
                    for date in row.controls:

                        if date.border is not None:
                            date.border(
                                ft.border.all(0.5, "4fadf9")
                                if date == e.control else None
                            )
                        date.bgcolor = "#20303e" if date == e.control else None

                        if date == e.control:
                            self.task_instnace.date.value = e.control.data

                            # # Check if the selected date is allowed to be changed
                            # if e.control.data != CalendarApp.fixed_date:
                            #     selected_date = e.control.data  # Assign the selected date to selected_date
                            # else:
                            #     # If the selected date is fixed, do nothing
                            #     return

                self.date_instnace.update()
                self.task_instnace.update()

    class DateGrid(ft.Column):
        def __init__(self, year: int, month: int, task_instance: object, client: Client) -> None:

            super(CalendarApp.DateGrid, self).__init__()
            self.year = year
            self.month = month
            self.task_manager = task_instance
            self.client = client

            self.month_class = {
                1: "January",
                2: "February",
                3: "March",
                4: "April",
                5: "May",
                6: "June",
                7: "July",
                8: "August",
                9: "September",
                10: "October",
                11: "November",
                12: "December"
            }

            self.date = ft.Text(f"{self.month_class[self.month]} {self.year}")

            self.year_and_month = ft.Container(
                bgcolor="#20303e",
                border_radius=ft.border_radius.only(top_left=10, top_right=10),
                content=ft.Row(
                    alignment="center",
                    controls=[
                        ft.IconButton(
                            "chevron_left",
                            on_click=lambda e: self.update_date_grid(e, -1),
                        ),
                        ft.Container(
                            width=150, content=self.date,
                            alignment=ft.alignment.center
                        ),
                        ft.IconButton(
                            "chevron_right",
                            on_click=lambda e: self.update_date_grid(e, 1),
                        ),
                    ]
                )
            )

            self.controls.insert(1, self.year_and_month)

            date_class = {
                6: "Sunday",
                0: "Monday",
                1: "Tuesday",
                2: "Wednesday",
                3: "Thursday",
                4: "Friday",
                5: "Saturday"
            }

            week_days = ft.Row(
                alignment="spaceEvenly",
                controls=[
                    CalendarApp.DateBox(
                        day=date_class[index], opacity=0.7
                    )
                    for index in range(7)
                ]
            )

            self.controls.insert(1, week_days)
            self.populate_date_grid(self.year, self.month, client=self.client)

        def populate_date_grid(self, year: int, month: int, client: Client) -> None:
            self.client = client
            del self.controls[2:]

            weeks = CalendarApp.cal.monthdayscalendar(year, month)
            event = False
            for week in weeks:
                row = ft.Row(alignment="spaceEvenly")
                for day in week:
                    if day != 0:
                        event = False
                        for index in range(len(self.client.user_workout_lst)):
                            if day == int(self.client.user_workout_lst[index][3].strftime("%d")):
                                print(self.client.user_workout_lst[index][3].strftime("%d"))
                                if int(self.client.user_workout_lst[index][3].strftime("%m")) == month:
                                    print(self.client.user_workout_lst[index][3].strftime("%m"))
                                    if int(self.client.user_workout_lst[index][3].strftime("%Y")) == year:
                                        print(self.client.user_workout_lst[index][3].strftime("%Y"))
                                        event = True
                                        # row.controls.clear()
                                        # row.controls.append(CalendarApp.DateBox("**"))

                        row.controls.append(
                            CalendarApp.DateBox(
                                day, event, self.format_date(day), self,
                                self.task_manager,
                            )
                        )

                    else:
                        row.controls.append(CalendarApp.DateBox(" "))

                    # for index in range(len(self.client.user_workout_lst)):
                    #     if day == int(self.client.user_workout_lst[index][2].strftime("%d")):
                    #         print(self.client.user_workout_lst[index][2].strftime("%d"))
                    #         if int(self.client.user_workout_lst[index][2].strftime("%m")) == month:
                    #             print(self.client.user_workout_lst[index][2].strftime("%m"))
                    #             if int(self.client.user_workout_lst[index][2].strftime("%Y")) == year:
                    #                 print(self.client.user_workout_lst[index][2].strftime("%Y"))
                    #                 # row.controls.clear()
                    #                 row.controls.append(CalendarApp.DateBox("**"))

                self.controls.append(row)

        def update_date_grid(self, e: ft.TapEvent, delta: int):
            CalendarApp.Settings.get_date(delta)

            self.update_year_and_month(
                CalendarApp.Settings.get_year(), CalendarApp.Settings.get_month()
            )

            self.populate_date_grid(
                CalendarApp.Settings.get_year(), CalendarApp.Settings.get_month(), self.client
            )

            self.update()

        def update_year_and_month(self, year: int, month: int):
            self.year = year
            self.month = month

            self.month_class = {
                1: "January",
                2: "February",
                3: "March",
                4: "April",
                5: "May",
                6: "June",
                7: "July",
                8: "August",
                9: "September",
                10: "October",
                11: "November",
                12: "December"
            }

            self.date.value = f"{self.month_class[self.month]} {self.year}"

        def format_date(self, day: int) -> str:

            self.month_class = {
                1: "January",
                2: "February",
                3: "March",
                4: "April",
                5: "May",
                6: "June",
                7: "July",
                8: "August",
                9: "September",
                10: "October",
                11: "November",
                12: "December"
            }

            return f"{self.month_class[self.month]} {day}, {self.year}"

    @staticmethod
    def input_style(height: int):
        return {
            "height": height,
            "focused_border_color": "blue",
            "border_radius": 5,
            "cursor_height": 16,
            "cursor_color": "white",
            "content_padding": 10,
            "border_width": 1.5,
            "text_size": 12,
        }

    class TaskManager(ft.Column):
        def __init__(self, client: Client) -> None:
            super(CalendarApp.TaskManager, self).__init__()
            self.client = client

            self.date = ft.TextField(
                label="Date", read_only=True, value=" ", **CalendarApp.input_style(38)
            )

            self.button1 = ft.ElevatedButton(text="add workout", on_click=self.go_to_app,
                                             bgcolor='#8532B8', color='white')

            self.event = ft.TextField(
                label="Date", read_only=True, value=" ", **CalendarApp.input_style(38)
            )

            self.controls = [
                self.date,
                self.event,
                self.button1
            ]

        def go_to_app(self, e: ft.ControlEvent) -> None:
            # Function to navigate to App3 page
            self.page.clean()
            app3_instance = AddWorkout(client=self.client)
            app3_instance.main(self.page)

    @staticmethod
    def main(page: ft.Page, client: Client):
        client1 = client
        # page.theme_mode = ft.ThemeMode.DARK
        page.bgcolor = "1f2128"

        task_manager = CalendarApp.TaskManager(client=client1)
        grid = CalendarApp.DateGrid(
            year=CalendarApp.Settings.get_year(),
            month=CalendarApp.Settings.get_month(),
            task_instance=task_manager,
            client=client1
        )

        page.add(
            ft.Container(
                height=350,
                border=ft.border.all(0.75, "#4fadf9"),
                border_radius=10,
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                content=grid,
            ),
            ft.Divider(color="transparent", height=20),
            task_manager,
        )

        page.update()


def main() -> None:
    ft.app(target=CalendarApp.main)


if __name__ == "__main__":
    main()


class App:  # login, signup, delete user

    def __init__(self, client: Client) -> None:
        self.page = None
        self.client = client

        # Create a button to navigate to App3 page
        self.button_to_app300 = ft.ElevatedButton(text="Go to App3", on_click=self.go_to_app3, bgcolor='#8532B8',
                                                  color='white')

        self.text1 = ft.Text("login", size=55, color='#8532B8', weight=ft.FontWeight.W_500, selectable=True,
                             font_family="Elephant")
        self.username1 = ft.TextField(label="User Name", autofocus=True, border_color='#8532B8')
        self.password1 = ft.TextField(label="Password", autofocus=True, password=True, can_reveal_password=True,
                                      border_color='#8532B8')
        self.button1 = ft.ElevatedButton(text="Login", on_click=self.click1, bgcolor='#8532B8', color='white')
        self.massageL1 = ft.TextField(read_only=True, border="none", color='#A8468C')

        self.main_panel_login = ft.Column(
            [
                self.text1,
                self.username1,
                self.password1,
                self.button1,
                self.massageL1
            ]
            # ,
            # scroll=ft.ScrollMode.ALWAYS,
            # height=1000
        )

        self.text2 = ft.Text("sign up", size=55, color='#8532B8', weight=ft.FontWeight.W_500, selectable=True,
                             font_family="Elephant")
        self.username2 = ft.TextField(label="User Name", autofocus=True, border_color='#8532B8')
        self.password2 = ft.TextField(label="Password", autofocus=True, password=True, can_reveal_password=True,
                                      border_color='#8532B8')
        self.button2 = ft.ElevatedButton(text="Sign Up", on_click=self.click2, bgcolor='#8532B8', color='white')
        self.massageS2 = ft.TextField(read_only=True, border="none", color='#A8468C')

        self.main_panel_signup = ft.Column(
            [
                self.text2,
                self.username2,
                self.password2,
                self.button2,
                self.massageS2
            ]
            # ,
            # scroll=ft.ScrollMode.ALWAYS,
            # height=100
        )

        self.main_panel_bottom = ft.Column(
            [
                self.button_to_app300
            ]
            # ,
            # scroll=ft.ScrollMode.ALWAYS,
            # height=100
        )

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

    def go_to_app3(self, e: ft.ControlEvent) -> None:
        # Function to navigate to App3 page
        self.page.clean()
        app3_instance = AddWorkout(self.client)
        app3_instance.main(self.page)

    # to authenticate
    def click1(self, e: ft.ControlEvent) -> None:
        username = self.username1.value
        password = self.password1.value

        # error massages
        self.username1.error_text = ""
        self.password1.error_text = ""

        # if the user put username and password
        if username and password:
            response = self.client.authenticate(username, password)
            self.massageL1.value = response["response"]
            if self.massageL1.value == "user authenticated":
                self.page.add(self.button_Next)
            self.page.update()

        # if the user put password and not username
        elif (not username) and password:
            self.username1.error_text = "Please enter your username"
            self.page.update()

        # if the user put username and not password
        elif (not password) and username:
            self.password1.error_text = "Please enter your password"
            self.page.update()

        # if the user not put username and password
        else:
            self.password1.error_text = "Please enter your password"
            self.username1.error_text = "Please enter your username"
            self.page.update()

    # to signup
    def click2(self, e: ft.ControlEvent) -> None:
        username = self.username2.value
        password = self.password2.value

        self.username2.error_text = ""
        self.password2.error_text = ""

        if username and password:
            response = self.client.signup(username, password)
            self.massageS2.value = response["response"]

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

    # to delete
    def click3(self, e: ft.ControlEvent) -> None:
        username = self.username3.value
        password = self.password3.value

        self.username3.error_text = ""
        self.password3.error_text = ""

        if username and password:
            response = self.client.delete(username, password)
            self.massageD3.value = response["response"]

            self.page.update()

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

        row_container = ft.Row([self.main_panel_login, self.main_panel_signup, self.main_panel_delete],
                               auto_scroll=True)
        row_container.main_alignment = ft.MainAxisAlignment.CENTER

        row_container.width = 920
        self.page.add(row_container)

        row_container2 = ft.Row([self.main_panel_bottom])
        row_container.width = 920
        self.page.add(row_container2)

        # self.page.add(self.main_panel_login, self.main_panel_signup)
        # self.page.add(self.main_panel_signup)

        self.page.horizontal_alignment = 'CENTER'
        self.page.vertical_alignment = 'CENTER'

        self.page.update()


def main() -> None:
    ft.app(target=App.main)


if __name__ == "__main__":
    main()


class App4:

    def __init__(self, client: Client) -> None:
        self.page = None
        self.client = client

        self.title1 = ft.Text("add set to exercise", size=20, color='#8532B8', weight=ft.FontWeight.W_500,
                              selectable=True,
                              font_family="Elephant")
        self.title2 = ft.Text("add exercise to workout", size=20, color='#8532B8', weight=ft.FontWeight.W_500,
                              selectable=True,
                              font_family="Elephant")
        # self.title3 = ft.Text("delete set from exercise", size=20, color='#8532B8', weight=ft.FontWeight.W_500, selectable=True,
        #                      font_family="Elephant")
        self.title4 = ft.Text("delete exercise from workout", size=20, color='#8532B8', weight=ft.FontWeight.W_500,
                              selectable=True,
                              font_family="Elephant")

        self.userid1 = ft.TextField(label="userid", autofocus=True, border_color='#8532B8')
        self.date = ft.TextField(label="date", autofocus=True, border_color='#8532B8')

        self.text1 = ft.Text("add the exercise:")
        self.name1 = ft.TextField(label="name", autofocus=True, border_color='#8532B8')
        self.power1 = ft.TextField(label="power", autofocus=True, border_color='#8532B8')
        # self.sets1 = ft.TextField(label="sets", autofocus=True, border_color='#8532B8')

        self.text2 = ft.Text("add the set:")
        self.repetitionsS1 = ft.TextField(label="repetitions", autofocus=True, border_color='#8532B8')
        self.timeS1 = ft.TextField(label="time", autofocus=True, border_color='#8532B8')
        self.weightS1 = ft.TextField(label="weight", autofocus=True, border_color='#8532B8')
        self.distance_KMS1 = ft.TextField(label="distance_KM", autofocus=True, border_color='#8532B8')

        # self.button1 = ft.ElevatedButton(text="delete the set", on_click=self.click1_addexercise(), bgcolor='#8532B8', color='white')
        # self.button3 = ft.ElevatedButton(text="add set to exercise", on_click=self.click3_add_set_to_exercise, bgcolor='#8532B8', color='white')
        self.button4 = ft.ElevatedButton(text="add exercise to workout", on_click=self.click4_add_exercise_to_workout,
                                         bgcolor='#8532B8', color='white')
        # self.button5 = ft.ElevatedButton(text="delete set from exercise", on_click=self.click5_delete_set_from_exercise, bgcolor='#8532B8', color='white')
        self.button6 = ft.ElevatedButton(text="delete exercise from workout",
                                         on_click=self.click6_delete_exercise_from_workout, bgcolor='#8532B8',
                                         color='white')

        # self.addsetM = ft.TextField(read_only=True, border="none", color='#A8468C')
        # self.deletesetM = ft.TextField(read_only=True, border="none", color='#A8468C')
        self.addexerciseM = ft.TextField(read_only=True, border="none", color='#A8468C')
        self.deleteexerciseM = ft.TextField(read_only=True, border="none", color='#A8468C')

        self.addset = ft.Column(
            [
                self.title1,
                self.text2,
                self.repetitionsS1,
                self.timeS1,
                self.weightS1,
                self.distance_KMS1,
                # self.button3,
                # self.addsetM,
            ]
        )

        # self.deleteset = ft.Column(
        #     [
        #         self.title3,
        #         self.text2,
        #         self.repetitionsS1,
        #         self.timeS1,
        #         self.weightS1,
        #         self.distance_KMS1,
        #         self.button5,
        #         self.deletesetM
        #     ]
        # )

        self.addexercise = ft.Column(
            [
                self.title2,
                self.text1,
                self.name1,
                self.power1,
                self.text2,
                self.repetitionsS1,
                self.timeS1,
                self.weightS1,
                self.distance_KMS1,
                self.button4,
                self.addexerciseM
            ]
        )

        self.deleteexercise = ft.Column(
            [
                self.title4,
                self.text1,
                self.name1,
                self.power1,
                self.text2,
                self.repetitionsS1,
                self.timeS1,
                self.weightS1,
                self.distance_KMS1,
                self.button6,
                self.deleteexerciseM
            ]
        )

    # to add new column of set in page
    def click2(self, e: ft.ControlEvent):
        row_container = ft.Row([self.addset])
        self.page.add(row_container)
        self.page.update()

    # to add a set to exercise by name
    # need to change to add by the currnet name and current exercise id
    # def click3_add_set_to_exercise(self, e: ft.ControlEvent):
    #
    #     repetitionsS1 = self.repetitionsS1.value
    #     timeS1 = self.timeS1.value
    #     weightS1 = self.weightS1.value
    #     distance_KMS1 = self.distance_KMS1.value
    #
    #     sets2 = Set(repetitions=repetitionsS1, time=timeS1, weight=weightS1, distance_KM=distance_KMS1)
    #     print("*********///////*********")
    #     print(json.dumps(sets2.dump()))
    #
    #     response = client4.addsettoexercise("nofar", json.dumps(sets2.dump()))
    #     print(response)
    #     self.addsetM.value = response["response"]
    #     # self.massage3.value = response.get("response", "Default Value")
    #     self.page.update()
    #
    # # to add a exercise to workout by name
    # # need to change to add by the currnet name and current workout id
    def click4_add_exercise_to_workout(self, e: ft.ControlEvent):
        userid1 = self.userid1.value
        date = self.date.value

        name1 = self.name1.value
        power1 = self.power1.value

        repetitionsS1 = self.repetitionsS1.value
        timeS1 = self.timeS1.value
        weightS1 = self.weightS1.value
        distance_KMS1 = self.distance_KMS1.value

        sets2 = Set(repetitions=repetitionsS1, time=timeS1, weight=weightS1, distance_KM=distance_KMS1)
        print("*********///////*********")
        print(json.dumps(sets2.dump()))

        exerlst = Exercise(name=name1, power=power1, sets=[sets2])
        exerlst = json.dumps(exerlst.dump())
        print("ok2")
        response2 = self.client.addexercisetoworkout("hadar7", exerlst)
        print("ok3")
        self.addexerciseM.value = response2["response"]
        print("worked")
        self.page.update()

    # to delete a set to exercise by name
    # need to change to add by the currnet name and current exercise id
    # def click5_delete_set_from_exercise(self, e: ft.ControlEvent):
    #     repetitionsS1 = self.repetitionsS1.value
    #     timeS1 = self.timeS1.value
    #     weightS1 = self.weightS1.value
    #     distance_KMS1 = self.distance_KMS1.value
    #
    #     sets2 = Set(repetitions=repetitionsS1, time=timeS1, weight=weightS1, distance_KM=distance_KMS1)
    #     print("*********///////*********")
    #     print(json.dumps(sets2.dump()))
    #
    #     response = client4.deletesetfromexercise("nofar", json.dumps(sets2.dump()))
    #     print(response)
    #     self.deletesetM.value = response["response"]
    #     # self.massage3.value = response.get("response", "Default Value")
    #     self.page.update()

    # to delete a exercise to workout by name
    # need to change to add by the currnet name and current workout id
    def click6_delete_exercise_from_workout(self, e: ft.ControlEvent):
        userid1 = self.userid1.value
        date = self.date.value

        name1 = self.name1.value
        power1 = self.power1.value

        repetitionsS1 = self.repetitionsS1.value
        timeS1 = self.timeS1.value
        weightS1 = self.weightS1.value
        distance_KMS1 = self.distance_KMS1.value

        sets2 = Set(repetitions=repetitionsS1, time=timeS1, weight=weightS1, distance_KM=distance_KMS1)
        print("*********///////*********")
        print(json.dumps(sets2.dump()))

        exerlst = Exercise(name=name1, power=power1, sets=[sets2])
        exerlst = json.dumps(exerlst.dump())
        print("ok2")
        response2 = self.client.deletexercisefromworkout("nofar", exerlst)
        print("ok3")
        self.deleteexerciseM.value = response2["response"]
        print("worked")
        self.page.update()

    def main(self, page: ft.Page) -> None:
        self.page = page
        self.page.scroll = ft.ScrollMode.ALWAYS

        # row_container = ft.Row([self.addexercise, self.deleteexercise, self.addset, self.deleteset])
        row_container = ft.Row([self.addexercise, self.deleteexercise])
        self.page.add(row_container)
        self.page.update()


def main() -> None:
    ft.app(target=App4().main)


if __name__ == "__main__":
    main()


class App5:  # show improvement
    def __init__(self, client: Client) -> None:
        self.page = None
        self.client = client

        self.text1 = ft.Text("show improvement", size=55, color='#8532B8', weight=ft.FontWeight.W_500,
                             selectable=True, font_family="Elephant")
        self.username1 = ft.TextField(label="User Name", autofocus=True, border_color='#8532B8')
        self.exercise_name = ft.TextField(label="exercise name", autofocus=True, border_color='#8532B8')
        # self.dd = ft.Dropdown(
        #     width=100,
        #     options=[
        #         ft.dropdown.Option({i}) for i in self.client.user_exer_lst
        #     ],
        # )

        # controls = [
        #     ft.ListTile(title=ft.Text(f"Color {i}"), on_click=close_anchor, data=i)
        #     for i in range(10)
        # ],
        self.s_date = ft.Text("start date-", size=20, color='#8532B8')
        self.day1 = ft.TextField(label="day", autofocus=True, border_color='#8532B8')
        self.month1 = ft.TextField(label="month", autofocus=True, border_color='#8532B8')
        self.year1 = ft.TextField(label="year", autofocus=True, border_color='#8532B8')

        self.e_date = ft.Text("end date-", size=20, color='#8532B8')
        self.day2 = ft.TextField(label="day", autofocus=True, border_color='#8532B8')
        self.month2 = ft.TextField(label="month", autofocus=True, border_color='#8532B8')
        self.year2 = ft.TextField(label="year", autofocus=True, border_color='#8532B8')

        self.button1 = ft.ElevatedButton(text="send", on_click=self.click1, bgcolor='#8532B8', color='white')
        self.m1 = ft.Text("avg repete-", size=20, color='#8532B8')
        self.m2 = ft.Text("avg time-", size=20, color='#8532B8')
        self.m3 = ft.Text("avg weight-", size=20, color='#8532B8')
        self.m4 = ft.Text("avg distance KM-", size=20, color='#8532B8')
        self.avgrepete = ft.TextField(read_only=True, border="none", color='#A8468C')
        self.avgtime = ft.TextField(read_only=True, border="none", color='#A8468C')
        self.avgweight = ft.TextField(read_only=True, border="none", color='#A8468C')
        self.avgdistance_KM = ft.TextField(read_only=True, border="none", color='#A8468C')

        self.show_improvement_panel = ft.Column(
            [
                self.text1,
                # self.username1,
                self.exercise_name,
                # self.dd,
                self.s_date,
                self.day1,
                self.month1,
                self.year1,
                self.e_date,
                self.day2,
                self.month2,
                self.year2,
                self.button1,
                self.m1,
                self.avgrepete,
                self.m2,
                self.avgtime,
                self.m3,
                self.avgweight,
                self.m4,
                self.avgdistance_KM
            ]
        )

    # to show improvement
    def click1(self, e: ft.ControlEvent) -> None:
        username = self.client.username
        exercise_name = self.exercise_name.value

        day1 = int(self.day1.value)
        month1 = int(self.month1.value)
        year1 = int(self.year1.value)
        s_date = datetime(year1, month1, day1)

        day2 = int(self.day2.value)
        month2 = int(self.month2.value)
        year2 = int(self.year2.value)
        e_date = datetime(year2, month2, day2)

        response = self.client.showimprovement(username, exercise_name, s_date, e_date)
        self.avgrepete.value = response["repete"]
        self.avgtime.value = response["time"]
        self.avgweight.value = response["weight"]
        self.avgdistance_KM.value = response["distance_KM"]
        self.page.update()

    def main(self, page: ft.Page) -> None:
        self.page = page
        self.page.scroll = ft.ScrollMode.ALWAYS

        row_container = ft.Row([self.show_improvement_panel])
        row_container.main_alignment = ft.MainAxisAlignment.CENTER

        row_container.width = 920
        self.page.add(row_container)

        self.page.horizontal_alignment = 'CENTER'
        self.page.vertical_alignment = 'CENTER'

        self.page.update()


def main() -> None:
    ft.app(target=App5.main)


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
    ft.app(target=HomePage().main)


if __name__ == "__main__":
    main()


class Profile_Page:
    def __init__(self, client: Client) -> None:
        self.page = None
        self.client = client

        self.text1 = ft.Text("Profile Page", size=55, color='#8532B8', weight=ft.FontWeight.W_500,
                             selectable=True, font_family="Elephant")

        self.m1 = ft.Text("name", size=20, color='#8532B8')
        self.m2 = ft.Text("user information", size=20, color='#8532B8')
        self.m3 = ft.Text("plan of workouts", size=20, color='#8532B8')

        self.profile_page_panel = ft.Column(
            [
                self.text1,
                self.m1,
                self.m2,
                self.m3
            ]
        )

    def main(self, page: ft.Page) -> None:
        self.page = page
        self.page.scroll = ft.ScrollMode.ALWAYS

        row_container = ft.Row([self.profile_page_panel])
        row_container.main_alignment = ft.MainAxisAlignment.CENTER

        row_container.width = 920
        self.page.add(row_container)

        self.page.horizontal_alignment = 'CENTER'
        self.page.vertical_alignment = 'CENTER'

        self.page.update()


def main() -> None:
    ft.app(target=Profile_Page.main)


if __name__ == "__main__":
    main()


class State:
    toggle = True


s = State()

class ShowImprove1:
    def __init__(self, client: Client) -> None:
        self.page = None
        self.client = client

        self.exercise_name = ft.TextField(label="exercise name", autofocus=True, border_color='#8532B8')
        self.s_date = ft.Text("start date-", size=20, color='#8532B8')
        self.day1 = ft.TextField(label="day", autofocus=True, border_color='#8532B8')
        self.month1 = ft.TextField(label="month", autofocus=True, border_color='#8532B8')
        self.year1 = ft.TextField(label="year", autofocus=True, border_color='#8532B8')

        self.e_date = ft.Text("end date-", size=20, color='#8532B8')
        self.day2 = ft.TextField(label="day", autofocus=True, border_color='#8532B8')
        self.month2 = ft.TextField(label="month", autofocus=True, border_color='#8532B8')
        self.year2 = ft.TextField(label="year", autofocus=True, border_color='#8532B8')
        self.button1 = ft.ElevatedButton(text="send", on_click=self.click1, bgcolor='#8532B8', color='white')

        self.show_improvement_panel = ft.Column(
            [
                self.exercise_name,
                self.s_date,
                self.day1,
                self.month1,
                self.year1,
                self.e_date,
                self.day2,
                self.month2,
                self.year2,
                self.button1
            ]
        )

    def click1(self, e: ft.ControlEvent) -> None:
        username = self.client.username
        self.workout_lst = self.client.user_workout_lst

        exercise_name = self.exercise_name.value

        day1 = int(self.day1.value)
        month1 = int(self.month1.value)
        year1 = int(self.year1.value)
        s_date = datetime(year1, month1, day1)

        day2 = int(self.day2.value)
        month2 = int(self.month2.value)
        year2 = int(self.year2.value)
        e_date = datetime(year2, month2, day2)

        response = self.client.improve_with_params(username, exercise_name, s_date, e_date)
        dates_l = response["dates"]
        count_sets_l = response["count_sets"]
        avgrepete_l = response["repetitions_avg"]
        avgtime_l = response["time_avg"]
        avgweight_l = response["weight_avg"]
        avgdistance_KM_l = response["distance_KM_avg"]

        self.page.clean()
        app_instance = Graphs1(client=self.client, exercise_name=exercise_name, s_date=s_date, e_date=e_date,
                               lst=avgrepete_l, date_lst=dates_l)
        app_instance.main(self.page)
        app_instance = Graphs1(client=self.client, exercise_name=exercise_name, s_date=s_date, e_date=e_date,
                               lst=avgrepete_l, date_lst=dates_l)
        app_instance.main(self.page)

    # def click2(self, e: ft.ControlEvent) -> None:
        # self.page.clean()
        # self.page.add(ft.Row([self.chart]))
        # self.page.update()

    def show(self, exercise_name, s_date, e_date, lst, date_lst):
        # new_lst = []
        # n = 0
        # for i in lst:
        #     new_lst.append(ft.LineChartDataPoint(i, date_lst[n]))
        #     n = n + 1
        #
        # data_1 = [
        #     ft.LineChartData(
        #         data_points=new_lst,
        #         stroke_width=5,
        #         color=ft.colors.CYAN,
        #         curved=True,
        #         stroke_cap_round=True,
        #     )
        # ]

        self.page.add(self.button, self.chart)
        self.page.update()


    def main(self, page: ft.Page):
        self.page = page
        self.page.scroll = ft.ScrollMode.ALWAYS

        row_container = ft.Row([self.show_improvement_panel])
        row_container.main_alignment = ft.MainAxisAlignment.CENTER

        row_container.width = 920
        self.page.add(row_container)

        self.page.horizontal_alignment = 'CENTER'
        self.page.vertical_alignment = 'CENTER'

        self.page.update()


def main() -> None:
    ft.app(target=ShowImprove1().main)


if __name__ == "__main__":
    main()


class Graphs1:
    def __init__(self, client: Client, exercise_name, s_date, e_date, lst, date_lst) -> None:
        self.page = None
        self.client = client
        self.exercise_name = exercise_name
        self.s_date = s_date
        self.e_date = e_date
        self.lst = lst
        self.date_lst = date_lst


        new_lst = []
        left_axis1 = []
        bottom_axis1 = []

        n = 0
        for i in lst:
            new_lst.append(ft.LineChartDataPoint(date_lst[n], i))
            left_axis1.append(ft.ChartAxisLabel(
                        value=date_lst[n],
                        label=ft.Text(i, size=14, weight=ft.FontWeight.BOLD),
                    ))

            bottom_axis1.append(ft.ChartAxisLabel(
                        value=date_lst[n],
                        label=ft.Container(
                            ft.Text(
                                i,
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ))

            n = n + 1

        self.data_1 = [
            ft.LineChartData(
                data_points=new_lst,
                stroke_width=5,
                color=ft.colors.CYAN,
                curved=True,
                stroke_cap_round=True,
            )
        ]

        self.chart = ft.LineChart(
            data_series=self.data_1,
            border=ft.border.all(3, ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE)),
            horizontal_grid_lines=ft.ChartGridLines(
                interval=1, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
            ),
            vertical_grid_lines=ft.ChartGridLines(
                interval=1, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
            ),
            left_axis=ft.ChartAxis(
                labels=left_axis1,
                labels_size=40,
            ),
            bottom_axis=ft.ChartAxis(
                labels=bottom_axis1,
                labels_size=32,
            ),
            tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
            # min_y=0,
            # max_y=6,
            # min_x=0,
            # max_x=11,
            # # animate=5000,
            # expand=True,
        )



    def main(self, page: ft.Page) -> None:
        self.page = page
        # self.page.scroll = ft.ScrollMode.ALWAYS

        self.page.add(ft.Row([self.chart]))

def main() -> None:
    ft.app(target=Graphs1().main)


if __name__ == "__main__":
    main()



