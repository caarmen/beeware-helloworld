"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


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
        text = "Content to fetch from a url"
        self.label.text = text


def main():
    return HelloWorld()
