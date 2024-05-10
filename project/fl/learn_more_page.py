import flet as ft
import welcome_page


class LearnMorePage:

    def __init__(self) -> None:
        self.page = None
        self.text1 = ft.Text("ABOUT US", size=60, color='#8532B8', weight=ft.FontWeight.W_500,
                             selectable=True, font_family="Elephant")

        self.m1 = ft.Text("information", size=20, color='#8532B8')
        self.m2 = ft.Text("pictures", size=20, color='#8532B8')

        self.button_Back = ft.ElevatedButton(text="BACK", on_click=self.back_to_welcome, bgcolor='#8532B8',
                                             color='white')

        self.learn_more_panel = ft.Column(
            [
                self.text1,
                self.m1,
                self.m2,
                self.button_Back
            ]
        )

    def back_to_welcome(self, e: ft.ControlEvent) -> None:
        self.page.clean()
        app_instance = welcome_page.First_page()
        app_instance.main(self.page)

    def main(self, page: ft.Page) -> None:
        self.page = page
        self.page.scroll = ft.ScrollMode.ALWAYS

        row_container = ft.Row([self.learn_more_panel])
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