import customtkinter

janela = customtkinter.CTk()
janela.geometry("500x300")
janela.title("Tela de Login")
# --- FUNÇÕES DE NAVEGAÇÃO ---
def ir_para_sucesso():
    frame_login.pack_forget()  # Esconde a tela de login
    frame_sucesso.pack(pady=20, padx=20, fill="both", expand=True) # Mostra a de sucesso

def voltar_para_login():
    frame_sucesso.pack_forget() # Esconde a tela de sucesso
    frame_login.pack(pady=20, padx=20, fill="both", expand=True) # Mostra a de login

# --- TELA DE LOGIN (FRAME 1) ---f
frame_login = customtkinter.CTkFrame(janela)
frame_login.pack(pady=20, padx=20, fill="both", expand=True)

texto = customtkinter.CTkLabel(frame_login, text="Fazer Login")
texto.pack(pady=10)

email = customtkinter.CTkEntry(frame_login, placeholder_text="Digite seu email")
email.pack(pady=10)

senha = customtkinter.CTkEntry(frame_login, placeholder_text="Digite sua senha", show="*") #Show define que só aparecerá * na senha 
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(frame_login, text="Lembrar de mim")
checkbox.pack(padx=10, pady=10)

botao_login = customtkinter.CTkButton(frame_login, text="Login", command=ir_para_sucesso)
botao_login.pack(pady=10)

# --- TELA DE SUCESSO (FRAME 2) ---
# Criamos, mas NÃO damos .pack() ainda, então ele começa escondido
frame_sucesso = customtkinter.CTkFrame(janela)

texto_sucesso = customtkinter.CTkLabel(frame_sucesso, text="Login Efetuado com Sucesso!", text_color="green")
texto_sucesso.pack(pady=20)

botao_voltar = customtkinter.CTkButton(frame_sucesso, text="Voltar", command=voltar_para_login)
botao_voltar.pack(pady=10)

janela.mainloop()