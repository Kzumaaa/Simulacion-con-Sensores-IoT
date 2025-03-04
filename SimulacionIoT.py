class Building:
    def __init__(self, x):
        self.floor = x
        self.nfloors = [] # Lista de pisos dentro del edificio [Floor]
    
    def agregar_piso(self, x):
        floor_x = []
        self.nfloors.append(floor_x)

    def configurar_edificio(self, x):        
        self.floor = x
        for i in range(x):
            self.nfloors.append(Floor(i))

class Floor:
    def __init__(self, x):
        self.room = x
        self.nrooms = [] # Lista de habitaciones dentro de cada piso

    def agregar_habitacion(self, room):
        self.nrooms.append(room)

    def visualizar_data(self):
        print(self.room)

class Room:
    def __init__(self):
        self.sensor = Sensor

class Sensor:
    def __init__(self):
        self.estado = "Normal"

    def cambio_estado_alert(self):
        self.estado = "Alert"
    
    def cambio_estado_normal(self):
        self.estado = "Normal"

class Simulation:
    def __init__(self):
        pass

def menu_principal():
    edificio = Building(0)
    while True:
        print("Ingrese una opcion")
        print("1. Configurar edificio")
        print("2. Ver estado del edificio")
        print("3. Avanzar simulacion")
        print("4. Limpiar habitacion")
        print("5. Bloquear habitacion")
        print("0. Salir")
        n = input()
        match(int(n)):
            case 0:
                break
            case 1:
                x = input("Ingrese la cantidad de pisos: ")
                edificio.configurar_edificio(int(x))
                #for i in range(int(x)):
                    #y = input("Ingrese la cantidad de habitaciones para el piso "+str(i)+": ")
                    #edificio.agregar_piso(int(y))

                pass
            case 2:
                #print(edificio.nfloors[4])
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            


menu_principal()
    