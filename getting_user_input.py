import flet as ft
from flet import *


# def main(page: Page):
#     """BUTTONS"""
#     # btn = ElevatedButton("Click me!")
#     # page.add(btn)

#     """Even Handlers"""
#     # page.title = "Flet counter example"
#     # page.vertical_alignment = MainAxisAlignment.CENTER

#     # txt_number = TextField(value="0", width=100, text_align="center")

#     # def minus_click(e):
#     #     txt_number.value = str(int(txt_number.value) - 1)
#     #     page.update()

#     # def plus_click(e):
#     #     txt_number.value = str(int(txt_number.value) + 1)
#     #     page.update()

#     # page.add(
#     #     Row(
#     #         controls=[
#     #             IconButton(icons.REMOVE, on_click=minus_click),
#     #             txt_number,
#     #             IconButton(icons.ADD, on_click=plus_click),
#     #         ],
#     #         alignment=MainAxisAlignment.CENTER,
#     #     ),
#     # )


# def main(page):
#     # """Textbox"""
#     # #
#     # def btn_click(e):
#     #     if not txt_name.value:
#     #         txt_name.error_text = "Please enter your name"
#     #         page.update()
#     #     else:
#     #         name = txt_name.value
#     #         page.clean()
#     #         page.add(Text(f"Hello, {name}"))

#     # txt_name = TextField(label="Your name")

#     # page.add(txt_name, ElevatedButton("Say hello!", on_click=btn_click))

#     """Checkbox"""

#     def checkbox_change(e):
#         output_text.value = f"You have learned how to ski : {todo_check.value}"
#         page.update()

#     output_text = ft.Text()
#  todo_check = Checkbox(
#         label="ToDo : Learn how to use ski", value=False, on_change=checkbox_change
#     )

#     page.add(todo_check, output_text)


def main(page: Page):
    """Dropdown"""

    def button_clicked(e):
        output_text.value = f"Dropdown value is: {color_dropdown.value}"
        page.update()

    output_text = Text()
    submit_btn = ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = Dropdown(
        width=100,
        options=[
            dropdown.Option("Red"),
            dropdown.Option("Green"),
            dropdown.Option("Blue"),
        ],
    )
    page.add(color_dropdown, submit_btn, output_text)


ft.app(target=main)
