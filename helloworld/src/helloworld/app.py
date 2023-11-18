"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from graphql_client.client import Client
from graphql_client.film_query import FilmQuery


class HelloWorld(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        self.main_window = toga.MainWindow(title=self.formal_name)
        button = toga.Button(
            "Fetch!",
            on_press=self.fetch_content,
            style=Pack(padding=5)
        )
        main_box.add(button)
        self.label = toga.Label(text="no data yet")
        main_box.add(self.label)
        self.main_window.content = main_box
        self.main_window.show()

    async def fetch_content(self, widget):
        async with Client(url="https://swapi-graphql.netlify.app/.netlify/functions/index") as client:
            model: FilmQuery = await client.film_query(id="ZmlsbXM6MQ==")


        self.label.text = f"{model.film.title} was released in {model.film.release_date}"


def main():
    return HelloWorld()
