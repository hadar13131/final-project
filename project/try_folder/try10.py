import flet as ft

class State:
    toggle = True

s = State()

def main(page: ft.Page):
    exercise_name = "exercise_name"
    s_date = "s_date"
    e_date = "e_date"
    lst = [1,2,3]
    date_lst = ["date_lst","date_lst","date_lst"]

    new_lst = []
    left_axis1 = []
    bottom_axis1 = []

    n = 0
    m = 0
    for i in lst:
        new_lst.append(ft.LineChartDataPoint(m, i))

        left_axis1.append(ft.ChartAxisLabel(
            value=i,
            label=ft.Text(str(i), size=14, weight=ft.FontWeight.BOLD),
        ))

        bottom_axis1.append(ft.ChartAxisLabel(
            value=m,
            label=ft.Container(
                ft.Text(
                    value=date_lst[n],
                    size=14,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                ),
                # margin=ft.margin.only(top=10),
            )
        ))

        n = n + 1
        m = m + 2

    data_1 = [
        ft.LineChartData(
            data_points=new_lst,
            stroke_width=5,
            color="#5E5868",
            curved=True,
            stroke_cap_round=True,
        )
    ]

    chart_one_parmeter = ft.LineChart(
        data_series=data_1,
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
        max_y=max(lst)+1,
        min_x=0,
        max_x=m,
        # # animate=5000,
        # expand=True
    )

    con = ft.Column(
        width=1000,
        controls=[
        ft.Container(
        # margin=120,
        # padding=120,
        alignment=ft.alignment.center,
        content=ft.Column([chart_one_parmeter])
    )]
    )
    page.add(con)
    page.add(ft.Column([chart_one_parmeter]))

ft.app(main)