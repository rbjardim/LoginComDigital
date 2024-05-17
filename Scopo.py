from tkinter import *

# Classe principal da aplicação
class Application:
    def __init__(self, master=None):
        # Define a fonte padrão
        self.fontePadrao = ("Arial", "10")

        # Cria e configura o primeiro container
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        # Cria e configura o segundo container
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        # Cria e configura o terceiro container
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        # Cria e configura o quarto container
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        # Cria e configura o quinto container
        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()

        # Cria e configura o sexto container
        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 20
        self.sextoContainer.pack()

        # Cria o título do formulário
        self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        # Cria o label e campo de entrada para o nome
        self.nomeLabel = Label(self.segundoContainer, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        # Cria o label e campo de entrada para a senha
        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        # Cria o checkbox para lembrar dados (não funcional)
        valor_check = IntVar()
        check = Checkbutton(root, text="Lembrar dados").pack(side=LEFT)

        # Cria o botão de autenticar
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        # Cria o label "OU"
        self.ouLabel = Label(self.quintoContainer, text="OU", font=self.fontePadrao)
        self.ouLabel.pack(side=RIGHT)

        # Cria o botão de autenticação por digital (não funcional)
        self.digital = Button(self.sextoContainer)
        self.digital["text"] = "Digital"
        self.digital["font"] = ("Calibri", "8")
        self.digital["width"] = 12
        self.digital["command"] = self.verificadigital
        self.digital.pack()

        # Cria o label de mensagem
        self.mensagem = Label(self.sextoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    # Método para verificar a senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "ruan.jardim" and senha == "teste01unip":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"

    # Método para verificar a digital (não funcional)
    def verificadigital(self):
        digital = self.nome.get()
        senha = self.senha.get()
        if digital == "ruan.jardim" and senha == "teste01unip":
            self.mensagem["text"] = "Autenticado"
            import main.py as socofing
        else:
            self.mensagem["text"] = "Erro na autenticação"

# Inicializa a aplicação
root = Tk()
Application(root)
root.mainloop()