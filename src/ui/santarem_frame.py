import tkinter as tk

def create_santarem_frame(container, show_frame, menu_frame):
    santarem_frame = tk.Frame(container)

    santarem_header = tk.Label(santarem_frame, text="SANTARÉM - OPÇÕES AVANÇADAS", font=("Arial", 14), pady=10)
    santarem_header.pack()

    santarem_option1 = tk.Button(santarem_frame, text="Opção A - Algo diferente", font=("Arial", 12), command=lambda: print("Executando Opção A"))
    santarem_option1.pack(pady=5)

    santarem_option2 = tk.Button(santarem_frame, text="Opção B - Outra coisa", font=("Arial", 12), command=lambda: print("Executando Opção B"))
    santarem_option2.pack(pady=5)

    # Botões de navegação
    btn_back_to_menu = tk.Button(santarem_frame, text="Voltar ao menu principal", font=("Arial", 12), command=lambda: show_frame(menu_frame))
    btn_back_to_menu.pack(pady=20)

    btn_exit_santarem = tk.Button(santarem_frame, text="Sair", font=("Arial", 12), command=lambda: root.destroy() if ask_user_want_to_close() else None)
    btn_exit_santarem.pack(pady=5)

    return santarem_frame