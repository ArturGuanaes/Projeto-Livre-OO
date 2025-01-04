import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        
        # Configuração da interface
        self.entrada = tk.Entry(root, width=30, borderwidth=5, font=("Arial", 14))
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Botões
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0), ('Sair', 5, 1, 4)
        ]
        
        for texto, linha, coluna, *largura in botoes:
            comando = lambda t=texto: self.click_botao(t)
            largura = largura[0] if largura else 1
            botao = tk.Button(root, text=texto, padx=20, pady=20, width=largura * 4, command=comando, font=("Arial", 12))
            botao.grid(row=linha, column=coluna, columnspan=largura)
    
    def click_botao(self, valor):
        if valor == "C":
            self.entrada.delete(0, tk.END)
        elif valor == "=":
            self.calcular()
        elif valor == "Sair":
            self.root.quit()
        else:
            self.entrada.insert(tk.END, valor)
    
    def calcular(self):
        try:
            expressao = self.entrada.get()
            resultado = eval(expressao)
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, str(resultado))
        except Exception as e:
            messagebox.showerror("Erro", "Expressão inválida!")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
