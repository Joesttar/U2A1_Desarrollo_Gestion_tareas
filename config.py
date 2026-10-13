import json
import os

def cargar_tareas():
    #Cargar las tareas desde el archivo JSON al inciar el programa

    if os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_tareas(tareas):
    #Guarda las tareas en el archivo JSON
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)


def mostrar_menu():
    print("\n---Gestor de tareas---")
    print("1. Agregar tarea")
    print("2. Lista tareas")
    print("3. Marcar tarea como completada")
    print("4. Salir")

def main():
    tareas = cargar_tareas()


    class Configuracion:
        _instancia = None
        def __new__(cls):
            if cls._instancia is None:
                cls._instancia = super(Configuracion, cls).__new__(cls)
                cls._instancia.mode_debug = True
            return cls._instancia

config = Configuracion()
if config.mode_debug:
    print("[DEBUG] Aplicacion inciada correctamente")

while True:
    mostrar_menu()
    opcion = input("Elige una opcion")

    while opcion == "1":
        titulo = input("Escribe la descripcion de la tarea: ")
        tareas.append({"titulo": titulo, "completada": False})
        guardar_tareas(tareas)
        print("¡Tarea guardada con exito!")
        break

    while opcion == "2":
        if not tareas:
                print("No hay tareas guardadas.")
        else:
            print("\nLISTA DE TAREAS:")
            for i, t in enumerate(tareas, 1):
                estado = "Completada" if t["completada"] else "Pendiente"
                print(f"{i}. {t['titulo']} - [{estado}]")
        break

    while opcion == "3":
        if not tareas:
                print("No hay tareas para completar.")
        else:
            for i, t in enumerate(tareas, 1):
                print(f"{i}. {t['titulo']}")
            num = int(input("Número de la tarea a completar: "))
            if 0 < num <= len(tareas):
                tareas[num - 1]["completada"] = True
                guardar_tareas(tareas)
                print("¡Tarea marcada como completada!")
            else:
                print("Número inválido.")
        break

    while opcion == "4":
        guardar_tareas(tareas)
        print("Saliendo de la aplicación. ¡Hasta luego!")
        break

    if opcion not in ["1", "2", "3", "4"]:
        print("Opción no válida, intenta de nuevo.")