import unittest
import tempfile
import os
from app import Libro, Revista
from utilidades import (
    cargar_items_biblioteca,
    prestar_items,
    contar_items,
    buscar_por_titulo
)

class TestBiblioteca(unittest.TestCase):

    def test_libro_valido(self):
        libro = Libro("Libro de Prueba", 1, "Autor X", 100)
        self.assertEqual(libro.prestar("Lucía"), "Libro 'Libro de Prueba' prestado a Lucía.")

    def test_libro_invalido(self):
        with self.assertRaises(ValueError):
            Libro("", 1, "Autor", 100)
        with self.assertRaises(ValueError):
            Libro("Título", -5, "Autor", 100)
    
    def test_revista_valida(self):
        revista = Revista("Ciencia", 2, 34)
        self.assertEqual(revista.prestar("Pedro"), "Revista 'Ciencia' edición 34 prestada a Pedro.")

    def test_revista_invalida(self):
        with self.assertRaises(ValueError):
            Revista("Revista", 3, 0)

    def test_prestar_items(self):
        items = [
            Libro("L1", 1, "A1", 123),
            Revista("R1", 2, 10)
        ]
        resultados = prestar_items(items, "Ana")
        self.assertEqual(resultados[0], "Libro 'L1' prestado a Ana.")
        self.assertEqual(resultados[1], "Revista 'R1' edición 10 prestada a Ana.")

    def test_contar_items(self):
        items = [
            Libro("Libro A", 1, "Autor A", 111),
            Libro("Libro B", 2, "Autor B", 222),
            Revista("Revista X", 3, 55)
        ]
        self.assertEqual(contar_items(items), {'libro': 2, 'revista': 1})

    def test_buscar_por_titulo(self):
        items = [
            Libro("Cien Años de Soledad", 1, "Gabriel G.", 500),
            Revista("Ci2encia Hoy", 2, 23)
        ]
        resultado = buscar_por_titulo(items, "cien")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0].titulo, "Cien Años de Soledad")

    def test_cargar_items_biblioteca(self):
        contenido = """libro,Libro Prueba,10,Autor Z,300
revista,Revista Prueba,20,5
libro,Libro Malo,error,Autor B,200
"""
       
        # Crea un archivo temporal     
        with tempfile.NamedTemporaryFile('w+', delete=False) as tmp:
            tmp.write(contenido)
            tmp.seek(0)
            tmp.close()
           
           # Carga items y borra el archivo temporal
            items = cargar_items_biblioteca(tmp.name)
            os.remove(tmp.name)
            self.assertEqual(len(items), 2)
            self.assertIsInstance(items[0], Libro)
            self.assertIsInstance(items[1], Revista)

if __name__ == '__main__':
    unittest.main()