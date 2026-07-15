#ACT3, Herencia
# Ejemplo básico de POO en Python
#Conceptos aplicados: clase, atributos, instanciación, metodos y constructores

class Termo:   #clase: Termo
    # Constructor: se ejecuta al crear un objeto
    #Definición de atributos
    def __init__(self, color, capacidad):  
        self.color = color          # atributo
        self.capacidad = capacidad  # atributo
        self.contenido = 0          # estado inicial

    # Método: es la acción que puede realizar el objeto
    def llenar(self, cantidad):
        #Se verifica que la cantidad no exceda la capacidad
        if cantidad <= self.capacidad:
            self.contenido = cantidad
            print(f"El termo se llenó con {cantidad} ml.")
        else:
            print("La cantidad excede la capacidad del termo.")

    # Método para beber del termo
    def beber(self, cantidad):
        #Se verifica que haya sufiente contenido
        if cantidad <= self.contenido:
            self.contenido -= cantidad
            print(f"Bebiste {cantidad} ml. Quedan {self.contenido} ml.")
        else:
            print("No hay suficiente contenido en el termo.")

#clase derivada 1
class TermoInteligente(Termo):
    def mostrarTemperatura(self):
        print("La bebida está a 15°C.")


#Clase derivada 2
class TermoDeViaje(Termo):
    def bloquearTapa(self):
        print("La tapa esta bloqueada para evitar derrames.")

# Crear un objeto (instancia) de la clase Termo
mi_termo = Termo("Azul", 500)

# Uso de los métodos
mi_termo.llenar(400) #El termo lo llenamos con 400 ml
mi_termo.beber(150)   #bebemos 150 ml

# crear una clase (instancia) derivada de la clase termo
mi_termo_inteligente = TermoInteligente("Rojo", 500)

# Uso de los metodos heredados y nuevos
mi_termo_inteligente.llenar(400)
mi_termo_inteligente.beber(150)
mi_termo_inteligente.mostrarTemperatura()

# crear una clase (instancia) derivada de la clase termo
mi_termo_viaje = TermoDeViaje("Rosado", 500)

# Uso de los metodos heredados y nuevos
mi_termo_viaje.llenar(400)
mi_termo_viaje.beber(150)
mi_termo_viaje.bloquearTapa()