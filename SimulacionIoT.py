import os
import random

class Building:
    def __init__(self, x):
        self.floor = x
        self.nfloors = [] # Lista de pisos dentro del edificio [Floor]

    def configurar_edificio(self, x):        
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
        self.nzombies = 0
        self.sensor = Sensor()

    def room_status(self):
        if self.nzombies == 0:
            return self.sensor.change_normal()
        else:
            return self.sensor.change_alert()
    
    def infection(self):
        self.nzombies += 1

class Sensor:
    def __init__(self):
        self.estado = ""

    def change_alert(self):
        self.estado = "Alert"
        return self.estado
    
    def change_normal(self):
        self.estado = "Normal"
        return self.estado

class Simulation:
    def __init__(self):
        self.edificio = Building(0)
        self.infection = False

    def initial_infection(self):
        self.infection = True
        floor = random.choice(self.edificio.nfloors)
        room = random.choice(floor.nrooms)
        room.infection()
        return "La infeccion inicial a comenzado en el piso "+ str(floor.floorid)+ " en la habitacion "+str(room.roomid)
    
    def building_status(self):
        for i in range(len(self.edificio.nfloors)): # Rango de la lista de pisos dentro del edificio
            print("Estado del piso "+str(i))
            for j in range(len(self.edificio.nfloors[i].nrooms)): # Rango de la lista de habitaciones dentro de cada piso
                print("Habitacion numero "+str(j) +" "+ str(self.edificio.nfloors[i].nrooms[j].room_status()))
            pause()
            clear()

def pause():
    programPause = input("Presione cualquier tecla para continuar...")

def clear():
    os.system('cls')

def menu_principal():
    simulation = Simulation()
    print("Bienvenido a la simulacion de apocalipsis zombie dentro de un edificio")
    pause()
    clear()
    print("Despiertas una mañana y ves a traves de tu ventana que la ciudad es un caos, a iniciado un apocalipsis zombie.")
    print("Afortunadamente dispones del sistema de sensores dentro del edificio, lo que te dara una vision de como avanza la infeccion dentro de este.")
    pause()
    clear()
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
                simulation.edificio.configurar_edificio(x)
                clear()
            case 2:
                simulation.building_status()
            case 3:
                if simulation.infection == False:
                    print(simulation.initial_infection())
                else:
                    print("Ya inicio la infeccion que esperas para escapar...")
                pause()
                clear()
            case 4:
                pass
            case 5:
                pass
            
menu_principal()
    