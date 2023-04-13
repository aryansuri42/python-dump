import webbrowser
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time
from filesharing import FileSharer
from kivy.core.clipboard import Clipboard

Builder.load_file('frontend.kv')


class WebcamScreen(Screen):
    def start(self):
        self.ids.cam.play = True
        self.ids.cam_button.text = "Stop Camera"

    def stop(self):
        self.ids.cam.play = False
        self.ids.cam_button.text = "Start Camera"
        self.ids.cam.texture = None

    def capture(self):
        filename = time.strftime("%Y%m%d")
        self.filepath = filename+"image.png"
        self.ids.cam.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    def create_link(self):
        name = App.get_running_app().root.ids.webcam_screen.filepath
        fileshare =FileSharer(filepath = name)
        self.url = fileshare.share()
        self.ids.link.text = self.url

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            name = App.get_running_app().root.ids.webcam_screen.filepath
            fileshare = FileSharer(filepath=name)
            self.url = fileshare.share()
            self.ids.link.text = self.url
            Clipboard.copy(self.url)

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            name = App.get_running_app().root.ids.webcam_screen.filepath
            fileshare = FileSharer(filepath=name)
            self.url = fileshare.share()
            self.ids.link.text = self.url
            webbrowser.open(self.url)


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
