from gestor import GestorAparatos

def main():
    print("💡 Sistema de Control de Gasto Eléctrico\n")

    tarifa = float(input("Ingrese la tarifa eléctrica en $/kWh: "))
    gestor = GestorAparatos(tarifa)

    while True:
        nombre = input("\nNombre del aparato (o 'salir' para terminar): ")
        if nombre.lower() == "salir":
            break

        potencia = float(input("Potencia del aparato en Watts: "))
        horas = float(input("Horas de uso al mes: "))

        gestor.agregar_aparato(nombre, potencia, horas)

    gestor.mostrar_reporte()

if __name__ == "__main__":
    main()
