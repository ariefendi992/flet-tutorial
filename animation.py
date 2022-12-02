from flet import *
import flet as ft
from math import pi


def main(page: Page):
    page.title = "Animation"

    # Opacity animation
    # c = Container(
    #     width=150,
    #     height=150,
    #     bgcolor="blue",
    #     border_radius=10,
    #     animate_opacity=300,
    # )
    # def animate_opacity(e):
    #     c.opacity = 0 if c.opacity == 1 else 1
    #     c.update()

    # page.add(
    #     c,
    #     ElevatedButton("Animate opacity", on_click=animate_opacity),
    # )

    # Rotation animation
    # c = Container(
    #     width=100,
    #     height=70,
    #     bgcolor="blue",
    #     border_radius=5,
    #     rotate=transform.Rotate(0, alignment=alignment.center),
    #     animate_rotation=animation.Animation(
    #         duration=300, curve=AnimationCurve.BOUNCE_OUT
    #     ),
    # )

    # def animate(e):
    #     c.rotate.angle += pi / 2
    #     page.update()

    # page.vertical_alignment = MainAxisAlignment.CENTER
    # page.horizontal_alignment = CrossAxisAlignment.CENTER
    # page.spacing = 30
    # page.add(
    #     c,
    #     ElevatedButton("Animate!", on_click=animate),
    # )

    # Scale animation
    # c = Container(
    #     width=100,
    #     height=100,
    #     bgcolor="blue",
    #     border_radius=5,
    #     scale=transform.Scale(scale=1),
    #     animate_scale=animation.Animation(600, AnimationCurve.BOUNCE_OUT),
    # )

    # def animate(e):
    #     # c.scale =2
    #     c.scale = 2 if c.scale == 1 else 1

    #     page.update()

    # page.vertical_alignment = MainAxisAlignment.CENTER
    # page.horizontal_alignment = CrossAxisAlignment.CENTER
    # page.spacing = 30
    # page.add(c, ElevatedButton("Animate!", on_click=animate))

    # Offset animation
    # c = Container(
    #     width=150,
    #     height=150,
    #     bgcolor="blue",
    #     border_radius=10,
    #     offset=transform.Offset(-2, 0),
    #     animate_offset=animation.Animation(1000),
    # )

    # def animate(e):
    #     c.offset = (
    #         transform.Offset(0, 0)
    #         if c.offset == transform.Offset(-2, 0)
    #         else transform.Offset(-2, 0)
    #     )
    #     c.update()

    # page.add(c, ElevatedButton("Reveal!", on_click=animate))

    # Position animation
    # c1 = Container(width=50, height=50, bgcolor="red", animate_position=1000)
    # c2 = Container(
    #     width=50, height=50, bgcolor="green", top=60, left=0, animate_position=500
    # )
    # c3 = Container(
    #     width=50, height=50, bgcolor="blue", top=120, left=0, animate_position=1000
    # )

    # def animate_container(e):
    #     c1.top = 20
    #     c1.left = 200
    #     c2.top = 100
    #     c2.left = 40
    #     c3.top = 180
    #     c3.left = 100
    #     page.update()

    # page.add(
    #     Stack([c1, c2, c3], height=250),
    #     ElevatedButton("Animate!", on_click=animate_container),
    # )

    # animate container
    # c = Container(
    #     width=150,
    #     height=150,
    #     bgcolor="red",
    #     animate=animation.Animation(1000, AnimationCurve.BOUNCE_OUT),
    # )

    # def animate_container(e):
    #     c.width = 100 if c.width == 150 else 150
    #     c.height = 50 if c.height == 150 else 150
    #     c.bgcolor = "blue" if c.bgcolor == "red" else "red"
    #     c.update()

    # page.add(c, ElevatedButton("Animate Container", on_click=animate_container))

    # Animated content switcher
    i = Image(src="https://picsum.photos/150/150", width=150, height=150)

    sw = AnimatedSwitcher(
        i,
        transition=AnimatedSwitcherTransition.SCALE,
        duration=500,
        switch_in_curve=AnimationCurve.BOUNCE_OUT,
        switch_out_curve=AnimationCurve.BOUNCE_IN,
    )

    def animate(e):
        sw.content = Image(
            src=f"https://picsum.photos/150/150?{time.time()}", width=150, height=150
        )
        page.update()

    page.add(sw, ElevatedButton("Animate!", on_click=animate))


ft.app(target=main)
