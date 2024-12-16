import tkinter as tk
from tkinter import messagebox

from utils.general_functions import export_all_data_as_csv, export_all_data_as_json

def ask_user_want_to_close():
    return messagebox.askyesno("Encerrar", "Deseja encerrar o sistema?")

def run_main_menu(paranagua, santarem, santos):
    def handle_option(option):
        if option == 1:
            export_all_data_as_csv(paranagua, santarem, santos)
        elif option == 2:
            export_all_data_as_json(paranagua, santarem, santos)
        elif option == 6:
            if ask_user_want_to_close():
                root.destroy()
        else:
            messagebox.showerror("Erro", "Opção inválida!")

    root = tk.Tk()
    root.title("Lineup de Navios")
    root.geometry("500x300")

    header = tk.Label(root, text="LINEUP DE NAVIOS\nPortos de Paranaguá, Santarém e Santos", font=("Arial", 14), pady=10)
    header.pack()

    btn_csv = tk.Button(root, text="Exportar dados como CSV", font=("Arial", 12), command=lambda: handle_option(1))
    btn_csv.pack(pady=5)

    btn_json = tk.Button(root, text="Exportar dados como JSON", font=("Arial", 12), command=lambda: handle_option(2))
    btn_json.pack(pady=5)

    btn_exit = tk.Button(root, text="Sair", font=("Arial", 12), command=lambda: handle_option(6))
    btn_exit.pack(pady=20)

    footer = tk.Label(root, text="Sistema de Gerenciamento de Navios", font=("Arial", 10), pady=10)
    footer.pack(side=tk.BOTTOM)

    root.mainloop()
