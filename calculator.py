#https://www.youtube.com/watch?v=qfSJJVjp6BY
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]


if __name__ == "__main__":
    app = MainApp()
    app.run()