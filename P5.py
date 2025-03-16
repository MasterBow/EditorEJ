import tkinter as tk
from FileHandler import FileHandler
from tkinter import filedialog, simpledialog, colorchooser, messagebox
import os


# Crear la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Editor de Texto Básico")
ventana.geometry("800x600")

# Crear un cuadro de texto donde el usuario puede ingresar texto
texto = tk.Text(ventana)
texto.pack(fill=tk.BOTH, expand=True)

# Crear una barra de menú para la aplicación
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Variable para almacenar la instancia de FileHandler
archivo_handler = None
current_filepath = None

# Definir una función para abrir un archivo
def abrir_archivo():
    global archivo_handler, current_filepath
    archivo_path = filedialog.askopenfilename(title="Abrir archivo", filetypes=[("Archivos de texto", "*.txt")])
    if archivo_path:
        encoding = simpledialog.askstring("Codificación", "Introduce la codificación del archivo (por defecto utf-8):") or 'utf-8'
        archivo_handler = FileHandler(archivo_path, encoding=encoding)
        current_filepath = archivo_path
        contenido, error = archivo_handler.abrir()
        if contenido is not None:
            texto.delete(1.0, tk.END)
            texto.insert(tk.END, contenido)
            ventana.title(f"Editor de Texto Básico - {os.path.basename(archivo_path)}")
        else:
            messagebox.showerror("Error", error)

# Definir una función para guardar un archivo
def guardar_archivo():
    global archivo_handler, current_filepath
    if current_filepath:
        if archivo_handler is None:
            encoding = simpledialog.askstring("Codificación", "Introduce la codificación del archivo (por defecto utf-8):") or 'utf-8'
            archivo_handler = FileHandler(current_filepath, encoding=encoding)
        contenido_a_guardar = texto.get(1.0, tk.END)
        exito, error = archivo_handler.guardar(contenido_a_guardar)
        if not exito:
            messagebox.showerror("Error", error)
    else:
        guardar_como_archivo()

def guardar_como_archivo():
    global archivo_handler, current_filepath
    archivo_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if archivo_path:
        encoding = simpledialog.askstring("Codificación", "Introduce la codificación del archivo (por defecto utf-8):") or 'utf-8'
        archivo_handler = FileHandler(archivo_path, encoding=encoding)
        current_filepath = archivo_path
        contenido_a_guardar = texto.get(1.0, tk.END)
        exito, error = archivo_handler.guardar(contenido_a_guardar)
        if exito:
            ventana.title(f"Editor de Texto Básico - {os.path.basename(archivo_path)}")
        else:
            messagebox.showerror("Error", error)
def borrar_texto():
    texto.delete(1.0, tk.END)

def cambiar_color():
    color = colorchooser.askcolor(title="Seleccionar color del texto")[1]
    if color:
        texto.config(fg=color)

def buscar_reemplazar():
    def buscar_reemplazar_texto():
        texto_buscar = entry_buscar.get()
        texto_reemplazar = entry_reemplazar.get()
        contenido = texto.get(1.0, tk.END)
        contenido = contenido.replace(texto_buscar, texto_reemplazar)
        texto.delete(1.0, tk.END)
        texto.insert(tk.END, contenido)

    ventana_buscar_reemplazar = tk.Toplevel(ventana)
    ventana_buscar_reemplazar.title("Buscar y reemplazar")

    label_buscar = tk.Label(ventana_buscar_reemplazar, text="Buscar:")
    label_buscar.pack()
    entry_buscar = tk.Entry(ventana_buscar_reemplazar)
    entry_buscar.pack()

    label_reemplazar = tk.Label(ventana_buscar_reemplazar, text="Reemplazar:")
    label_reemplazar.pack()
    entry_reemplazar = tk.Entry(ventana_buscar_reemplazar)
    entry_reemplazar.pack()

    boton_buscar_reemplazar = tk.Button(ventana_buscar_reemplazar, text="Buscar y reemplazar", command=buscar_reemplazar_texto)
    boton_buscar_reemplazar.pack()

    ventana_buscar_reemplazar = tk.Toplevel(ventana)
    ventana_buscar_reemplazar.title("Buscar y reemplazar")

    label_buscar = tk.Label(ventana_buscar_reemplazar, text="Buscar:")
    label_buscar.pack()
    entry_buscar = tk.Entry(ventana_buscar_reemplazar)
    entry_buscar.pack()

    label_reemplazar = tk.Label(ventana_buscar_reemplazar, text="Reemplazar:")
    label_reemplazar.pack()
    entry_reemplazar = tk.Entry(ventana_buscar_reemplazar)
    entry_reemplazar.pack()

    boton_buscar_reemplazar = tk.Button(ventana_buscar_reemplazar, text="Buscar y reemplazar", command=buscar_reemplazar)
    boton_buscar_reemplazar.pack()

# Definir la función principal de la aplicación
def main():
    # Crear un menú para operaciones de archivos
    menu_archivo = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
    # Añadir comandos al menú de archivos
    menu_archivo.add_command(label="Abrir", command=abrir_archivo, accelerator="Ctrl+A")
    menu_archivo.add_command(label="Guardar", command=guardar_archivo, accelerator="Ctrl+G")
    menu_archivo.add_command(label="Guardar como...", command=guardar_como_archivo)
    menu_archivo.add_separator()
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

# Llamar a la función principal para iniciar la aplicación
if __name__ == "__main__":
    main()