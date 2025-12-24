import os

def limpiar_pantalla():
    # Limpia la consola dependiendo del sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def ejecutar_sistema():
    # En Python, en lugar de una matriz fija de [100, 4], 
    # usamos una lista que puede crecer dinámicamente.
    inventario = []
    contador_equipos = 0

    while True:
        print("\n--- SISTEMA DE INVENTARIO DE EQUIPOS DE RED ---")
        print("1. Agregar un Nuevo Equipo")
        print("2. Mostrar Inventario Completo")
        print("3. Buscar el Equipo por Tipo/Marca/Ubicacion")
        print("4. Salir")
        
        opcion = input("Ingrese la opción: ")

        # --- 1. Agregar Nuevo Equipo ---
        if opcion == "1":
            if len(inventario) < 100:
                print("\n--- Agregar Nuevo Equipo ---")
                tipo = input("Ingrese el Tipo (Switch, Router, Firewall, AP): ")
                marca = input("Ingrese la Marca: ")
                ubicacion = input("Ingrese la Ubicación (Edificio/Sala): ")
                
                contador_equipos += 1
                # Creamos un diccionario para representar el equipo
                nuevo_equipo = {
                    "id": str(contador_equipos),
                    "tipo": tipo,
                    "marca": marca,
                    "ubicacion": ubicacion
                }
                inventario.append(nuevo_equipo)
                print(f"✅ Equipo agregado con ID: {nuevo_equipo['id']}")
            else:
                print("❌ El inventario está lleno (máximo 100 equipos).")

        # --- 2. Mostrar Inventario Completo ---
        elif opcion == "2":
            print("\n--- INVENTARIO DE EQUIPOS DE RED ---")
            if inventario:
                for equipo in inventario:
                    print(f"ID: {equipo['id']} | Tipo: {equipo['tipo']} | Marca: {equipo['marca']} | Ubicación: {equipo['ubicacion']}")
            else:
                print("⚠️ El inventario está vacío.")

        # --- 3. Buscar Equipo ---
        elif opcion == "3":
            print("\n--- Buscar Equipo ---")
            termino = input("Ingrese término de búsqueda (Tipo, Marca o Ubicación): ").lower()
            encontrado = False
            
            print("--- Resultados de Búsqueda ---")
            for equipo in inventario:
                # Comparamos convirtiendo a minúsculas para facilitar la búsqueda
                if (termino in equipo['tipo'].lower() or 
                    termino in equipo['marca'].lower() or 
                    termino in equipo['ubicacion'].lower()):
                    
                    print(f"ID: {equipo['id']} | Tipo: {equipo['tipo']} | Marca: {equipo['marca']} | Ubicación: {equipo['ubicacion']}")
                    encontrado = True
            
            if not encontrado:
                print(f"No se encontraron equipos que coincidan con '{termino}'.")

        # --- 4. Salir ---
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta Luego! 👋")
            break

        # --- Opción Inválida ---
        else:
            print("❌ Opción no válida. Intente de nuevo.")

        input("\nPresione Enter para continuar...")
        limpiar_pantalla()

if __name__ == "__main__":
    ejecutar_sistema()