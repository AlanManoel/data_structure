from tkinter import *
from tkinter import messagebox
from Binary_tree import * 


class Interface_tree_avl:
    def __init__(self):
        self.tree = Binary_tree() #A Arvore binaria

        self.app = Tk() #A Aplicação
        self.app.title('Árvore Binaria')

        self.main_font = ('Times New Roman', 12)

        #Frame que vai conter a arvore binaria
        self.frame_da_tree = Frame(self.app)
        self.frame_da_tree.pack(side=TOP)

        self.title_frame = Label(self.frame_da_tree, text="Árvore Binaria", font=('Times New Roman',15))
        self.title_frame.pack()

        self.canvas = Canvas(self.frame_da_tree, width=1366, height=600)
        self.canvas.pack()

        #Frame das pre ordens
        self.frame_ordens = Frame(self.frame_da_tree)
        self.frame_ordens.pack(side=TOP, pady=(5))

        #Labels de ordens
        self.label_pre_order = Label(self.frame_ordens, text=f'Pré Ordem: {self.tree.pre_order()}')
        self.label_pre_order['font']= self.main_font
        self.label_pre_order.pack(side=LEFT, padx=(0, 20))

        self.label_in_order = Label(self.frame_ordens, text=f'Em Ordem: {self.tree.in_order()}')
        self.label_in_order['font']= self.main_font
        self.label_in_order.pack(side=LEFT, padx=(0, 20))

        self.label_pos_order = Label(self.frame_ordens, text=f'Pós Ordem: {self.tree.post_order()}')
        self.label_pos_order['font']= self.main_font
        self.label_pos_order.pack(side=LEFT)
        
        #Frame que vai conter os botões
        self.frame_botoes = Frame(self.app)
        self.frame_botoes.pack(side=BOTTOM, pady=(0, 5))

        #Opção de adicionar e remover
        self.entrada_number =  Entry(self.frame_botoes, width=30)
        self.entrada_number.pack(side=LEFT, padx=(0, 20))
        
        #Botão de adicionar
        self.botao_add = Button(self.frame_botoes, text="Adicionar", command=self.adicionar, width=10)
        self.botao_add['background'] = 'yellow'
        self.botao_add['font']= self.main_font
        self.botao_add.pack(side=LEFT, padx=(0, 20))

        #Botão de remover
        self.botao_remove = Button(self.frame_botoes, text="Remover", command=self.remover, width=10)
        self.botao_remove['background'] = 'yellow'
        self.botao_remove['font']= self.main_font
        self.botao_remove.pack(side=LEFT, padx=(0, 20))

        #Botão de buscar
        self.botao_buscar = Button(self.frame_botoes, text="Buscar", command=self.buscar, width=10)
        self.botao_buscar['background'] = 'yellow'
        self.botao_buscar['font']= self.main_font
        self.botao_buscar.pack(side=LEFT, padx=(0, 20))

        #Labels de maior e menor numeros
        self.label_maior = Label(self.frame_botoes, text=f"Maior: {self.tree.max_value()}")
        self.label_maior['font']= self.main_font
        self.label_maior.pack(side=LEFT, padx=(0, 20))

        self.label_menor = Label(self.frame_botoes, text=f"Menor: {self.tree.min_value()}")
        self.label_menor['font']= self.main_font
        self.label_menor.pack(side=LEFT, padx=(0, 20))
        
        #Para a aplicação ficar executando direto
        self.app.mainloop() 

    def adicionar(self):
        valor = self.entrada_number.get()
        if (valor != ""): #Se o valor for diferente de vazio
            valores = valor.split(',')
            for numero in valores:
                try:
                    numero = int(numero) #Tratamento de erro, para caso seja digitado letras
                except: #Caso seja digitado letra
                    pass
                else: #Caso não seja letra
                    self.tree.insert(numero)
                    self.atualizar_arvore()
        self.entrada_number.delete(0, END)
   
    def remover(self):
        valor = self.entrada_number.get()
        if (valor != ""):
            try:
                valor = int(valor)
            except:
                messagebox.showinfo("Árvore Binaria", f"Somente número pode ser removido.")
            else:
                if (self.tree.search(valor)):
                    self.tree.remove(valor)
                    self.atualizar_arvore()
                else:
                    messagebox.showinfo("Árvore Binaria", f"O número não existe na árvore.")
                    
        self.entrada_number.delete(0, END)

    def buscar(self):
        valor = self.entrada_number.get()
        if (valor != ""):
            try:
                valor = int(valor)
            except:
                messagebox.showinfo("Árvore Binaria", f"Somente número pode ser buscado.")
            else:
                if (self.tree.search(valor)):
                    self.buscar_numero(self.tree.root, valor, 683, 60, 120)
                else:
                    messagebox.showinfo("Árvore Binaria", f"O número {valor} não está na árvore")
        self.entrada_number.delete(0, END)

    def atualizar_arvore(self):
        self.canvas.delete("all")
        self.label_maior.config(text=f"Maior: {self.tree.max_value()}")
        self.label_menor.config(text=f"Menor: {self.tree.min_value()}")

        self.label_pre_order.config(text=f'Pré Ordem: {self.tree.pre_order()}')
        self.label_in_order.config(text=f'Em Ordem: {self.tree.in_order()}')
        self.label_pos_order.config(text=f'Pós Ordem: {self.tree.post_order()}')

        self.mostrar_arvore(self.tree.root, 683, 60, 120)

    def mostrar_arvore(self, node, x, y, espaco):
        if node:
            self.canvas.create_oval(x-12, y-12, x+12, y+12, fill="yellow")
            self.canvas.create_text(x, y, text=str(node.value), fill="black")            
            if node.left:
                x_left = x - espaco
                y_left = y + 50
                self.canvas.create_line(x, y+12, x_left, y_left-12, arrow=LAST)
                self.mostrar_arvore(node.left, x_left, y_left, espaco//2)

            if node.right:
                x_right = x + espaco
                y_right = y + 50
                self.canvas.create_line(x, y+12, x_right, y_right-12, arrow=LAST)
                self.mostrar_arvore(node.right, x_right, y_right, espaco//2)
    
    def buscar_numero(self, node, valor, x, y, espaco):
        if valor == node.value:
            cor = 'gray'
        else:
            cor = 'yellow'
        if node:
            
            self.canvas.create_oval(x-12, y-12, x+12, y+12, fill=cor)
            self.canvas.create_text(x, y, text=str(node.value), fill="black")
            if node.left:
                x_left = x - espaco
                y_left = y + 50
                self.canvas.create_line(x, y+12, x_left, y_left-12, arrow=LAST)
                self.buscar_numero(node.left, valor, x_left, y_left, espaco//2)

            if node.right:
                x_right = x + espaco
                y_right = y + 50
                self.canvas.create_line(x, y+12, x_right, y_right-12, arrow=LAST)
                self.buscar_numero(node.right, valor, x_right, y_right, espaco//2)

#Iniciando a aplicação
gui = Interface_tree_avl()
