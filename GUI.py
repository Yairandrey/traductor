from logica import logica
import tkinter as tk

class GUI:

    _languages=['english','romanian','hungarian','greek','finnish',
                'danish','norwegian','swedish','dutch','polish',
                'ukrainian','vietnamese','malay','tagalog','swahili']

    def createWindow(self):
        window = tk.Tk()
        window.config(background='#B0E0E6')
        window.title("Traductor")
        label_one = tk.Label(window, text='Traductor de idiomas', font=('Verdana 23'), fg='#696969',bg='#B0E0E6')
        label_one.place(x=500, y=30)
        label_two = tk.Label(window, text="Ingresa texto", font=('Verdana 18'), fg='red', bg='#B0E0E6')
        label_two.place(x=300, y=100)
        entry = tk.Entry(window)
        entry.place(x=480, y =100, height=50, width=300)
        label_three = tk.Label(window, text="Elige idioma a traducir", font=('Verdana 20'), fg='black', bg='#B0E0E6')
        label_three.place(x=400, y=250)
        a = 40
        b = 320
        i = 0
        for languages in GUI._languages:
            btn = tk.Button(window, text=languages, font=('Verdana 22'), fg='black', bg='#36454F',width=10, height=2,justify='center')
            btn.place(x=a,y=b)
            a += 200
            if i == 4 or i == 9 or i == 14:
                b += 150
                a = 40
            i += 1
        label_four = tk.Button(window, text="Calcular", width=20, height=2,background='#708090',fg='black',font='Verdana 18',command=lambda: logica.translator(a,entry.get(), 'english',window))
        label_four.place(x=850, y=100)
        window.mainloop()






















    






