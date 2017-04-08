from kivy.app import App
from kivy.lang import Builder


class ConvertMilesToKilometers(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("miles_to_km.kv")
        return self.root


ConvertMilesToKilometers().run()
