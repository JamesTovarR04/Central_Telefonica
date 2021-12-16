from tkinter import *
from pygame import mixer

class Telefono(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.configure(bg='#171717')
        self.grid()
        self.crearElementos()
        mixer.init()

    def establecerLlamada(self):
        mixer.music.load("./sounds/tonoRespuesta.mp3")
        mixer.music.play()
        self.display.delete(0, END)
        self.display.insert(0,'Hablando...')

    def llamar(self):
        self.numLlamar = self.display.get()
        for abonado in self.abonados:
            if str(abonado.numero) == self.numLlamar:
                if abonado.estado == 'Ocupado':
                    self.display.insert(END,' está ' + abonado.estado)
                    mixer.music.load("./sounds/tonoOcupado.wav")
                    mixer.music.play()
                elif abonado.estado == 'Fuera de servicio':
                    self.display.insert(END,' está ' + abonado.estado)
                    mixer.music.load("./sounds/tonoFueradeServicio.wav")
                    mixer.music.play()
                elif abonado.estado == 'Disponible':
                    mixer.music.load("./sounds/tonoMarcando.wav")
                    mixer.music.play()
                    self.display.insert(0,'Llamando: ')
                    self.display.after(22000, self.establecerLlamada)
                return
        self.display.insert(0,'No existe :(')
        mixer.music.load("./sounds/tonoFueradeServicio.wav")
        mixer.music.play()
        
    def listaAbonados(self, listaAbonados):
        self.abonados = listaAbonados

    def limpiar(self):
        self.display.delete(0, END)

    def mostrar(self, caracter):
        self.display.insert(END, caracter)
        if caracter == '#': caracter = 'Num'
        elif caracter == '*': caracter = 'Ast'
        mixer.music.load("./sounds/numero" + caracter + ".mp3")
        mixer.music.play()
 
    def crearElementos(self):
        self.display = Entry(self, font=("Arial", 15), borderwidth = 15, relief=FLAT, justify=RIGHT, bg='#090909', fg='#eee')
        self.display.insert(0, "")
        self.display.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)
 
        self.btnLLamar = Button(self, font=("Arial", 12), fg='green', text="[-]", bg='#171717', command=lambda: self.llamar())
        self.btnLLamar.grid(row=1, column=0, sticky="nsew", ipady=5)
        self.btnColgar = Button(self, font=("Arial", 12), fg='red', text="[-]", bg='#171717', command=lambda: self.limpiar())
        self.btnColgar.grid(row=1, column=2, sticky="nsew", ipady=5)
 
        self.btn7 = Button(self, font=("Arial", 12), fg='white', text="7", bg='#171717', command=lambda: self.mostrar("7"))
        self.btn7.grid(row=4, column=0, sticky="nsew", ipady=5)
        self.btn8 = Button(self, font=("Arial", 12), fg='white', text="8", bg='#171717', command=lambda: self.mostrar("8"))
        self.btn8.grid(row=4, column=1, sticky="nsew", ipady=5)
        self.btn9 = Button(self, font=("Arial", 12), fg='white', text="9", bg='#171717', command=lambda: self.mostrar("9"))
        self.btn9.grid(row=4, column=2, sticky="nsew", ipady=5)
 
        self.btn4 = Button(self, font=("Arial", 12), fg='white', text="4", bg='#171717', command=lambda: self.mostrar("4"))
        self.btn4.grid(row=3, column=0, sticky="nsew", ipady=5)
        self.btn5 = Button(self, font=("Arial", 12), fg='white', text="5", bg='#171717', command=lambda: self.mostrar("5"))
        self.btn5.grid(row=3, column=1, sticky="nsew", ipady=5)
        self.btn6 = Button(self, font=("Arial", 12), fg='white', text="6", bg='#171717', command=lambda: self.mostrar("6"))
        self.btn6.grid(row=3, column=2, sticky="nsew", ipady=5)
 
        self.btn1 = Button(self, font=("Arial", 12), fg='white', text="1", bg='#171717', command=lambda: self.mostrar("1"))
        self.btn1.grid(row=2, column=0, sticky="nsew", ipady=5)
        self.btn2 = Button(self, font=("Arial", 12), fg='white', text="2", bg='#171717', command=lambda: self.mostrar("2"))
        self.btn2.grid(row=2, column=1, sticky="nsew", ipady=5)
        self.btn3 = Button(self, font=("Arial", 12), fg='white', text="3", bg='#171717', command=lambda: self.mostrar("3"))
        self.btn3.grid(row=2, column=2, sticky="nsew", ipady=5)
 
        self.btnAst = Button(self, font=("Arial", 12), fg='#CCC', text="*", bg='#171717', command=lambda: self.mostrar("*"))
        self.btnAst.grid(row=5, column=0, sticky="nsew", ipady=5)
        self.btn0 = Button(self, font=("Arial", 12), fg='white', text="0", bg='#171717', command=lambda: self.mostrar("0"))
        self.btn0.grid(row=5, column=1, sticky="nsew", ipady=5)
        self.btnNum = Button(self, font=("Arial", 12), fg='#CCC', text="#", bg='#171717', command=lambda: self.mostrar("#"))
        self.btnNum.grid(row=5, column=2, sticky="nsew", ipady=5)