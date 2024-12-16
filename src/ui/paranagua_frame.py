import tkinter as tk

def create_paranagua_frame(container, show_frame, menu_frame):
    paranagua_frame = tk.Frame(container)

    paranagua_header = tk.Label(paranagua_frame, text="PARANAGUÁ - OPÇÕES AVANÇADAS", font=("Arial", 14), pady=10)
    paranagua_header.pack()

    paranagua_option1 = tk.Button(paranagua_frame, text="Opção A - Algo diferente", font=("Arial", 12), command=lambda: print("Executando Opção A"))
    paranagua_option1.pack(pady=5)

    paranagua_option2 = tk.Button(paranagua_frame, text="Opção B - Outra coisa", font=("Arial", 12), command=lambda: print("Executando Opção B"))
    paranagua_option2.pack(pady=5)

    # Botões de navegação
    btn_back_to_menu = tk.Button(paranagua_frame, text="Voltar ao menu principal", font=("Arial", 12), command=lambda: show_frame(menu_frame))
    btn_back_to_menu.pack(pady=20)

    btn_exit_paranagua = tk.Button(paranagua_frame, text="Sair", font=("Arial", 12), command=lambda: root.destroy() if ask_user_want_to_close() else None)
    btn_exit_paranagua.pack(pady=5)

    return paranagua_frame