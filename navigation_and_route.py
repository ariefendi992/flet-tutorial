from flet import *
import flet as ft


# def main(page: Page):
#     """Page Route"""
#     page.add(Text(f"Inital route: {page.route}"))

#     def route_change(route):
#         page.add(Text(f"New route: {route}"))

#     page.on_route_change = route_change
#     page.update()

"""Route can be changed programmatically, by updating page.route property:"""
#
# def main(page: Page):
#     page.add(Text(f"Initial route: {page.route}"))

#     def route_change(route):
#         page.add(Text(f"New route: {route}"))

#     def go_store(e):
#         page.route = "/store"
#         page.update()

#     page.on_route_change = route_change
#     page.add(ElevatedButton("Go to store", on_click=go_store))


"""Building views on route change"""
#
def main(page: Page):
    page.title = "Route Example"

    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Flet app"), bgcolor=colors.SURFACE_VARIANT),
                    ElevatedButton("Visit Sotre", on_click=lambda _: page.go("/store")),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                View(
                    "/store",
                    [
                        AppBar(title=Text("Store"), bgcolor=colors.SURFACE_VARIANT),
                        ElevatedButton("Go Gome", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    # troute = TemplateRoute(page.route)

    # if troute.match("/books/:id"):
    #     print("Book view ID:", troute.id)
    # elif troute.match("/account/:account_id/orders/:order_id"):
    #     print("Account:", troute.account_id, "Order:", troute.order_id)
    # else:
    #     print("Unknown route")


ft.app(target=main, view=WEB_BROWSER)
