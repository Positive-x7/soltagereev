from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

def get_kuku():
    print('Kuku')
def get_hello():
    print('Hello')
def get_Bye():
    print('Bye')
def get_good():
    print('good')

class MyApp(App):
    def build(self):    
        main_line = BoxLayout(orientation='vertical')
        line1 = BoxLayout()
        line2 = BoxLayout(padding=20 , spacing=20)
        line3 = BoxLayout(padding=20, spacing=20)
        line4 = BoxLayout(padding=20, spacing=20)

        img1 = Image(source='830.jpg')
        txt1 = Label(text='Это надпись', color=(1,0.3,0.3), font_size=45)
        img2 = Image(source='831..jpg')
        txt2 = Label(text='Это что-то', color=(0.3,0.4,0.7), font_size=45)
        btn1 = Button(text='Скрепки', color=(0,0.7,0.3), font_size=65, background_color=(0,0,1))
        btn2 = Button(text='Скобы')
        btn3 = Button(text='ПРИВЕТ', color=(0,0.4,0.6), font_size=45, background_color=(0,0.6,0.4))
        btn4 = Button(text='ПОКА', color=(0,0.9,0.9), font_size=45, background_color=(0,0.8,0.8))
        btn1.on_press = get_kuku
        btn2.on_press = get_hello
        btn3.on_press = get_Bye
        btn4.on_press = get_good

        line1.add_widget(img1)
        line1.add_widget(txt1)
        line4.add_widget(img2)
        line4.add_widget(txt2)
        line2.add_widget(btn1)
        line2.add_widget(btn2)
        line3.add_widget(btn3)
        line3.add_widget(btn4)

        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(line3)
        main_line.add_widget(line4)

        return main_line
    
MyApp().run()