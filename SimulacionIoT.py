import os

class Building:
    def __init__(self, x):
        self.floor = x
        self.nfloors = [] # Lista de pisos dentro del edificio [Floor]

    def configurar_edificio(self, x):        
        #self.floor = x
        for i in range(self.floor, x):
            self.nfloors.append(Floor(i)) # 0 ---> 7
            y = int(input("Ingrese la cantidad de habitaciones para el piso "+str(i)+": "))
            self.nfloors[i].agregar_habitacion(y)        
        self.floor = x

class Floor:
    def __init__(self, x):
        self.floorid = x
        self.nrooms = [] # Lista de habitaciones dentro de cada piso

    def agregar_habitacion(self, y):
        for i in range(len(self.nrooms), y):
            self.nrooms.append(Room(i))

    def visualizar_data(self):
        print(self.room)

class Room:
    def __init__(self, x):
        self.roomid = x
        self.sensor = Sensor()

    def room_state(self):
        return self.sensor.estado

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

def pause():
    programPause = input("Presione cualquier tecla para continuar...")

def clear():
    os.system('cls')

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
        n = int(input())
        clear()
        match(n):
            case 0:
                break
            case 1:
                x = int(input("Ingrese la cantidad de pisos: "))
                edificio.configurar_edificio(x)
                clear()
            case 2:
                for i in range(len(edificio.nfloors)):
                    print("Estado del piso "+str(i))
                    for j in range(len(edificio.nfloors[i].nrooms)):
                        print("Habitacion numero "+str(j) +" "+ str(edificio.nfloors[i].nrooms[j].room_state()))
                    pause()
                    clear()
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            


menu_principal()
    