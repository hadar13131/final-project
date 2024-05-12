from project.models import Set, Exercise, Workout
import json

import calendar
from datetime import datetime

import flet as ft
import calendar
from datetime import datetime
from project.client import Client

import project.check_errors as c_e

class AddFullWorkout:
    def __init__(self, client: Client, date):
        self.page = None
        self.client = client
        self.date = datetime.strptime(date, "%B %d, %Y")  # from string to datetime
        self.str_date = date


        self.workout_name = ft.TextField(label="name of workout", autofocus=True, border_color='#8532B8')

        self.add_workout_button = ft.ElevatedButton(text="continue", on_click=self.add_workout, bgcolor='#8532B8',
                                         color='white')


        self.massage2 = ft.TextField(read_only=True, border="none", color='#A8468C')


        self.first_panel = ft.Column([
            ft.Container(
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            content=ft.Row(
                controls=[
                    ft.Column(
                        [
                            ft.Text("ADD NEW WORKOUT-", size=55, color='#8532B8', weight=ft.FontWeight.W_500,
                                    selectable=True,
                                    font_family="Century Gothic"),
                            ft.Row(
                                [
                                    ft.Text("THE DATE IS- " + self.str_date, size=25, color='#0A54B6',
                                            weight=ft.FontWeight.W_500,
                                            selectable=True, font_family="Century Gothic"),
                                ]
                            )
                        ]
                    )
                ]
            )
        ),
            ft.Container(
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor='#CC99FF',
                border_radius=10,
                border=ft.border.all(3, '#8532B8'),
                content=ft.Row(
                    controls=[
                        ft.Column(
                            [

                                ft.Text("ADD THE NAME OF YOUR WORKOUT-", size=25, color='#8532B8',
                                        weight=ft.FontWeight.W_500,
                                        selectable=True,
                                        font_family="Century Gothic"),
                                self.workout_name,

                            ]
                        )
                    ]
                )
            ),
            ft.Container(
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                content=ft.Row(
                    controls=[
                        ft.Column(
                            [
                                ft.Text("CONTINUE TO ADD NEW EXERCISE-", size=35, color='#8532B8',
                                        weight=ft.FontWeight.W_500,
                                        selectable=True,
                                        font_family="Century Gothic"),
                                self.add_workout_button,
                                self.massage2
                            ]
                        )
                    ]
                )
            )
        ])

        self.delete_workout = ft.ElevatedButton(text="delete workout", on_click=self.delete_workout,
                                                 bgcolor='#8532B8', color='white')

        self.exercise_name = ft.TextField(label="exercise name", autofocus=True, border_color='#8532B8')
        self.power_text = ft.Text("the exercise is power-")
        self.power1 = ft.RadioGroup(content=ft.Row([
            ft.Radio(value="True", label="Yes"),
            ft.Radio(value="False", label="No")]))

        self.add_exercise_button = ft.ElevatedButton(text="add the exercise to workout",
                                                     on_click=self.add_exercise,
                                                     bgcolor='#8532B8', color='white')

        self.addexerciseM = ft.TextField(read_only=True, border="none", color='#A8468C')

        self.button_more_set = ft.ElevatedButton(text="add more set to exercise", on_click=self.show_set_format,
                                                 bgcolor='#8532B8', color='white')

        self.button_add_exercise = ft.ElevatedButton(text="add exercise", on_click=self.show_exercise_format,
                                                 bgcolor='#8532B8', color='white')

        self.exercise_info = ft.Row([ft.Container(
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor='#CC99FF',
            border_radius=10,
            border=ft.border.all(3, '#8532B8'),
            content=ft.Row(
                controls=[
                    ft.Column(
                        [
                            ft.Text("ADD NEW EXERCISE- ", size=30, color='#8532B8', weight=ft.FontWeight.W_500,
                                    selectable=True,
                                    font_family="Arial Rounded MT Bold"),
                            self.exercise_name,
                            ft.Text("THE EXERCISE IS POWER? ", size=20, color='#8532B8', weight=ft.FontWeight.W_500,
                                    selectable=True,
                                    font_family="Arial Rounded MT Bold"),
                            self.power1,
                            self.add_exercise_button,
                            self.addexerciseM
                        ]
                    )
                ]
            )
        )])



        self.text2 = ft.Text("add a set:")
        self.repetitionsS1 = ft.TextField(label="repetitions", autofocus=True, border_color='#8532B8')
        self.timeS1 = ft.TextField(label="time (minutes)", autofocus=True, border_color='#8532B8')
        self.weightS1 = ft.TextField(label="weight (Kg)", autofocus=True, border_color='#8532B8')
        self.distance_KMS1 = ft.TextField(label="distance (KM)", autofocus=True, border_color='#8532B8')

        self.add_set_button = ft.ElevatedButton(text="add the set to exercise", on_click=self.add_set, bgcolor='#8532B8',
                                               color='white')

        self.addsetM = ft.TextField(read_only=True, border="none", color='#A8468C')

        self.set_info1 = ft.Column([
            # self.button_more_set,
            ft.Text("ADD NEW SET- ", size=30, color='#8532B8', weight=ft.FontWeight.W_500, selectable=True,
                    font_family="Arial Rounded MT Bold"),
            self.repetitionsS1,
            self.timeS1,
            self.weightS1,
            self.distance_KMS1,
            self.add_set_button,
            self.addsetM
        ])

        self.set_info = ft.Row([ft.Container(
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor='#CC99FF',
            border_radius=10,
            border=ft.border.all(3, '#8532B8'),
            content=ft.Row(
                controls=[
                    ft.Column(
                        [
                            ft.Text("ADD NEW SET- ", size=30, color='#8532B8', weight=ft.FontWeight.W_500,
                                    selectable=True,
                                    font_family="Arial Rounded MT Bold"),
                            ft.Row([
                                self.repetitionsS1,
                                self.timeS1,
                            ]),
                            ft.Row([
                                self.weightS1,
                                self.distance_KMS1
                            ]),
                            self.add_set_button,
                            self.addsetM
                        ]
                    )
                ]
            )
        )])

    def delete_workout(self, e: ft.ControlEvent):
        response = self.client.deleteworkout(self.client.username, self.workout_name.value, self.date)
        self.page.clean()
        app_instance = CalendarApp(client=self.client)
        app_instance.main(self.page, self.client)

    def show_workout_details(self, workout_name, workout_date):

        self.workout_info = ft.Container(
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            content=ft.Row(
                controls=[
                    ft.Row(
                        [
                            ft.Column([
                                ft.Text("WORKOUT DETAILS ", size=35, color="#242F9C",
                                        weight=ft.FontWeight.W_500, selectable=True,
                                        font_family="Arial Rounded MT Bold",
                                        text_align=ft.alignment.center),

                                ft.Text("Workout name- " + workout_name, size=20, color="#0070C0",
                                        weight=ft.FontWeight.W_500, selectable=True,
                                        font_family="Arial Rounded MT Bold",
                                        text_align=ft.alignment.center),

                                ft.Text("Workout date- " + workout_date, size=20, color="#0070C0",
                                        weight=ft.FontWeight.W_500, selectable=True,
                                        font_family="Arial Rounded MT Bold",
                                        text_align=ft.alignment.center),

                                self.delete_workout

                                # ft.Column(self.show_exercise())
                            ])

                        ]
                    )
                ]
            )
        )

        return self.workout_info

    def add_workout(self, e: ft.ControlEvent):
        username = self.client.username
        workout_name = self.workout_name.value
        date = self.date

        if workout_name and date:
            if c_e.check_workoutname(self.client, workout_name, date):
                response = self.client.addworkout(userid=username, workout_name=workout_name, date=date, exerciselist="")
                self.massage2.value = response["response"]
                self.page.update()
                self.page.clean()

                row1 = self.show_workout_details(workout_name=workout_name, workout_date=self.str_date)
                self.page.add(row1)

                self.page.add(ft.Row([self.button_add_exercise]))

                self.fill_exercise()

                self.page.update()

            else:
                self.massage2.value = "this workout is exist, please choose other name"
                self.page.update()


        else:
            self.massage2.value = "please fill all the fields"
            self.page.update()

    def fill_exercise(self):
        self.page.add(ft.Row([self.exercise_info]))
        self.page.update()

    def show_exercise_format(self, e: ft.ControlEvent):
        self.page.clean()
        self.exercise_name.value = ""
        self.power1.value = ""
        self.addexerciseM.value = ""
        self.page.add(self.show_workout_details(workout_name=self.workout_name.value, workout_date=self.str_date))
        self.page.add(ft.Row([self.button_add_exercise]))
        self.page.add(ft.Row([self.exercise_info]))
        self.page.update()

    def add_exercise(self, e: ft.ControlEvent):
        username = self.client.username
        workout_name = self.workout_name.value
        date = self.date

        exercise_name = self.exercise_name.value
        power = self.power1.value

        if exercise_name and power:
            if c_e.check_exercisename(self.client, workout_name, date, exercise_name):
                self.exerlst = Exercise(name=exercise_name, power=power, sets=[])
                self.exerlst = json.dumps(self.exerlst.dump())

                response2 = self.client.addexercisetoworkout(userid=username, date=date, workout_name=workout_name,
                                                             exercise=self.exerlst)

                self.addexerciseM.value = response2["response"]
                self.page.clean()
                self.page.add(self.show_workout_details(workout_name=self.workout_name.value, workout_date=self.str_date))
                self.page.add(ft.Row([self.button_add_exercise]))
                self.page.add(ft.Row([self.exercise_info, self.set_info]))
                self.addsetM.value = ""
                self.page.update()

            else:
                self.addexerciseM.value = "the exercise exist, please choose other name"
                self.page.update()

        else:
            self.addexerciseM.value = "please fill all the fields"
            self.page.update()




    def add_set(self, e: ft.ControlEvent):
        username = self.client.username
        workout_name = self.workout_name.value
        date = self.date

        exercise_name = self.exercise_name.value
        power = self.power1.value

        repetitionsS1 = 0
        timeS1 = 0
        weightS1 = 0
        distance_KMS1 = 0

        repetitionsS1 = self.repetitionsS1.value
        timeS1 = self.timeS1.value
        weightS1 = self.weightS1.value
        distance_KMS1 = self.distance_KMS1.value

        if repetitionsS1 == "":
            repetitionsS1 = 0

        if timeS1 == "":
            timeS1 = 0

        if weightS1 == "":
            weightS1 = 0

        if distance_KMS1 == "":
            distance_KMS1 = 0

        if not c_e.str_is_int(repetitionsS1):
            self.addsetM.value = "the repetitions should be in full"
            self.page.update()

        elif not c_e.str_is_int(timeS1):
            self.addsetM.value = "the time should be in minutes"
            self.page.update()

        else:
            if (c_e.is_numeric(repetitionsS1) and c_e.is_numeric(timeS1) and c_e.is_numeric(weightS1)
                    and c_e.is_numeric(distance_KMS1)):
                sets2 = Set(repetitions=repetitionsS1, time=timeS1, weight=weightS1, distance_KM=distance_KMS1)

                response = self.client.addsettoexercise2(userid=username, date=str(self.date),
                                                         workout_name=self.workout_name.value,
                                                         exercise_name=self.exercise_name.value,
                                                         power=self.power1.value, sets=json.dumps(sets2.dump()))

                self.addsetM.value = response["response"]

                self.repetitionsS1.value = ""
                self.timeS1.value = ""
                self.weightS1.value = ""
                self.distance_KMS1.value = ""
                self.page.update()

            else:
                self.addsetM.value = "please enter only numbers!"
                self.page.update()


    def show_set_format(self, e: ft.ControlEvent):
        self.page.clean()
        self.repetitionsS1.value = ""
        self.timeS1.value = ""
        self.weightS1.value = ""
        self.distance_KMS1.value = ""
        self.addsetM.value = ""
        self.page.add(self.show_workout_details(workout_name=self.workout_name.value, workout_date=self.str_date))
        self.page.add(ft.Row([self.button_add_exercise]))
        self.page.add(ft.Row([self.exercise_info, self.set_info]))
        self.page.update()

    def main(self, page: ft.Page) -> None:
        self.page = page
        self.page.scroll = ft.ScrollMode.ALWAYS

        row_container = self.first_panel
        row_container.main_alignment = ft.MainAxisAlignment.CENTER

        row_container.width = 600
        self.page.add(row_container)

        self.page.horizontal_alignment = 'CENTER'
        self.page.vertical_alignment = 'CENTER'

        self.page.bgcolor = ft.colors.GREY_100
        # self.page.add(ft.Column([self.first_panel]))
        self.page.update()


def main() -> None:
    ft.app(target=AddFullWorkout.main)


if __name__ == "__main__":
    main()



class ShowTheWorkout:
    def __init__(self, client: Client, date) -> None:
        self.page = None
        self.client = client

        self.workout_lst = self.client.user_workout_lst
        self.date = datetime.strptime(date, "%B %d, %Y")

        self.workout_name = ft.TextField(label="name of workout", autofocus=True, border_color='#8532B8')
        self.massage = ft.TextField(read_only=True, border="none", color='#A8468C')

        self.button_show_delete_workout = ft.ElevatedButton(text="delete workout", on_click=self.show_delete_workout,
                                                            bgcolor='#8532B8', color='white')

        self.button_delete_workout = ft.ElevatedButton(text="delete", on_click=self.delete_workout, bgcolor='#8532B8',
                                                       color='white')

    def date_workout(self):
        lst = []
        for index in range(len(self.workout_lst)):
            date1 = datetime.strptime(self.workout_lst[index][3], '%Y-%m-%dT%H:%M:%S')
            if self.date == date1:
                lst.append(self.workout_lst[index])

        return lst

    def show_delete_workout(self, e: ft.ControlEvent):
        lst = self.date_workout()

        lst_name_workout_dropdown = []
        for i in lst:
            lst_name_workout_dropdown.append(ft.dropdown.Option(i[2]))

        self.lst_name_workout = ft.Dropdown(
                width=100,
                options=lst_name_workout_dropdown,
            )

        self.delete_fomat = ft.Column([
            ft.Text("choose workout to delete- ", size=35, color='#8532B8', weight=ft.FontWeight.W_500, selectable=True,
                    font_family="Elephant"),

            self.lst_name_workout,

            self.button_delete_workout
        ])

        self.page.clean()
        self.page.add(self.delete_fomat)
        self.page.update()


    def delete_workout(self, e: ft.ControlEvent):
        workout_name = self.lst_name_workout.value
        response = self.client.deleteworkout(self.client.username, workout_name, self.date)
        self.page.clean()
        self.calndar_format()

    def check1(self):
        lst = self.date_workout()

        if not lst:
            self.page.clean()
            self.massage.value = "there is no workout in this day"
            self.calndar_format()
            self.page.update()

        else:
            self.page.clean()
            final_lst = self.show_workout(lst)
            self.calndar_format()
            self.page.add(self.button_show_delete_workout)
            self.page.add(ft.Column(final_lst))
            self.page.update()
            # for i in final_lst:
            #     self.page.add(ft.Column([i]))
            #     self.page.update()

    def show_workout(self, lst):
        format_workout_lst = []

        for i in lst:
            temp = ft.Container(
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor='#CC99FF',
                border_radius=10,
                border=ft.border.all(3, '#8532B8'),
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text("Workout name- " + i[2], size=20, color=ft.colors.PURPLE,
                                        weight=ft.FontWeight.W_500, selectable=True, font_family="Elephant",
                                        text_align=ft.alignment.center),

                                ft.Text("date- " + str(i[3]), size=20, color=ft.colors.PURPLE,
                                        weight=ft.FontWeight.W_500, selectable=True, font_family="Elephant",
                                        text_align=ft.alignment.center),
                                # ft.ElevatedButton(text="X",value= i[2] ,on_click=self.delete_workout(i[2], i[3]), bgcolor='#8532B8',
                                #                                                color='white'),

                                # self.button_delete_workout
                            ]
                        ),

                        ft.ExpansionTile(
                            title=ft.Text(i[2] + " exercises-"),
                            subtitle=ft.Text("TAP TO SEE THE EXERCISES"),
                            affinity=ft.TileAffinity.LEADING,
                            # initially_expanded=True,
                            collapsed_text_color=ft.colors.BLUE,
                            text_color=ft.colors.BLUE,
                            controls=self.format_exercise_lst(i[4])
                        )
                    ]
                )
            )

            format_workout_lst.append(temp)

        return format_workout_lst

    def format_exercise_lst(self, e_lst):
        lst = []
        if not e_lst:
            return lst

        n = 1
        for i1 in e_lst:
            i = json.loads(i1)
            temp = ft.ExpansionTile(
                title=ft.Text(f"exercise {n}- {i['name']}"),
                subtitle=ft.Text("open for more"),
                affinity=ft.TileAffinity.LEADING,
                collapsed_text_color=ft.colors.PINK,
                text_color=ft.colors.PINK,
                controls=[
                    ft.ExpansionTile(
                        title=ft.Text("exercise information- "),
                        subtitle=ft.Text("open for more"),
                        affinity=ft.TileAffinity.LEADING,
                        # initially_expanded=True,
                        collapsed_text_color=ft.colors.BLUE,
                        text_color=ft.colors.BLUE,
                        controls=[
                            ft.ListTile(title=ft.Text("power- " + i["power"]))
                        ]
                    ),

                    ft.ExpansionTile(
                        title=ft.Text("exercise sets- "),
                        subtitle=ft.Text("open for more"),
                        affinity=ft.TileAffinity.LEADING,
                        # initially_expanded=True,
                        collapsed_text_color=ft.colors.BLUE,
                        text_color=ft.colors.BLUE,
                        controls=self.format_set_lst(i["sets"])
                    )
                ]
            )

            lst.append(temp)
            n = n + 1

        return lst

    def format_set_lst(self, s_lst):
        lst = []
        if not s_lst:
            return lst

        for s in s_lst:
            # s = json.loads(s1)
            repetitions = s["repetitions"]
            time = s["time"]
            weight = s["weight"]
            distance_KM = s["distance_KM"]

            str1 = (f"repetitions- {repetitions} time- {time} weight- {weight} distance_KM- "
                    f"{distance_KM}")
            temp = ft.ListTile(title=ft.Text(str1))
            lst.append(temp)

        return lst

    def calndar_format(self):
        task_manager = CalendarApp.TaskManager(client=self.client)
        grid = CalendarApp.DateGrid(
            year=CalendarApp.Settings.get_year(),
            month=CalendarApp.Settings.get_month(),
            task_instance=task_manager,
            client=self.client
        )

        self.page.add(ft.Row([
            ft.Container(
                height=500,
                border=ft.border.all(1, ft.colors.BLACK),
                border_radius=10,
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                content=grid,
            ),
            ft.Divider(color="transparent", height=20),
            task_manager,
            self.massage
        ]))

        self.page.update()


    def main(self, page: ft.Page) -> None:
        self.page = page
        self.page.scroll = ft.ScrollMode.ALWAYS
        self.page.bgcolor = ft.colors.GREY_100
        self.check1()
        self.page.update()


def main() -> None:
    ft.app(target=ShowTheWorkout.main)


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
        "width": 75, "height": 55, "alignment": ft.alignment.center, "shape": ft.BoxShape("rectangle"),
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
                self.content = ft.Text(f"{self.day}", text_align="center", color="#F509C8")
                # self.content = ft.Text(f"{self.day} \n**", text_align="center")

        def selected(self, e: ft.TapEvent):
            if self.date_instnace:
                for row in self.date_instnace.controls[1:]:
                    for date in row.controls:

                        if date.border is not None:
                            date.border(
                                ft.border.all(0.5, ft.colors.BLACK)
                                if date == e.control else None
                            )
                        date.bgcolor = "#CCCCFF" if date == e.control else None

                        if date == e.control:
                            self.task_instnace.date.value = e.control.data

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
                bgcolor="#C777F3",
                border_radius=ft.border_radius.only(top_left=10, top_right=10),
                content=ft.Row(
                    alignment="center",
                    controls=[
                        ft.IconButton(
                            "chevron_left",
                            on_click=lambda e: self.update_date_grid(e, -1),
                        ),
                        ft.Container(
                            width=430, content=self.date,
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
                            date_obj = datetime.strptime(self.client.user_workout_lst[index][3], '%Y-%m-%dT%H:%M:%S')
                            if day == int(date_obj.strftime("%d")):
                                if int(date_obj.strftime("%m")) == month:
                                    if int(date_obj.strftime("%Y")) == year:
                                        event = True

                        row.controls.append(
                            CalendarApp.DateBox(
                                day, event, self.format_date(day), self,
                                self.task_manager,
                            )
                        )

                    else:
                        row.controls.append(CalendarApp.DateBox(" "))

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
            "focused_border_color": "pink",
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
            self.show_workout_info = ft.ElevatedButton(text="show workout info", on_click=self.go_to_show_workout_info,
                                                       bgcolor='#8532B8', color='white')

            self.button_add_w = ft.ElevatedButton(text="add workout", on_click=self.go_to_app,
                                                  bgcolor='#8532B8', color='white')

            self.event = ft.TextField(read_only=True, border="none", color=ft.colors.BLACK)

            self.boolworkout = ft.TextField(read_only=True, border="none", color=ft.colors.BLACK)

            # self.event = ft.TextField(
            #     label="Date", read_only=True, value=" ", **CalendarApp.input_style(38)
            # )

            self.controls = [ft.Row(
                [
                    ft.Container(
                        alignment=ft.alignment.top_center,
                        bgcolor="#CCCCFF",
                        margin=10,
                        border_radius=10,
                        padding=20,
                        content=ft.Column([
                            ft.Column(
                                [
                                    self.date,
                                    self.event
                                ]
                            ),

                            ft.Row(
                                [
                                    self.show_workout_info,
                                    self.button_add_w
                                ]
                            )
                        ])
                    )
                ])]

        def go_to_app(self, e: ft.ControlEvent) -> None:
            # Function to navigate to App3 page
            if self.date.value != " ":
                self.page.clean()
                app3_instance = AddFullWorkout(client=self.client, date=self.date.value)
                app3_instance.main(self.page)
            else:
                self.event.value = "please select date"
                self.page.update()

        def go_to_show_workout_info(self, e: ft.ControlEvent) -> None:
            # Function to navigate to App3 page
            if self.date.value != " ":
                # self.page.clean()
                app3_instance = ShowTheWorkout(client=self.client, date=self.date.value)
                app3_instance.main(self.page)
            else:
                self.event.value = "please select date"
                self.page.update()

    @staticmethod
    def main(page: ft.Page, client: Client):
        client1 = client
        # page.theme_mode = ft.ThemeMode.DARK
        # page.bgcolor = "1f2128"
        page.bgcolor = ft.colors.GREY_100


        task_manager = CalendarApp.TaskManager(client=client1)
        grid = CalendarApp.DateGrid(
            year=CalendarApp.Settings.get_year(),
            month=CalendarApp.Settings.get_month(),
            task_instance=task_manager,
            client=client1
        )

        page.add(ft.Row([
            ft.Container(
                height=500,
                border=ft.border.all(1, ft.colors.BLACK),
                border_radius=10,
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                content=grid,
            ),
            ft.Divider(color="transparent", height=20),
            task_manager

        ]))

        page.update()


def main() -> None:
    ft.app(target=CalendarApp.main)


if __name__ == "__main__":
    main()
