import tkinter as tk 

janela= tk.Tk()
janela.geometry("500x300")

#Dar funcionalidade para o butão
def clique():
    print("Fazer Login")

janela.title("Janela de Login")
texto = tk.Label(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

butao = tk.Button(janela, text="Login", command=clique) #Ao clicar no botão será imprimido no terminal "Fazer login"
butao.pack(padx=10, pady=10)
janela.mainloop()