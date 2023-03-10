from lista import *
from tkinter import *


class Janela:
    def __init__(self, top_level):
        self.lista = lista()  
        self.frame_1 = Frame(top_level)
        self.frame_1.pack()

        self.frame_2 = Frame(top_level)
        self.frame_2.pack()

        self.frame_3 = Frame(top_level)
        self.frame_3.pack()

        self.titulo = Label(self.frame_1, text="Lista encadeada", font=('Verdana', '12', 'bold', 'italic' ))
        self.titulo.pack()

        self.mostrar_lista = Label(self.frame_1, text=self.lista, font=('Verdana', '8', 'bold'))
        self.mostrar_lista.pack()


        self.txt_elemento = Label(self.frame_2,text="Elemento: ")
        self.txt_elemento.pack(side=LEFT)
        self.elemento = Entry(self.frame_2)
        self.elemento.focus_force()
        self.elemento.pack(side=LEFT)

        self.botao_adicionar = Button(self.frame_3, text="Adicionar no final", command=self.append)
        self.botao_adicionar.pack(side=LEFT)

        self.excluir_ultimo = Button(self.frame_3, text="Remover no final", command=self.pop)
        self.excluir_ultimo.pack(side=LEFT)

        self.remover_elemento = Button(self.frame_3, text="Remover elemento", command=self.remove)
        self.remover_elemento.pack(side=LEFT)

    def append(self):
        if (self.elemento.get() != ""):
            self.lista.append(self.elemento.get())
            self.mostrar_lista['text'] = self.lista
            self.elemento.select_clear()
    def pop(self):
        self.lista.pop()
        self.mostrar_lista['text'] = self.lista
    def remove(self):
        self.lista.remove(self.elemento.get())
        self.mostrar_lista['text'] = self.lista



raiz= Tk()
Janela(raiz)
raiz.mainloop()