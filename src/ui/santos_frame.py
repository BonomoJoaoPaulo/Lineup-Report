import tkinter as tk

def create_santos_frame(container, show_frame, menu_frame):
    santos_frame = tk.Frame(container)

    santos_header = tk.Label(santos_frame, text="SANTOS - OPÇÕES AVANÇADAS", font=("Arial", 14), pady=10)
    santos_header.pack()

    santos_option1 = tk.Button(santos_frame, text="Opção A - Algo diferente", font=("Arial", 12), command=lambda: print("Executando Opção A"))
    santos_option1.pack(pady=5)

    santos_option2 = tk.Button(santos_frame, text="Opção B - Outra coisa", font=("Arial", 12), command=lambda: print("Executando Opção B"))
    santos_option2.pack(pady=5)

    # Botões de navegação
    btn_back_to_menu = tk.Button(santos_frame, text="Voltar ao menu principal", font=("Arial", 12), command=lambda: show_frame(menu_frame))
    btn_back_to_menu.pack(pady=20)

    btn_exit_santos = tk.Button(santos_frame, text="Sair", font=("Arial", 12), command=lambda: root.destroy() if ask_user_want_to_close() else None)
    btn_exit_santos.pack(pady=5)

    return santos_frame