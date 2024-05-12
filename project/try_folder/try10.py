import flet as ft

class State:
    toggle = True

s = State()

def main(page: ft.Page):
    con1 = ft.Column(
        height=50,
        controls=[ft.Text("con1")])

    con2 = ft.Column([ft.Text("con2")])


    # page.add(ft.Row(
    #     alignment=ft.MainAxisAlignment.CENTER,
    #     controls=[con1,con2]
    # ))

    # page.add(ft.Column([con1]),ft.Column([con2]))
    page.add(ft.Row([ft.Column([con1]),ft.Column([con2])]))
    page.add(ft.Row([ft.Column([con1]),ft.Column([con2])]))



ft.app(main)