import os
from dotenv import load_dotenv
import flet as ft
from flet.auth.providers.github_oauth_provider import GitHubOAuthProvider
from flet.auth.oauth_provider import OAuthProvider

load_dotenv()


def main(page: ft.Page):
    # # Sign in with OAuth provider
    # provider = GitHubOAuthProvider(
    #     client_id="b88ec891f9d07cb1019b",
    #     client_secret="eb94cf06e89619d50737f367d5e9f3fc23aab30b",
    #     redirect_url="http://localhost:8550/api/oauth/redirect",
    # )

    # def login_click(e):
    #     page.login(provider)

    # def on_login(e):
    #     print("Access token:", page.auth.token.access_token)
    #     print("User ID:", page.auth.user.id)

    # page.on_login = on_login
    # page.add(ft.ElevatedButton("Login with GitHub", on_click=login_click))

    # # Checking authentication results
    # provider = GitHubOAuthProvider(
    #     client_id=os.getenv("GITHUB_CLIENT_ID"),
    #     client_secret=os.getenv("GITHUB_CLIENT_SECRET"),
    #     redirect_url="http://localhost:8550/api/oauth/redirect",
    # )
    # # print(f"client id {os.getenv('GITHUB_CLIENT_ID')}")

    # def login_button_click(e):
    #     page.login(provider, scope=["public_repo"])

    # def on_login(e: ft.LoginEvent):
    #     print("Name:", page.auth.user["name"])
    #     print("Login:", page.auth.user["login"])
    #     print("Email:", page.auth.user["email"])
    #     if not e.error:
    #         toggle_login_buttons()

    # def logout_button_click(e):
    #     page.logout()

    # def on_logout(e):
    #     toggle_login_buttons()

    # def toggle_login_buttons():
    #     login_button.visible = page.auth is None
    #     logout_button.visible = page.auth is not None
    #     page.update()

    # login_button = ft.ElevatedButton("Login with GitHub", on_click=login_button_click)
    # logout_button = ft.ElevatedButton("Logout", on_click=logout_button_click)
    # toggle_login_buttons()
    # page.on_login = on_login
    # page.on_logout = on_logout
    # page.add(login_button, logout_button)

    # Configuring a custom OAuth provider
    provider = OAuthProvider(
        client_id=os.getenv("LINKEDIN_CLIENT_ID"),
        client_secret=os.getenv("LINKEDIN_CLIENT_SECRET"),
        authorization_endpoint="https://www.linkedin.com/oauth/v2/authorization",
        token_endpoint="https://www.linkedin.com/oauth/v2/accessToken",
        redirect_url="http://localhost:8550/api/oauth/redirect",
        user_endpoint="https://api.linkedin.com/v2/me",
        user_scopes=["r_liteprofile", "r_emailaddress"],
        user_id_fn=lambda u: u["id"],
    )

    def login_click(e):
        page.login(provider)

    def on_login(e):
        if e.error:
            raise Exception(e.error)
        print("User ID:", page.auth.user.id)
        print("Access token:", page.auth.token.access_token)

    page.on_login = on_login
    page.add(ft.ElevatedButton("Login with LinkedIn", on_click=login_click))


ft.app(target=main, port=8550, view=ft.WEB_BROWSER)
