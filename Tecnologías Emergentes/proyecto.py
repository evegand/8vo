from tkinter import *
from tkinter import filedialog
from datetime import datetime
import math
import locale
import csv

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Combinar Correspondencia")
        self.master.geometry("800x600")
        self.create_menu()
        self.create_table()
        
    def create_menu(self):
        self.menu_bar = Menu(self.master)
        self.master.config(menu=self.menu_bar)
        
        file_menu = Menu(self.menu_bar, tearoff=False)
        file_menu.add_command(label="Abrir archivo de personas", command=self.open_file)
        file_menu.add_command(label="Guardar archivo de personas", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.master.quit)
        
        self.menu_bar.add_cascade(label="Archivo", menu=file_menu)
        
        report_menu = Menu(self.menu_bar, tearoff=False)
        report_menu.add_command(label="Imprimir un oficio", command=self.print_letter)
        report_menu.add_command(label="Imprimir varios oficios", command=self.print_letters)
        report_menu.add_command(label="Imprimir todos los oficios", command=self.print_all_letters)
        
        self.menu_bar.add_cascade(label="Reportes", menu=report_menu)
        
    def create_table(self):
        self.table = Frame(self.master)
        self.table.pack(fill=BOTH, expand=1)
        
        # Table headers
        headers = ["ID", "Nombre", "Apellido 1", "Apellido 2", "Cargo", "Empresa", "Calle", "Número Ext.", "Número Int.", "Colonia", "Municipio", "Estado", "Código Postal", "Teléfono", "Correo Electrónico", "Fecha de Nacimiento", "Edad"]
        for i, header in enumerate(headers):
            label = Label(self.table, text=header, font=("Arial", 12, "bold"))
            label.grid(row=0, column=i, padx=5, pady=5)
        
        # Table data
        self.data = []
        for i in range(50):
            row = [i+1] + [""]*15
            self.data.append(row)
            for j, cell in enumerate(row):
                label = Label(self.table, text=cell, font=("Arial", 12))
                label.grid(row=i+1, column=j, padx=5, pady=5)
        
        # Buttons
        add_button = Button(self.table, text="Agregar", command=self.add_person)
        add_button.grid(row=len(self.data)+1, column=0, padx=5, pady=5)
        
        edit_button = Button(self.table, text="Editar", command=self.edit_person)
        edit_button.grid(row=len(self.data)+1, column=1, padx=5, pady=5)
        
        delete_button = Button(self.table, text="Eliminar", command=self.delete_person)
        delete_button.grid(row=len(self.data)+1, column=2, padx=5, pady=5)