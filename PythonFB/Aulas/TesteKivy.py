from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        label = Label(
            text='Fala Galera!',
            size_hint=(.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        return label

if __name__ == '__main__':
    my_app = MainApp()
    my_app.run()
