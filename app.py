from abc import ABC, abstractmethod

class ItemBiblioteca(ABC):
    def __init__(self, titulo: str, id_item: int):
        if not titulo or not isinstance(titulo, str):
            raise ValueError("El título debe contener algo.")
        if not isinstance(id_item, int) or id_item <= 0:
            raise ValueError("El ID debe ser un numero positivo.")
        self.titulo = titulo
        self.id_item = id_item
        print(f"📘 Ítem creado: {self.__class__.__name__} - '{self.titulo}' (ID: {self.id_item})")

    @abstractmethod
    def prestar(self, usuario: str) -> str:
        pass

class Libro(ItemBiblioteca):
    def __init__(self, titulo: str, id_item: int, autor: str, paginas: int):
        super().__init__(titulo, id_item)
        if not autor:
            raise ValueError("El autor debe ser una cadena no vacía.")
        if not isinstance(paginas, int) or paginas <= 0:
            raise ValueError("Las páginas deben ser un número entero positivo.")
        self.autor = autor
        self.paginas = paginas
        print(f"   ➤ Libro registrado: {self.titulo} de {self.autor} con {self.paginas} páginas.")


    def prestar(self, usuario: str) -> str:
        mensaje = f"Libro '{self.titulo}' prestado a {usuario}."
        print(f"✔️ {mensaje}")
        return mensaje

    

class Revista(ItemBiblioteca):
    def __init__(self, titulo: str, id_item: int, numero_edicion: int):
        super().__init__(titulo, id_item)
        if not isinstance(numero_edicion, int) or numero_edicion <= 0:
            raise ValueError("El número de edición debe ser un entero positivo.")
        self.numero_edicion = numero_edicion
        print(f"   ➤ Revista registrada: {self.titulo} - Edición {self.numero_edicion}")

    def prestar(self, usuario: str) -> str:
        mensaje = f"Revista '{self.titulo}' edición {self.numero_edicion} prestada a {usuario}."
        print(f"✔️ {mensaje}")
        return mensaje
