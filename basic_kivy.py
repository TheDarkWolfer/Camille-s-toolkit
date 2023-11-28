from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class LabelChangerApp(App):
    def build(self):
        self.label_text = "Hello, Kivy!"

        layout = BoxLayout(orientation='vertical')
        self.label = Label(text=self.label_text)
        button = Button(text="Change Label", on_press=self.change_label_text)

        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def change_label_text(self, instance):
        self.label_text = "Label changed!"
        self.label.text = self.label_text


if __name__ == '__main__':
    LabelChangerApp().run()
