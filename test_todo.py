import unittest

class TestGestorTareas(unittest.TestCase):

    def setUp(self):
        self.tareas = []

    def test_agregar_tarea(self):
        titulo = "Estudiar patrones de diseño"
        self.tareas.append({"titulo": titulo, "completada": False})

        self.assertEqual(len(self.tareas), 1)
        self.assertEqual(self.tareas[0]["titulo"], titulo)
        self.assertFalse(self.tareas[0]["completada"])

    def test_completar_tarea(self):
        tarea = {"titulo": "Hacer repositorio en GitHub", "completada": False}
        self.tareas.append(tarea)

        self.tareas[0]["completada"] = True

        self.assertTrue(self.tareas[0]["completada"])

if __name__ == "__main__":
    unittest.main()