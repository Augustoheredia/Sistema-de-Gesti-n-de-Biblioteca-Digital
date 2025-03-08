class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {len(self.libros_prestados)}"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # ISBN: Libro
        self.usuarios = set()  # IDs de usuario únicos
        self.registros_usuarios = {} # ID: Usuario

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' agregado con éxito.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            self.registros_usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado con éxito.")
        else:
            print("ID de usuario ya existe.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)
            del self.registros_usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.registros_usuarios[id_usuario]
            libro = self.libros[isbn]
            if libro not in usuario.libros_prestados:
                usuario.libros_prestados.append(libro)
                print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
            else:
                print("El usuario ya tiene este libro prestado.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.registros_usuarios[id_usuario]
            libro = self.libros[isbn]
            if libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(libro)
                print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
            else:
                print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario o libro no encontrado.")

    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.autor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.registros_usuarios[id_usuario]
            return usuario.libros_prestados
        else:
            return None


# Ejemplo de uso
biblioteca = Biblioteca()

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "9780061120084")
libro2 = Libro("1984", "George Orwell", "Ciencia ficción", "9780451524935")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

usuario1 = Usuario("Juan Pérez", "JP123")
usuario2 = Usuario("María García", "MG456")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

biblioteca.prestar_libro("JP123", "9780061120084")
biblioteca.prestar_libro("MG456", "9780451524935")

print("\nLibros prestados a Juan:")
for libro in biblioteca.listar_libros_prestados("JP123"):
    print(libro)

print("\nBúsqueda de libros de ciencia ficción:")
for libro in biblioteca.buscar_libros("categoria", "ciencia ficción"):
    print(libro)

biblioteca.devolver_libro("JP123", "9780061120084")
biblioteca.dar_baja_usuario("MG456")