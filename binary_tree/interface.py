from tkinter import *
from Binary_tree import *



class Interface_binary_tree:
    def __init__(self):
        self.tree = Binary_AVL() #A Arvore binaria

        self.app = Tk() #A Aplicação
        self.app.title('Árvore Binaria AVL')

        #Frame que vai conter a arvore binaria
        self.frame_da_tree = Frame(self.app)
        self.frame_da_tree.pack(side=LEFT)

        self.title_frame = Label(self.frame_da_tree, text="Árvore Binaria AVL")
        self.title_frame.pack()

        self.canvas = Canvas(self.frame_da_tree, width=966, height=600)
        self.canvas.pack()

        #Frame que vai conter os botões
        self.frame_botoes = Frame(self.app)
        self.frame_botoes.pack(side=RIGHT)

        #Opção de adicionar
        self.entrada_add =  Entry(self.frame_botoes)
        self.entrada_add.pack(padx=50)
        
        self.botao_add = Button(self.frame_botoes, text="Adicionar", command=self.adicionar)
        self.botao_add.pack(pady=5)

        #Opção de Remover
        self.entrada_remove =  Entry(self.frame_botoes)
        self.entrada_remove.pack(padx=50)

        self.botao_remove = Button(self.frame_botoes, text="Remover", command=self.remover)
        self.botao_remove.pack()

        self.app.mainloop() #Para a aplicação ficar executando direto

    def adicionar(self):
        valor = self.entrada_add.get()
        if (valor != ""):
            valor = int(valor)
            self.tree.insert(valor)
            self.atualizar_arvore()
        self.entrada_add.delete(0, END)

    def remover(self):
        valor = self.entrada_remove.get()
        if (valor != ""):
            valor = int(valor)
            self.tree.remove(valor)
            self.atualizar_arvore()
        self.entrada_remove.delete(0, END)

    def atualizar_arvore(self):
        self.canvas.delete("all")
        self.mostrar_arvore(self.tree.root, 483, 60, 50)

    def mostrar_arvore(self, node, x, y, espaco):
        if node:
            self.canvas.create_oval(x-12, y-12, x+12, y+12, fill="yellow")
            self.canvas.create_text(x, y, text=str(node.value), fill="black")

            if node.left:
                x_left = x - (espaco)
                y_left = y + 50
                self.canvas.create_line(x, y+12, x_left, y_left-12, arrow=LAST)
                self.mostrar_arvore(node.left, x_left, y_left, espaco//2)

            if node.right:
                x_right = x + (espaco)
                y_right = y + 50
                self.canvas.create_line(x, y+12, x_right, y_right-12, arrow=LAST)
                self.mostrar_arvore(node.right, x_right, y_right, espaco//2)



#Iniciando a aplicação
gui = Interface_binary_tree()
