from flet import *
import flet as ft


# def main(page: Page):
#     """Drag and Drop"""
#     page.title = "Drag and Drop example"

#     def drag_accept(e):
#         # get draggable (source) control by its ID
#         src = page.get_control(e.src_id)
#         # update text inside draggable control
#         src.content.content.value = "0"
#         # update text inside drag target control
#         e.control.content.content.value = "1"
#         page.update()

#     page.add(
#         Row(
#             controls=[
#                 # Draggable(
#                 #     group="number",
#                 #     content=Container(
#                 #         width=50,
#                 #         height=50,
#                 #         bgcolor=colors.CYAN_200,
#                 #         border_radius=5,
#                 #         content=Text(f"1", size=20),
#                 #         alignment=alignment.center,
#                 #     ),
#                 # ),
#                 ###### animasi ketika di drag content
#                 Draggable(
#                     group="number",
#                     content=Container(
#                         width=50,
#                         height=50,
#                         bgcolor=colors.CYAN_200,
#                         border_radius=5,
#                         content=Text("1", size=20),
#                         alignment=alignment.center,
#                     ),
#                     content_when_dragging=Container(
#                         width=50,
#                         height=50,
#                         bgcolor=colors.BLUE_GREY_200,
#                         border_radius=5,
#                     ),
#                     content_feedback=Text("1"),
#                 ),
#                 Container(width=100),
#                 DragTarget(
#                     group="number",
#                     content=Container(
#                         width=50,
#                         height=50,
#                         bgcolor=colors.PINK_200,
#                         border_radius=5,
#                         content=Text("0", size=20),
#                         alignment=alignment.center,
#                     ),
#                     on_accept=drag_accept,
#                 ),
#             ],
#         ),
#     )

"""DRAG WILL ACCEPT & DRAG LEAVE"""


def main(page: Page):
    page.title = "Drag and Drop example 2"

    def drag_accept(e):
        # get draggable (source) control by it ID
        src = page.get_control(e.src_id)
        # update text inside draggable control
        src.content.content.value = "0"
        # reset source group, so it cannot be dropped to a target anymore
        src.group = """sumary_line"""
        # update text inside darg target control
        e.control.content.content.value = "1"
        # reset border
        e.control.content.border = None
        page.update()

    def drag_will_accept(e):
        # black border when it's allowed to drop and read when it's not
        e.control.content.border = border.all(
            2, colors.BLACK45 if e.data == "true" else colors.RED
        )
        e.control.update()

    def drag_leave(e):
        e.control.content.border = None
        e.control.update()

    page.add(
        Row(
            [
                Draggable(
                    group="number",
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.CYAN_200,
                        border_radius=5,
                        content=Text("1", size=20),
                        alignment=alignment.center,
                    ),
                    content_when_dragging=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.BLUE_GREY_200,
                        border_radius=5,
                    ),
                    content_feedback=Text("1"),
                ),
                Container(width=100),
                DragTarget(
                    group="number",
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.PINK_200,
                        border_radius=5,
                        content=Text("0", size=20),
                        alignment=alignment.center,
                    ),
                    on_accept=drag_accept,
                    on_will_accept=drag_will_accept,
                    on_leave=drag_leave,
                ),
            ],
        ),
    )


ft.app(target=main)
