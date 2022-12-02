from flet import *
import flet as ft
import os

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


def main(page: Page):
    """Large List"""
    # for i in range(5000):
    #     page.controls.append(Text(f"Line {i}"))

    # page.scroll = "always"
    # page.update()

    """ListView"""
    # lv = ListView(expand=True, spacing=10)
    # for i in range(5000):
    #     lv.controls.append(Text(f"Line {i}"))

    # page.add(lv)

    """GridView"""
    # r = Row(wrap=True, scroll="always", expand=True)
    # page.add(r)

    # for i in range(5000):
    #     r.controls.append(
    #         Container(
    #             Text(f"Item {i}"),
    #             width=100,
    #             height=100,
    #             alignment=alignment.center,
    #             bgcolor=colors.AMBER_100,
    #             border=border.all(1, colors.AMBER_400),
    #             border_radius=border_radius.all(5),
    #         )
    #     )
    # page.update()

    """GridView Similar"""
    # gv = GridView(expand=True, max_extent=150, child_aspect_ratio=1)
    # page.add(gv)

    # for i in range(5000):
    #     gv.controls.append(
    #         Container(
    #             Text(f"Item {i}", color=colors.BLACK),
    #             alignment=alignment.center,
    #             bgcolor=colors.AMBER_100,
    #             border=border.all(1, colors.AMBER_400),
    #             border_radius=border_radius.all(5),
    #         ),
    #     )
    # page.update()

    """Batch Update"""
    #  add ListView to a page first
    lv = ListView(expand=True, spacing=10, item_extent=50)
    page.add(lv)

    for i in range(5100):
        lv.controls.append(Text(f"Line {i}"))
        # send page to a page
        if i % 500 == 0:
            page.update()

    # send the rest to a page
    page.update()


ft.app(target=main)
