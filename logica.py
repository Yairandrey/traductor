from googletrans import Translator
import tkinter as tk

class logica:

    def translator(self,text,idiom_to_translate,window):
        print(f'texto ingresado es: {text}')
        translator = Translator()
        res = translator.translate(text, src='spanish', dest=idiom_to_translate)
        print(f'traduccion es:  {res.text}')
        label_five = tk.Label(window, text="El idioma seleccionado es: ", font=('Verdana 17'), fg='black', bg='#B0E0E6')
        label_five.place(x=1050,y=300)