import json

import calendar
from datetime import datetime

import flet as ft
import calendar
from datetime import datetime
from project.client import Client


class ShowImproveGraps:
    def __init__(self, client: Client):
        self.page = None
        self.client = client

        self.exercises_name_lst = self.client.user_exer_lst

        self.exercise_name = ft.TextField(label="exercise name", label_style=ft.TextStyle(color=ft.colors.BLACK),
                                          autofocus=True, border_color=ft.colors.WHITE)
        # self.search = ft.SearchBar(
        #
        # )
        self.s_date_text = ft.Text("start date-", size=20, color='#8532B8')
        self.day1 = ft.TextField(label="day", autofocus=True, border_color='#8532B8')
        self.month1 = ft.TextField(label="month", autofocus=True, border_color='#8532B8')
        self.year1 = ft.TextField(label="year", autofocus=True, border_color='#8532B8')

        self.e_date_text = ft.Text("end date-", size=20, color='#8532B8')
        self.day2 = ft.TextField(label="day", autofocus=True, border_color='#8532B8')
        self.month2 = ft.TextField(label="month", autofocus=True, border_color='#8532B8')
        self.year2 = ft.TextField(label="year", autofocus=True, border_color='#8532B8')
        self.button1 = ft.ElevatedButton(text="send", on_click=self.show_graph1_on_click, bgcolor='#8532B8',
                                         color='white')

        self.massageD1 = ft.TextField(read_only=True, border="none", color=ft.colors.BLACK)
        self.massageD2 = ft.TextField(read_only=True, border="none", color=ft.colors.BLACK)
        self.errorM = ft.TextField(read_only=True, border="none", color=ft.colors.BLACK, border_width=50)

        self.s_date = ""
        self.e_date = ""

        self.date_picker1 = ft.DatePicker(
            on_change=self.change_date1,
            on_dismiss=self.date_picker_dismissed1,
        )

        self.date_button1 = ft.ElevatedButton(
            "START date",
            color=ft.colors.BLACK,
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: self.date_picker1.pick_date(),
        )

        self.date_picker2 = ft.DatePicker(
            on_change=self.change_date2,
            on_dismiss=self.date_picker_dismissed2,
        )

        self.date_button2 = ft.ElevatedButton(
            "END date",
            color=ft.colors.BLACK,
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: self.date_picker2.pick_date(),
        )

        self.show_improvement_panel = ft.Column(
            [
                self.exercise_name,
                self.date_button1,
                self.massageD1,
                self.date_button2,
                self.massageD2,
                self.button1,
                self.errorM
            ]
        )

        self.view = ft.Container(
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor='#CC99FF',
            border_radius=10,
            border=ft.border.all(3, '#8532B8'),
            content=ft.Column(
                width=600,
                controls=[
                    ft.Text("CHECK YOUR IMPROVEMENT", size=55, color=ft.colors.WHITE, weight=ft.FontWeight.W_500,
                            selectable=True, font_family="Elephant", text_align=ft.alignment.center),
                    self.exercise_name,

                    ft.Row(
                        controls=[
                            self.date_button1, self.date_button2,
                        ],
                    ),
                    ft.Row(
                        controls=[
                            self.massageD1, self.massageD2,
                        ],
                    ),

                    ft.Row(
                        controls=[
                            self.button1, self.errorM,
                        ],
                    )

                ],
            )
        )

        self.text_chart1 = ft.Container(
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            content=ft.Row(
                alignment=ft.alignment.center,
                width=600,
                controls=[
                    ft.Text(f"THE GRAPH SHOW THE AVG OF THE ALL {self.exercise_name.value} "
                            f"EXERCISES YOU DID IN THE TIME YOU CHOSE", size=20, color=ft.colors.BLACK,
                            weight=ft.FontWeight.W_100,
                            selectable=True, font_family="Century Gothic", text_align=ft.alignment.center),

                ],
            )
        )

        self.text_chart2 = ft.Container(
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            content=ft.Row(
                alignment=ft.alignment.center,
                width=600,
                controls=[
                    ft.Text(f"THE GRAPH SHOW THE IMPROVEMENT OF {1} "
                            f" YOU DID IN THE TIME YOU CHOSE", size=20, color=ft.colors.BLACK,
                            weight=ft.FontWeight.W_100,
                            selectable=True, font_family="Century Gothic", text_align=ft.alignment.center),

                ],
            )
        )

    def change_date1(self, e):
        self.s_date = self.date_picker1.value
        # self.massageD1.value = str(self.date_picker1.value)
        self.massageD1.value = self.date_picker1.value.strftime("%x")
        self.page.update()
        print(f"Date picker 1 changed, value is {self.date_picker1.value}")

    def date_picker_dismissed1(self, e):
        print(f"Date picker dismissed, value is {self.date_picker1.value}")

    def change_date2(self, e):
        self.e_date = self.date_picker2.value
        # self.massageD2.value = str(self.date_picker2.value)
        self.massageD2.value = self.date_picker2.value.strftime("%x")
        self.page.update()
        print(f"Date picker 2 changed, value is {self.date_picker2.value}")

    def date_picker_dismissed2(self, e):
        print(f"Date picker dismissed, value is {self.date_picker2.value}")

    def show_graph1_on_click(self, e: ft.ControlEvent) -> None:
        username = self.client.username
        self.workout_lst = self.client.user_workout_lst

        self.exercise_name2 = self.exercise_name.value

        s_date = self.s_date
        e_date = self.e_date

        if self.exercise_name2 and s_date and e_date:
            if s_date > e_date:
                self.errorM.value = "the stat day should be before \n the end day!"
                self.page.update()

            else:
                response = self.client.improve_with_params2(username, self.exercise_name2, s_date, e_date)
                self.dates_l = response["dates"]
                self.count_sets_l = response["count_sets"]
                self.avgrepete_l = response["repetitions_avg"]
                self.avgtime_l = response["time_avg"]
                self.avgweight_l = response["weight_avg"]
                self.avgdistance_KM_l = response["distance_KM_avg"]

                if not self.dates_l:
                    self.errorM.value = f"there is no {self.exercise_name2} exercise between the days you picked"
                    self.page.update()

                else:
                    self.show_graph1(exercise_name=self.exercise_name2, s_date=s_date, e_date=e_date)


        else:
            self.errorM.value = "please fill all fields"
            self.page.update()

    def click_change_details(self, e: ft.ControlEvent):
        self.page.clean()
        self.page.add(self.view)

    def show_graph1(self, exercise_name: str, s_date, e_date):
        chart1 = self.bring_graph1(exercise_name=exercise_name, s_date=s_date, e_date=e_date)

        view1 = ft.Column(
            # width=600,
            controls=[
                ft.Container(
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor='#CC99FF',
                    content=ft.Column(
                        [
                            ft.Text("THE DETAILS", size=30, color='#8532B8', weight=ft.FontWeight.W_500,
                                    selectable=True, font_family="Elephant"),
                            ft.Text("exercise name: " + exercise_name, size=20, color='#8532B8',
                                    weight=ft.FontWeight.W_500,
                                    selectable=True, font_family="Arial Rounded MT Bold"),
                            ft.Text(s_date.strftime("%x") + " - " + e_date.strftime("%x"), size=20,
                                    color=ft.colors.BLACK,
                                    weight=ft.FontWeight.W_500, selectable=True, font_family="Arial Rounded MT Bold"),
                            ft.ElevatedButton(text="change details", on_click=self.click_change_details,
                                              bgcolor='#8532B8',
                                              color='white'),
                        ]
                    )
                ),

                ft.Row([
                    self.text_chart1
                ]),

                ft.Row(
                    controls=[
                        chart1
                    ],
                )
            ],
        )
        self.page.clean()
        self.page.add(view1)
        self.page.update()


    def bring_graph1(self, exercise_name, s_date, e_date):

        username = self.client.username

        date1 = s_date
        date2 = e_date

        date11 = str(date1.strftime("%x"))
        date22 = str(date2.strftime("%x"))

        dates = date11 + " - " + date22

        response = self.client.showimprovement2(username, exercise_name, s_date, e_date)

        self.count_sets = response["count_sets"]
        self.avgrepete = response["repete"]
        self.avgtime = response["time"]
        self.avgweight = response["weight"]
        self.avgdistance_KM = response["distance_KM"]

        max1 = max(self.count_sets, self.avgrepete, self.avgtime, self.avgweight, self.avgdistance_KM)

        self.chart_of_avg = ft.BarChart(
            bar_groups=[
                ft.BarChartGroup(
                    x=0,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=self.count_sets,
                            width=80,
                            color="#5E5868",
                            tooltip="count the all sets you did",
                            tooltip_style=ft.TextStyle(bgcolor=ft.colors.PINK),
                            border_radius=0,
                        ),
                    ],
                ),
                ft.BarChartGroup(
                    x=1,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=self.avgrepete,
                            width=80,
                            color="#5E5868",
                            tooltip="show the avg of repetitions in every exercise",
                            border_radius=0,
                        ),
                    ],
                ),
                ft.BarChartGroup(
                    x=2,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=self.avgtime,
                            width=80,
                            color="#5E5868",
                            tooltip="show the avg of time in every exercise",
                            border_radius=0,
                        ),
                    ],
                ),
                ft.BarChartGroup(
                    x=3,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=self.avgweight,
                            width=80,
                            color="#5E5868",
                            tooltip="show the avg of weight in every exercise",
                            border_radius=0,
                        ),
                    ],
                ),
                ft.BarChartGroup(
                    x=4,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=self.avgdistance_KM,
                            width=80,
                            color="#5E5868",
                            tooltip="show the avg of distance KM in every exercise",
                            border_radius=0,
                        ),
                    ],
                )
            ],
            border=ft.border.all(1, ft.colors.GREY_400),
            left_axis=ft.ChartAxis(
                labels_size=40, title=ft.Text(dates), title_size=40
            ),
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=0, label=ft.Container(ft.Text("count sets"), padding=10, on_click=self.click_count_sets)
                    ),
                    ft.ChartAxisLabel(
                        value=1, label=ft.Container(ft.Text("avg repete"), padding=10, on_click=self.click_repete)
                    ),
                    ft.ChartAxisLabel(
                        value=2, label=ft.Container(ft.Text("avg time"), padding=10, on_click=self.click_time)
                    ),
                    ft.ChartAxisLabel(
                        value=3, label=ft.Container(ft.Text("avg weight"), padding=10, on_click=self.click_weight)
                    ),
                    ft.ChartAxisLabel(
                        value=4,
                        label=ft.Container(ft.Text("avg distance KM"), padding=10, on_click=self.click_distance_KM)
                    )
                ],
                labels_size=40,
            ),
            horizontal_grid_lines=ft.ChartGridLines(
                color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
            ),
            tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
            max_y=max1 + 15,
            interactive=True,
            expand=True,
        )

        return self.chart_of_avg

    def click_count_sets(self, e: ft.ControlEvent):
        self.page.clean()
        self.show_graph1(exercise_name=self.exercise_name2, s_date=self.s_date, e_date=self.e_date)

        self.show_graph2(exercise_name1=self.exercise_name2, s_date=self.s_date, e_date=self.e_date,
                         lst=self.count_sets_l,
                         date_lst=self.dates_l, name_param="count sets")

    def click_repete(self, e: ft.ControlEvent):
        self.page.clean()
        self.show_graph1(exercise_name=self.exercise_name2, s_date=self.s_date, e_date=self.e_date)

        self.show_graph2(exercise_name1=self.exercise_name2, s_date=self.s_date, e_date=self.e_date,
                         lst=self.avgrepete_l,
                         date_lst=self.dates_l, name_param="repete")

    def click_time(self, e: ft.ControlEvent):
        self.page.clean()
        self.show_graph1(exercise_name=self.exercise_name2, s_date=self.s_date, e_date=self.e_date)

        self.show_graph2(exercise_name1=self.exercise_name2, s_date=self.s_date, e_date=self.e_date, lst=self.avgtime_l,
                         date_lst=self.dates_l, name_param="time")

    def click_weight(self, e: ft.ControlEvent):
        self.page.clean()
        self.show_graph1(exercise_name=self.exercise_name2, s_date=self.s_date, e_date=self.e_date)

        self.show_graph2(exercise_name1=self.exercise_name2, s_date=self.s_date, e_date=self.e_date,
                         lst=self.avgweight_l,
                         date_lst=self.dates_l, name_param="weight")

    def click_distance_KM(self, e: ft.ControlEvent):
        self.page.clean()
        self.show_graph1(exercise_name=self.exercise_name2, s_date=self.s_date, e_date=self.e_date)

        self.show_graph2(exercise_name1=self.exercise_name2, s_date=self.s_date, e_date=self.e_date,
                         lst=self.avgdistance_KM_l,
                         date_lst=self.dates_l, name_param="distance KM")

    def show_graph2(self, exercise_name1: str, s_date, e_date, lst, date_lst, name_param):

        chart_of_params = self.bring_graph2(exercise_name=exercise_name1, s_date=s_date, e_date=e_date, lst=lst,
                                            date_lst=date_lst)


        # view1 = ft.Column(
        #     controls=[
        #
        #         ft.Row(
        #             controls=[
        #                 ft.Text(f"THE GRAPH SHOW THE IMPROVEMENT OF {name_param} "
        #                         f" YOU DID IN THE TIME YOU CHOSE", size=20, color=ft.colors.BLACK,
        #                         weight=ft.FontWeight.W_100,
        #                         selectable=True, font_family="Century Gothic", text_align=ft.alignment.center),
        #             ],
        #         ),
        #         chart_of_params,
        #
        #         ft.Row([])
        #
        #     ]
        # )

        self.page.add(ft.Text(f"THE GRAPH SHOW THE IMPROVEMENT OF {name_param} "
                                f" YOU DID IN THE TIME YOU CHOSE", size=20, color=ft.colors.BLACK,
                                weight=ft.FontWeight.W_100,
                                selectable=True, font_family="Century Gothic", text_align=ft.alignment.center))
        container1 = ft.Column(
            width=1000,
            controls=[
                ft.Container(
                    # margin=120,
                    # padding=120,
                    alignment=ft.alignment.center,
                    content=ft.Column([chart_of_params])
                )]
        )
        self.page.add(container1)
        # self.page.add(chart_of_params)

        # view2 = ft.Column([self.chart_of_params])

        # self.page.clean()

        # self.page.add(view1)
        self.page.update()

    def bring_graph2(self, exercise_name, s_date, e_date, lst, date_lst):
        self.exercise_name = exercise_name
        self.s_date = s_date
        self.e_date = e_date
        self.lst = lst
        self.date_lst = date_lst

        # if len(date_lst) == 0:
        #     return 0

        new_lst = []
        left_axis1 = []
        bottom_axis1 = []

        n = 0
        m = 0
        for i in self.lst:
            new_lst.append(ft.LineChartDataPoint(m, i))

            dt_object = datetime.strptime(self.date_lst[n], "%Y-%m-%dT%H:%M:%S")
            date = str(dt_object.strftime("%x"))

            left_axis1.append(ft.ChartAxisLabel(
                value=i,
                label=ft.Text(str(i), size=14, weight=ft.FontWeight.BOLD),
            ))

            bottom_axis1.append(ft.ChartAxisLabel(
                    value=m,
                    label=ft.Container(
                        ft.Text(
                            value=date,
                            size=14,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                        ),
                        # margin=ft.margin.only(top=10),
                    )
                ))

            n = n + 1
            m = m + 2

        self.data_1 = [
            ft.LineChartData(
                data_points=new_lst,
                stroke_width=5,
                color="#5E5868",
                curved=True,
                stroke_cap_round=True,
            )
        ]

        self.chart_one_parmeter = ft.LineChart(
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
            min_y=0,
            max_y=max(self.lst) + 10,
            min_x=0,
            max_x=m,
            # # animate=5000,
            # expand=True
        )

        return self.chart_one_parmeter


    def main(self, page: ft.Page):
        self.page = page
        self.page.scroll = ft.ScrollMode.ALWAYS

        self.page.overlay.append(self.date_picker1)
        self.page.overlay.append(self.date_picker2)

        row_container = self.view
        row_container.main_alignment = ft.MainAxisAlignment.CENTER

        row_container.width = 600
        self.page.add(row_container)

        self.page.horizontal_alignment = 'CENTER'
        self.page.vertical_alignment = 'CENTER'

        self.page.bgcolor = "#E7CDFF"

        self.page.update()


def main() -> None:
    ft.app(target=ShowImproveGraps.main)


if __name__ == "__main__":
    main()
