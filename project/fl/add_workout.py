from project.models import Set, Exercise, Workout
import json

import calendar
from datetime import datetime

import flet as ft
import calendar
from datetime import datetime
from project.client import Client


class AddWorkout:  # add workout
    def __init__(self, client: Client, date) -> None:
        self.page = None
        self.client = client

        self.date = datetime.strptime(date, "%B %d, %Y")

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
                # self.day,
                # self.month,
                # self.year,
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

        # day = int(self.day.value)
        # month = int(self.month.value)
        # year = int(self.year.value)
        #
        # date = datetime(year, month, day)

        date = self.date

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
        # self.power1 = ft.TextField(label="power", autofocus=True, border_color='#8532B8')

        self.power_text = ft.Text("the exercise is power-")
        self.power1 = ft.RadioGroup(content=ft.Column([
                        ft.Radio(value="True", label="Yes"),
                        ft.Radio(value="False", label="No")]))

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
                self.power_text,
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
    ft.app(target=Add_Exercise.main)


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
    ft.app(target=Add_Set.main)


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

            self.event = ft.TextField(read_only=True, border="none", color=ft.colors.BLACK)

            # self.event = ft.TextField(
            #     label="Date", read_only=True, value=" ", **CalendarApp.input_style(38)
            # )

            self.controls = [
                self.date,
                self.event,
                self.button1
            ]

        def go_to_app(self, e: ft.ControlEvent) -> None:
            # Function to navigate to App3 page
            if self.date.value != " ":
                self.page.clean()
                app3_instance = AddWorkout(client=self.client, date=self.date.value)
                app3_instance.main(self.page)
            else:
                self.event.value = "please select date"
                self.page.update()

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
