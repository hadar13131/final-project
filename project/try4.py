import flet as ft
from datetime import datetime

# class Time2:
#     def __init__(self):
#         self.page = None
#         self.selected_date = None
#
#         self.button1 = ft.CupertinoDatePicker(
#             on_change=self.handle_picker_change,  # Call the handle_date_change function
#             date_picker_mode=ft.CupertinoDatePickerMode.DATE_AND_TIME
#         )
#
#         self.button3 = ft.OutlinedButton(
#             "Show CupertinoDatePicker",
#             on_click=lambda e: self.page.show_bottom_sheet(
#                 ft.CupertinoBottomSheet(
#                     ft.CupertinoDatePicker(
#                         on_change=lambda e: print(e.data),
#                         date_picker_mode=ft.CupertinoDatePickerMode.DATE_AND_TIME
#                     ),
#                     height=216,
#                     padding=ft.padding.only(top=6)
#                 )
#             ),
#         )
#
#         self.button2 = ft.OutlinedButton(
#             "Save Selected Date",
#             on_click=self.save_selected_date
#         )
#
#     def handle_date_change(self, event):
#         # Access the selected date from the event data and assign it to the selected_date attribute
#         self.selected_date = event.data
#         print("Selected date:", self.selected_date)
#
#     def save_selected_date(self, event):
#         if self.selected_date is not None:
#             # Use the selected_date attribute and perform any actions you want
#             print("Selected date to be saved:", self.selected_date)
#         else:
#             print("Please select a date first.")
#
#     def handle_picker_change(self, e):
#         self.selected_date.current.value = e.data
#         self.page.update()
#
#     def main(self, page: ft.Page):
#         self.page = page
#         self.page.theme_mode = ft.ThemeMode.LIGHT
#         self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#         self.page.add(self.button3, self.button2)
#
# def main() -> None:
#     ft.app(target=Time2().main)
#
# if __name__ == "__main__":
#     main()


class Time3:
    def __init__(self):
        self.page = None

        self.date_picker = ft.DatePicker(
            on_change=self.change_date,
            on_dismiss=self.date_picker_dismissed,
            # first_date=datetime(2023, 10, 1),
            # last_date=datetime(2024, 10, 1),
        )

        self.date_button = ft.ElevatedButton(
            "Pick date",
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: self.date_picker.pick_date(),
        )

    def change_date(self, e):
        print(f"Date picker changed, value is {self.date_picker.value}")

    def date_picker_dismissed(self, e):
        print(f"Date picker dismissed, value is {self.date_picker.value}")

    def main(self, page: ft.Page):
        self.page = page
        self.page.overlay.append(self.date_picker)
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.add(self.date_button)

def main() -> None:
    ft.app(target=Time3().main)

if __name__ == "__main__":
    main()


