from tkinter import *


class Janela:
    def __init__(self, top_level):
        self.fr1 = Frame(top_level)
        self.fr1.pack()

        self.titulo = Label(self.fr1)
        self.titulo['text'] = 'GOOGLE TRADUTOR'
        self.titulo['font'] = ('Verdana', '12', 'italic', 'bold')
        self.titulo.pack()

        self.label = Label(self.fr1)
        self.label['text'] = 'Clique para traduzir para português'
        self.label['font'] = ('Verdana', '10', 'italic')
        self.label['width'] = 30
        self.label.pack()


        # self.botao = Button(self.fr1, text='Olá mundo', background= 'gray',foreground= 'white', font= ('Verdana', '10', 'italic', 'bold'), height= 3)
        #Ou
        self.botao = Button(self.fr1)
        self.botao['text'] = 'Hello World!' #Definição de texto
        self.botao['background'] = 'gray' #definição da cor do botão
        self.botao['foreground'] = 'white' #definção da cor da letra do botão
        self.botao['font'] = ('Verdana', '10', 'italic', 'bold') #Definição da fonte--tamanho--tipo
        self.botao['height'] = 1 #Definição da altura do botão
        self.botao['width'] = 10 #Definição da largura do botão
        self.botao.bind('<Button-1>', self.traduzir) #Definição do evento ao clicar no botão esquerdo
        self.botao.pack()


    def traduzir(self, event):
        if (self.botao['text'] == 'Hello World!'):
            self.label['text'] = 'Clique para traduzir para o inglês.'
            self.botao['text'] = 'Olá Mundo!'
        else:
            self.botao['text'] = 'Hello World!'
            self.label['text'] = 'Clique para traduzir para português.'

raiz = Tk()
Janela(raiz)
raiz.mainloop()
