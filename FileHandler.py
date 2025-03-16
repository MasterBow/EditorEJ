import os

class FileHandler:
    def __init__(self, filepath):
        """
        Inicializa el FileHandler con la ruta del archivo.

        Args:
            filepath (str): La ruta al archivo que se va a manipular.
        """
        self.filepath = filepath

    def abrir(self, mode='r'):
        """
        Abre el archivo en el modo especificado.

        Args:
            mode (str): Modo de apertura del archivo ('r' para lectura, 'w' para escritura, 'a' para añadir, etc.).
                       Por defecto es 'r' (lectura).

        Returns:
            file object: Objeto de archivo si la apertura es exitosa, None si falla.
            str: Mensaje de error en caso de fallo.
        """
        try:
            self.file = open(self.filepath, mode)
            return self.file, None  # Retorna el objeto de archivo y None para indicar que no hay error
        except FileNotFoundError:
            return None, f"Error: El archivo '{self.filepath}' no fue encontrado."
        except Exception as e:
            return None, f"Error al abrir el archivo '{self.filepath}': {e}"

    def guardar(self, contenido, mode='w'):
        """
        Guarda el contenido en el archivo. Sobrescribe el archivo si existe en modo 'w'.

        Args:
            contenido (str): El contenido a guardar en el archivo.
            mode (str): Modo de escritura ('w' para escribir, 'a' para añadir). Por defecto es 'w'.

        Returns:
            bool: True si la operación de guardado es exitosa, False si falla.
            str: Mensaje de error en caso de fallo.
        """
        try:
            with open(self.filepath, mode) as f: # Usamos 'with' para asegurar que el archivo se cierra correctamente
                f.write(contenido)
            return True, None # Retorna True y None para indicar que no hay error
        except Exception as e:
            return False, f"Error al guardar en el archivo '{self.filepath}': {e}"


    def editar_contenido(self, nuevo_contenido):
        """
        Edita el contenido del archivo reemplazando todo el contenido existente.

        Args:
            nuevo_contenido (str): El nuevo contenido para el archivo.

        Returns:
            bool: True si la edición es exitosa, False si falla.
            str: Mensaje de error en caso de fallo.
        """
        return self.guardar(nuevo_contenido, mode='w') # Reutilizamos la función guardar con modo 'w' para editar


    def eliminar(self):
        """
        Elimina el archivo.

        Returns:
            bool: True si la eliminación es exitosa, False si falla.
            str: Mensaje de error en caso de fallo.
        """
        try:
            os.remove(self.filepath)
            return True, None # Retorna True y None para indicar que no hay error
        except FileNotFoundError:
            return False, f"Error: El archivo '{self.filepath}' no fue encontrado."
        except Exception as e:
            return False, f"Error al eliminar el archivo '{self.filepath}': {e}"