import flet as ft
from time import sleep


def main(page: ft.Page):
    """Basic app structure"""
    # add/update controls on Page
    # pass

    """CONTROLS"""
    # t = ft.Text(value="Hello, world!", color="green")
    # page.controls.append(t)
    # page.update()
    # t = ft.Text()
    # page.add(t)

    # for i in range(10):
    #     t.value = f"Step {i}"
    #     page.update()
    #     sleep(1)

    # page.add(ft.Row(controls=[ft.Text("A"), ft.Text("B"), ft.Text("C")]))
    # page.update()

    # page.add(
    #     ft.Row(
    #         controls=[
    #             ft.TextField(label="Your Name"),
    #             ft.ElevatedButton(text="Say my name"),
    #         ]
    #     )
    # )

    # for i in range(10):
    #     page.controls.append(ft.Text(f"Line {i}"))
    #     if i > 4:
    #         page.controls.pop(0)
    #     page.update()
    #     sleep(0.3)

    # def button_clicked(e):
    #     page.add(ft.Text("Clicked!"))

    # page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))

    # def add_clicked(e):
    #     # page.add(ft.Checkbox(label=new_task.value))
    #     page.add(ft.Text(new_task.value))

    # new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    # page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

    """VISIBLE PROPERTY
        DISABLED PROPERTY
    """
    # first_name = ft.TextField()
    # last_name = ft.TextField()
    # first_name.disabled = True
    # last_name.disabled = True
    # page.add(first_name, last_name)

    # first_name = ft.TextField()
    # last_name = ft.TextField()
    # c = ft.Column(controls=[first_name, last_name])
    # c.disabled = True
    # page.add(c)

    """CONTROL REFS"""
    # first_name = ft.TextField(label="First Name", autofocus=True)
    # last_name = ft.TextField(label="Last Name")
    # greetings = ft.Column()

    # def btn_click(e):
    #     greetings.controls.append(
    #         ft.Text(f"Hello, {first_name.value} {last_name.value}!")
    #     )
    #     first_name.value = ""
    #     last_name.value = ""
    #     page.update()
    #     first_name.focus()

    # page.add(
    #     first_name,
    #     last_name,
    #     ft.ElevatedButton("Say Hello!", on_click=btn_click),
    #     greetings,
    # )

    fisrt_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()

    def btn_click(e):
        greetings.current.controls.append(
            ft.Text(f"Hello, {fisrt_name.current.value} {last_name.current.value}")
        )
        fisrt_name.current.value = ""
        last_name.current.value = ""
        page.update()
        fisrt_name.current.focus()

    page.add(
        ft.TextField(ref=fisrt_name, label="First Name", autofocus=True),
        ft.TextField(ref=last_name, label="Last Name"),
        ft.ElevatedButton("Say hello!", on_click=btn_click),
        ft.Column(ref=greetings),
    )

# a = lambda ex : ex

ft.app(target=main)
