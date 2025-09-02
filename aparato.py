class Aparato:
    def __init__(self, nombre, potencia, horas):
        
        self.nombre = nombre
        self.potencia = potencia
        self.horas = horas

    def consumo_kwh(self):
     
        return (self.potencia * self.horas) / 1000

    def costo(self, tarifa):
        
        return self.consumo_kwh() * tarifa
