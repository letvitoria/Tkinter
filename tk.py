import tkinter as tk
import os

#Instanciar a janela
janela = tk.Tk()
janela.title("Primeiro app")
janela.geometry("500x400+20+20") # Largura x Altura + Posição X + Posição Y
#A janela aparece em uma distância de 20 pixels a partir do topo e 20 pixels a partir da esquerda da tela

#Criar e posicionar o label com a mensagem
mensagem = tk.Label(janela, text="Olá Mundo!")
mensagem.pack() #Gerenciador de geometria
#Mudando a cor de fundo 
janela.configure(bg="lightblue")
#Definindo Largura máxima da janela
janela.maxsize(800, 600) # Largura máxima x Altura máxima
janela.minsize(300, 200) # Largura mínima x Altura mínima
#janela.resizable(False,False) #Redimentsionamento de janela desativado
#janela.resizable(True,False) #Redimentsiona a largura, mas altura segue desativado
#janela.state('zoomed') #Define a janela em tela cheia
janela.attributes("-alpha", 0.6) #Define a jenela semitransparente

icon_path = os.path.join(os.path.dirname(__file__), '4-source.ico') #importando icone
janela.iconbitmap(icon_path) #Define o ícone da janela

 #Adicionando o evnto de click para mostrar a outra janela | Significa botão esquerdo do mouse(métdo bind)


#Abrir outra janela ao clicar na janela principal

    


#Exibir a janela
janela.mainloop()