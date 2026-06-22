import os
# Evita problemas de carga de la ventana gráfica en Windows
os.environ['KIVY_WINDOW'] = 'sdl2'

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

# Ajustamos el tamaño de la ventana para simular un celular
Window.size = (360, 600)

# --- DISEÑO DE LA INTERFAZ CON ESTILO CAPIBARA (Lenguaje KV) ---
KV = '''
MDScreen:
    md_bg_color: 0.38, 0.29, 0.21, 1  # Café Pelaje de Capibara Oscuro

    MDBoxLayout:
        orientation: 'vertical'
        padding: '15dp'
        spacing: '10dp'

        # 1. IMAGEN DEL CAPIBARA
        AsyncImage:
            source: "https://www.shutterstock.com/shutterstock/photos/2536715087/display_1500/stock-vector-cute-capybara-character-funny-flat-animal-vector-tangerine-on-head-of-kawaii-capibara-isolated-2536715087.jpg"
            size_hint_y: 0.25
            allow_stretch: True
            keep_ratio: True

        # 2. PANTALLA DE LA CALCULADORA
        MDTextField:
            id: pantalla
            text: "0"
            halign: "right"
            font_size: "45sp"
            multiline: False
            readonly: True
            mode: "fill"
            fill_color_normal: 0.95, 0.92, 0.88, 1    # Fondo beige claro
            text_color_normal: 0, 0, 0, 1            # Números de la pantalla en NEGRO
            text_color_focus: 0, 0, 0, 1
            size_hint_y: 0.15
            line_color_normal: 0, 0, 0, 0            
            line_color_focus: 0, 0, 0, 0

        # 3. TECLADO DE BOTONES
        MDGridLayout:
            cols: 4
            spacing: '10dp'
            size_hint_y: 0.60

            # Fila 1
            MDFillRoundFlatButton:
                text: "C"
                md_bg_color: 0.7, 0.3, 0.2, 1  
                text_color: "white"
                font_size: "22sp"
                on_release: app.limpiar_pantalla()
            MDFillRoundFlatButton:
                text: "("
                md_bg_color: 0.52, 0.42, 0.33, 1  
                text_color: "white"
                font_size: "22sp"
                on_release: app.agregar_caracter("(")
            MDFillRoundFlatButton:
                text: ")"
                md_bg_color: 0.52, 0.42, 0.33, 1
                text_color: "white"
                font_size: "22sp"
                on_release: app.agregar_caracter(")")
            MDFillRoundFlatButton:
                text: "/"
                md_bg_color: 0.9, 0.55, 0.2, 1    # Naranja
                text_color: "white"
                font_size: "22sp"
                on_release: app.agregar_caracter("/")

            # Fila 2
            MDFillRoundFlatButton:
                text: "7"
                md_bg_color: 0.23, 0.18, 0.13, 1  # Café oscuro
                text_color: "white"
                font_size: "22sp"
                on_release: app.agregar_caracter("7")
            MDFillRoundFlatButton:
                text: "8"
                md_bg_color: 0.23, 0.18, 0.13, 1
                text_color: "white"
                font_size: "22sp"
                on_release: app.agregar_caracter("8")
            MDFillRoundFlatButton:
                text: "9"
                md_bg_color: 0.23, 0.18, 0.13, 1
                text_color: "white"
                font_size: "22sp"
                on_release: app.agregar_caracter("9")
            MDFillRoundFlatButton:
                text: "*"
                md_bg_color: 0.9, 0.55, 0.2, 1
                text_color: "white"
                font_size: "22sp"
                on_release: app.agregar_caracter("*")

            # Fila 3
            MDFillRoundFlatButton:
                text: "4"
                md_bg_color: 0.23, 0.18, 0.13, 1
                text_color: "white"
                font_size: "22sp"
                on_release: app.agregar_caracter("4")
            MDFillRoundFlatButton:
                text: "5"
                md_bg_color: 0.23, 0.18, 0.13, 1
                text_color: "white"
                font_size: "22sp"
                on_release: app.agregar_caracter("5")
            MDFillRoundFlatButton:
                text: "6"
                md_bg_color: 0.23, 0.18, 0.13, 1
                text_color: "white"
                font_size: "22sp"
                on_release: app.agregar_caracter("6")
            MDFillRoundFlatButton:
                text: "-"
                md_bg_color: 0.9, 0.55, 0.2, 1
                text_color: "white"
                font_size: "22sp"
                on_release: app.agregar_caracter("-")

            # Fila 4
            MDFillRoundFlatButton:
                text: "1"
                md_bg_color: 0.23, 0.18, 0.13, 1
                text_color: "white"
                font_size: "22sp"
                on_release: app.agregar_caracter("1")
            MDFillRoundFlatButton:
                text: "2"
                md_bg_color: 0.23, 0.18, 0.13, 1
                text_color: "white"
                font_size: "22sp"
                on_release: app.agregar_caracter("2")
            MDFillRoundFlatButton:
                text: "3"
                md_bg_color: 0.23, 0.18, 0.13, 1
                text_color: "white"
                font_size: "22sp"
                on_release: app.agregar_caracter("3")
            MDFillRoundFlatButton:
                text: "+"
                md_bg_color: 0.9, 0.55, 0.2, 1
                text_color: "white"
                font_size: "22sp"
                on_release: app.agregar_caracter("+")

            # Fila 5
            MDFillRoundFlatButton:
                text: "+/-"
                md_bg_color: 0.52, 0.42, 0.33, 1
                text_color: "white"
                font_size: "18sp"
                on_release: app.invertir_signo()
            MDFillRoundFlatButton:
                text: "0"
                md_bg_color: 0.23, 0.18, 0.13, 1
                text_color: "white"
                font_size: "22sp"
                on_release: app.agregar_caracter("0")
            MDFillRoundFlatButton:
                text: "."
                md_bg_color: 0.23, 0.18, 0.13, 1
                text_color: "white"
                font_size: "22sp"
                on_release: app.agregar_caracter(".")
            MDFillRoundFlatButton:
                text: "="
                md_bg_color: 0.4, 0.6, 0.3, 1  # Verde musgo
                text_color: "white"
                font_size: "22sp"
                on_release: app.procesar_resultado()
'''

class CalculadoraCapiApp(MDApp):
    def build(self):
        # Desactivamos paletas automáticas para usar nuestros colores manuales
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def agregar_caracter(self, caracter):
        texto_actual = self.root.ids.pantalla.text
        if texto_actual == "0" or texto_actual == "Capi-Error":
            self.root.ids.pantalla.text = caracter
        else:
            self.root.ids.pantalla.text = f"{texto_actual}{caracter}"

    def limpiar_pantalla(self):
        self.root.ids.pantalla.text = "0"

    def invertir_signo(self):
        texto_actual = self.root.ids.pantalla.text
        if texto_actual != "0" and texto_actual != "Capi-Error":
            if texto_actual.startswith("-"):
                self.root.ids.pantalla.text = texto_actual[1:]
            else:
                self.root.ids.pantalla.text = f"-{texto_actual}"

    def procesar_resultado(self):
        texto_actual = self.root.ids.pantalla.text
        try:
            resultado = str(eval(texto_actual))
            if resultado.endswith('.0'):
                resultado = resultado[:-2]
            self.root.ids.pantalla.text = resultado
        except Exception:
            self.root.ids.pantalla.text = "Capi-Error"

if __name__ == '__main__':
    CalculadoraCapiApp().run()