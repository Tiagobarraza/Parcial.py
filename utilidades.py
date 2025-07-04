import csv
from app import Libro, Revista, ItemBiblioteca

def cargar_items_biblioteca(ruta: str) -> list[ItemBiblioteca]:
    items = []
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            try:
                tipo, titulo, id_ = fila[:3]
                id_item = int(id_)
                if tipo.lower() == 'libro':
                    autor, paginas = fila[3], int(fila[4])
                    items.append(Libro(titulo, id_item, autor, paginas))
                elif tipo.lower() == 'revista':
                    numero_edicion = int(fila[3])
                    items.append(Revista(titulo, id_item, numero_edicion))
            except Exception as e:
                print(f"Error al cargar ítem {fila}: {e}")
    return items

def prestar_items(items: list[ItemBiblioteca], usuario: str) -> list[str]:
    return [item.prestar(usuario) for item in items]

def contar_items(items: list[ItemBiblioteca]) -> dict:
    conteo = {'libro': 0, 'revista': 0}
    for item in items:
        if isinstance(item, Libro):
            conteo['libro'] += 1
        elif isinstance(item, Revista):
            conteo['revista'] += 1
    return conteo

def buscar_por_titulo(items: list[ItemBiblioteca], palabra_clave: str) -> list[ItemBiblioteca]:
    return [item for item in items if palabra_clave.lower() in item.titulo.lower()]
