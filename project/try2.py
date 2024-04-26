import json

import calendar
from datetime import datetime

import flet as ft
import calendar
from datetime import datetime
from project.client import Client

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

        response = self.client.improve_with_params2(username, exercise_name, s_date, e_date)
        dates_l = response["dates"]
        count_sets_l = response["count_sets"]
        avgrepete_l = response["repetitions_avg"]
        avgtime_l = response["time_avg"]
        avgweight_l = response["weight_avg"]
        avgdistance_KM_l = response["distance_KM_avg"]

        chart1 = self.show(exercise_name=exercise_name, s_date=s_date, e_date=e_date, lst=avgrepete_l, date_lst=dates_l)
        chart2 = self.show(exercise_name=exercise_name, s_date=s_date, e_date=e_date, lst=avgtime_l, date_lst=dates_l)
        chart3 = self.show(exercise_name=exercise_name, s_date=s_date, e_date=e_date, lst=avgweight_l, date_lst=dates_l)
        chart4 = self.show(exercise_name=exercise_name, s_date=s_date, e_date=e_date, lst=avgdistance_KM_l, date_lst=dates_l)
        chart5 = self.show(exercise_name=exercise_name, s_date=s_date, e_date=e_date, lst=count_sets_l, date_lst=dates_l)
        # self.page.add(chart1)
        # self.page.add(chart2)
        # self.page.add(chart3)
        # self.page.add(chart4)
        # self.page.add(chart5)
        self.page.update()

        self.graphs_panel = ft.Column(
            [
                chart1,
                chart2,
                chart3,
                chart4,
                chart5
            ]
        )

        self.page.add(chart1, chart2, chart3, chart4, chart5)
        self.page.update()


        # app_instance = Graphs1(client=self.client, exercise_name=exercise_name, s_date=s_date, e_date=e_date,
        #                        lst=avgrepete_l, date_lst=dates_l)
        # app_instance.main(self.page)

    # def click2(self, e: ft.ControlEvent) -> None:
        # self.page.clean()
        # self.page.add(ft.Row([self.chart]))
        # self.page.update()


    def show(self, exercise_name, s_date, e_date, lst, date_lst):
        self.exercise_name = exercise_name
        self.s_date = s_date
        self.e_date = e_date
        self.lst = lst
        self.date_lst = date_lst

        # lst = [7, 3, 4]
        # date_lst = ["2020-11-17T00:00:00", "2020-09-19T00:00:00", "2020-09-22T00:00:00"]
        new_lst = []
        left_axis1 = []
        bottom_axis1 = []

        n = 0
        m = 2
        for i in self.lst:
            new_lst.append(ft.LineChartDataPoint(m, i))

            dt_object = datetime.strptime(self.date_lst[n], "%Y-%m-%dT%H:%M:%S")

            left_axis1.append(ft.ChartAxisLabel(
                value=i,
                label=ft.Text(str(i), size=14, weight=ft.FontWeight.BOLD),
            ))

            bottom_axis1.append(ft.ChartAxisLabel(
                value=m,
                label=ft.Container(
                    ft.Text(
                        str(dt_object.strftime("%x")),
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                    ),
                    margin=ft.margin.only(top=10),
                )
            ))

            n = n + 1
            m = m + 2

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
            min_y=0
            # max_y=6,
            # min_x=0,
            # max_x=11,
            # # animate=5000,
            # expand=True,
        )

        return self.chart


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
    ft.app(target=ShowImprove1.main)


if __name__ == "__main__":
    main()
