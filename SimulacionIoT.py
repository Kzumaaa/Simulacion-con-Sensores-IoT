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
        self.bloqueo = False

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

    def initial_infection(self): # Funcion de un solo uso donde se escoge un piso aleatorio y una habitacion aleatoria para simular la infeccion inicial
        self.infection = True
        floor = random.choice(self.edificio.nfloors)
        room = random.choice(floor.nrooms)
        room.infection()
        return "La infeccion inicial a comenzado en el piso "+ str(floor.floorid)+ " en la habitacion "+str(room.roomid)
    
    def infeccion_continua(self): # Funcion de propagacion de zombies
        val_ady = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Lista de posiciones adyacentes a un punto
        random.shuffle(val_ady)
        for i in range(len(self.edificio.nfloors)): # Rango de la lista de pisos dentro del edificio
            for j in range(len(self.edificio.nfloors[i].nrooms)): # Rango de la lista de habitaciones dentro de cada piso
                if self.edificio.nfloors[i].nrooms[j].nzombies >= 1: # Cantidad de zombies dentro de la habitacion >= 1
                    for dx, dy in val_ady: # Posicion de habitaciones adyacentes a la que tiene zombies (arriba, abajo, izquiera y derecha)
                        x, y = i + dx, j + dy # Habitaciones adyacentes a la que tiene zombies (arriba, abajo, izquiera y derecha)
                        if x >= 0 and y >= 0:
                            try: # Manejo de error en caso de que se llegue a un valor inexistente en la lista de pisos y habitaciones
                                if random.random() < 0.5 and self.edificio.nfloors[x].nrooms[y].bloqueo != True: # 50% de que los zombies se propaguen a otras habitaciones
                                    if self.edificio.nfloors[i].nrooms[j].nzombies > 1:
                                        self.edificio.nfloors[x].nrooms[y].nzombies += 1
                                        self.edificio.nfloors[i].nrooms[j].nzombies -= 1
                                        print("Se han propagado zombies del piso "+str(self.edificio.nfloors[i].floorid)+" habitacion "+str(self.edificio.nfloors[i].nrooms[j].roomid)+" hacia "+str(self.edificio.nfloors[x].floorid)+" habitacion "+str(self.edificio.nfloors[x].nrooms[y].roomid))
                                        break

                                if random.random() < 0.3 and self.edificio.nfloors[x].nrooms[y].bloqueo != True: # 30% de que los zombies se trasladen de una habitacion a otra
                                    self.edificio.nfloors[x].nrooms[y].nzombies += self.edificio.nfloors[i].nrooms[j].nzombies
                                    self.edificio.nfloors[i].nrooms[j].nzombies = 0
                                    print("Los zombies se han trasladado al piso "+str(self.edificio.nfloors[x].floorid)+" habitacion "+str(self.edificio.nfloors[x].nrooms[y].roomid))
                                    break
                                
                                if random.random() < 0.5: # 50% de que los zombies aumenten su poblacion en su respectiva habitacion
                                    self.edificio.nfloors[i].nrooms[j].nzombies += 1
                                    print("A aumentado la poblacion de zombies en el piso "+str(self.edificio.nfloors[i].floorid)+" habitacion "+str(self.edificio.nfloors[i].nrooms[j].roomid))
                                    break
                                
                                print("Los zombies han permanecido en sus respectivas habitaciones")
                                break
                            except:
                                pass
    
    def building_status(self):
        for i in range(len(self.edificio.nfloors)): # Rango de la lista de pisos dentro del edificio
            print("Estado del piso "+str(i))
            for j in range(len(self.edificio.nfloors[i].nrooms)): # Rango de la lista de habitaciones dentro de cada piso
                print("Habitacion numero "+str(j) +", Sensor: "+ str(self.edificio.nfloors[i].nrooms[j].room_status())+", Zombies: "+str(self.edificio.nfloors[i].nrooms[j].nzombies)+", Bloqueo: "+str(self.edificio.nfloors[i].nrooms[j].bloqueo))
            pause()
            clear()

def pause():
    programPause = input("Presione intro para continuar...")

def clear():
    os.system('cls')

def menu_principal():
    simulation = Simulation()
    turno = 0
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
        print("6. Desbloquear habitacion")
        print("0. Salir")
        try:
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
                    print("Turno "+str(turno))
                    try:
                        if simulation.infection == False:
                            print(simulation.initial_infection())
                        else:
                            simulation.infeccion_continua()
                        turno += 1
                        pause()
                        clear()
                    except IndexError:
                        print("Ingrese la configuracion del edificio antes de interactuar con esta opcion")
                        pause()
                        clear()
                case 4:
                    try:
                        floor_to_clean = int(input("Ingrese el piso: "))
                        clear()
                        room_to_clean = int(input("Ingrese la habitacion: "))
                        clear()
                        if simulation.edificio.nfloors[floor_to_clean].nrooms[room_to_clean].nzombies > 0:
                            simulation.edificio.nfloors[floor_to_clean].nrooms[room_to_clean].nzombies = 0
                            print("La habitacion "+str(simulation.edificio.nfloors[floor_to_clean].nrooms[room_to_clean].roomid)+ " del piso "+str(simulation.edificio.nfloors[floor_to_clean].floorid)+" se ha limpiado correctamente")
                        else:
                            print("La habitacion no tiene zombies")
                        pause()
                        clear()
                    except:
                        print("Habitacion inexistente")
                case 5:
                    try:
                        floor_to_lock = int(input("Ingrese el piso: "))
                        clear()
                        room_to_lock = int(input("Ingrese la habitacion: "))
                        clear()
                        if simulation.edificio.nfloors[floor_to_lock].nrooms[room_to_lock].bloqueo == False:
                            simulation.edificio.nfloors[floor_to_lock].nrooms[room_to_lock].bloqueo = True
                            print("La habitacion "+str(simulation.edificio.nfloors[floor_to_lock].nrooms[room_to_lock].roomid)+ " del piso "+str(simulation.edificio.nfloors[floor_to_lock].floorid)+" se ha bloqueado correctamente")
                        else:
                            print("La habitacion ya se encuentra bloqueada")
                        pause()
                        clear()
                    except:
                        print("Habitacion inexistente")
                case 6:
                    try:
                        floor_to_unlock = int(input("Ingrese el piso: "))
                        clear()
                        room_to_unlock = int(input("Ingrese la habitacion: "))
                        clear()
                        if simulation.edificio.nfloors[floor_to_unlock].nrooms[room_to_unlock].bloqueo == True:
                            simulation.edificio.nfloors[floor_to_unlock].nrooms[room_to_unlock].bloqueo = False
                            print("La habitacion "+str(simulation.edificio.nfloors[floor_to_unlock].nrooms[room_to_unlock].roomid)+ " del piso "+str(simulation.edificio.nfloors[floor_to_unlock].floorid)+" se ha desbloqueado correctamente")
                        else:
                            print("La habitacion ya se encuentra desbloqueada")
                        pause()
                        clear()
                    except:
                        print("Habitacion inexistente")
        except:
            clear()
            
menu_principal()
    