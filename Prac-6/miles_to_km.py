from kivy.app import App
from kivy.lang import Builder


class ConvertMilesToKilometers(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("miles_to_km.kv")
        return self.root

    def get_user_input(self):
        try:
            input_value = float(self.root.ids.user_input.text)
            self.calculate_kilometers()
            return input_value
        except: ValueError
        input_value = 0.0
        return input_value

    def update_number(self, number):
        input_value = self.get_user_input()+ float(number)
        self.root.ids.user_input.text = str(input_value)

    def calculate_kilometers(self):
        miles = self.get_user_input()
        kilometers = miles * float(1.6)
        self.root.ids.display_output.text = str(kilometers)

ConvertMilesToKilometers().run()
