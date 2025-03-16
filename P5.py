import tkinter as tk
from tkinter import filedialog, simpledialog, colorchooser

# Crear la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Editor de Texto Básico")
ventana.geometry("800x600")  # Establecer un tamaño de ventana predeterminado

# Crear un cuadro de texto donde el usuario puede ingresar texto
texto = tk.Text(ventana)
texto.pack(fill=tk.BOTH, expand=True)

# Crear una barra de menú para la aplicación
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Definir una función para abrir un archivo
def abrir_archivo():
    archivo = filedialog.askopenfilename(title="Abrir archivo", filetypes=[("Archivos de texto", "*.txt")])
    if archivo:  # Comprobar si el usuario seleccionó un archivo
        with open(archivo, "r") as f:
            contenido = f.read()
            texto.delete(1.0, tk.END)  # Limpiar el cuadro de texto
            texto.insert(tk.END, contenido)  # Insertar el contenido en el cuadro de texto

# Definir una función para guardar un archivo
def guardar_archivo():
    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if archivo:  # Comprobar si el usuario seleccionó un archivo
        with open(archivo, "w") as f:
            f.write(texto.get(1.0, tk.END))  # Guardar el contenido del cuadro de texto

# Definir una función para borrar el contenido del cuadro de texto
def borrar_texto():
    texto.delete("1.0", tk.END)

# Definir una función para cambiar el color del texto
def cambiar_color():
    color = colorchooser.askcolor()[1]  # Obtener el color seleccionado
    if color:  # Si el usuario seleccionó un color
        texto.tag_configure("colortexto", foreground=color)  # Establecer el color del texto
        texto.tag_add("colortexto", "1.0", tk.END)  # Aplicar el color a todo el texto

# Definir una función para buscar y reemplazar texto
def buscar_reemplazar():
    buscar = simpledialog.askstring("Buscar", "Introduce el texto a buscar:")
    if buscar:
        reemplazar = simpledialog.askstring("Reemplazar", "Introduce el texto para reemplazar:")
        if reemplazar is not None:
            contenido = texto.get(1.0, tk.END)  # Obtener el contenido del cuadro de texto
            nuevo_contenido = contenido.replace(buscar, reemplazar)  # Reemplazar el texto
            texto.delete(1.0, tk.END)  # Limpiar el cuadro de texto
            texto.insert(tk.END, nuevo_contenido)  # Insertar el nuevo contenido

# Definir la función principal de la aplicación
def main():
    # Crear un menú para operaciones de archivos
    menu_archivo = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
    # Añadir comandos al menú de archivos
    menu_archivo.add_command(label="Abrir", command=abrir_archivo, accelerator="Ctrl+A")
    menu_archivo.add_command(label="Guardar", command=guardar_archivo, accelerator="Ctrl+G")
    menu_archivo.add_command(label="Borrar", command=borrar_texto, accelerator="Ctrl+E")

    # Crear un menú para operaciones de edición
    menu_edicion = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Edición", menu=menu_edicion)
    # Añadir comandos al menú de edición
    menu_edicion.add_command(label="Color del texto", command=cambiar_color)
    menu_edicion.add_command(label="Buscar y reemplazar", command=buscar_reemplazar, accelerator="Ctrl+B")

    # Vincular accesos directos de teclado a las funciones correspondientes
    ventana.bind("<Control-a>", lambda event: abrir_archivo())
    ventana.bind("<Control-g>", lambda event: guardar_archivo())
    ventana.bind("<Control-e>", lambda event: borrar_texto())
    ventana.bind("<Control-b>", lambda event: buscar_reemplazar())

    # Iniciar el bucle principal de eventos de la aplicación
    ventana.mainloop()

# Comprobar si este script se está ejecutando directamente (no se está importando)
if __name__ == "__main__":
    # Llamar a la función principal para iniciar la aplicación
    main()
