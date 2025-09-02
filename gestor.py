from aparato import Aparato

class GestorAparatos:
    def __init__(self, tarifa):
        """
        tarifa: float -> costo por kWh
        """
        self.aparatos = []
        self.tarifa = tarifa

    def agregar_aparato(self, nombre, potencia, horas):
        aparato = Aparato(nombre, potencia, horas)
        self.aparatos.append(aparato)

    def mostrar_reporte(self):
        print("\n📊 REPORTE DE CONSUMO ELÉCTRICO")
        print("-" * 40)

        total_consumo = 0
        total_costo = 0

        # Ordenar aparatos por mayor consumo
        self.aparatos.sort(key=lambda x: x.consumo_kwh(), reverse=True)

        for aparato in self.aparatos:
            consumo = aparato.consumo_kwh()
            costo = aparato.costo(self.tarifa)
            total_consumo += consumo
            total_costo += costo

            print(f"Aparato: {aparato.nombre}")
            print(f"   Consumo: {consumo:.2f} kWh")
            print(f"   Costo: ${costo:.2f}")
            print("-" * 40)

        print(f"\n✅ Consumo Total: {total_consumo:.2f} kWh")
        print(f"💲 Gasto Mensual: ${total_costo:.2f}")
