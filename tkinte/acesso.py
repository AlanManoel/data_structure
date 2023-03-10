from tkinter import *


class Janela:
    def __init__(self, top_level):
        self.frame1 = Frame(top_level)
        self.frame1.pack()

        self.frame2 = Frame(top_level)
        self.frame2.pack()

        self.frame3 = Frame(top_level)
        self.frame3.pack()

        self.frame4 = Frame(top_level, pady=10)
        self.frame4.pack()

        Label(self.frame1,text='PASSWORDS', fg='darkblue', font=('Verdana','14','bold'), height=3).pack()
        fonte1=('Verdana','10','bold')

        Label(self.frame2,text='Nome: ', font=fonte1,width=8).pack(side=LEFT)

        self.nome=Entry(self.frame2,width=10,font=fonte1)
        self.nome.focus_force() # Para o foco começar neste campo
        self.nome.pack(side=LEFT)

        Label(self.frame3, text="Senha:", font=fonte1, width=8).pack(side=LEFT)

        self.senha = Entry(self.frame3, width=10, font=fonte1)
        self.senha['show']= '*'
        self.senha.pack(side=LEFT)

        self.entrar = Button(self.frame4, font=fonte1, text='Conferir', bg='pink', command=self.conferir)
        self.entrar.pack()

        self.msg = Label(self.frame4, font=fonte1, height=3, text='Aguardando...')
        self.msg.pack()


    def conferir(self):
        nome= self.nome.get()
        senha = self.senha.get()
        if (nome == senha):
            self.msg['text']= 'Acesso permitido'
            self.msg['fg'] = 'darkgreen'
        else:
            self.msg['text']= 'Acesso negado'
            self.msg['fg']= 'red'
            self.senha.focus_force()


raiz= Tk()
Janela(raiz)
raiz.mainloop()