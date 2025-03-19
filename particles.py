import pygame
import constants

class Particle():

    def __init__(self, x:float, y:float, charge:float, color:int):
        
        self.position:list[float] = [x,y]
        self.velocity:list[float]  = [0, 0]
        
        self.charge:float = charge
        
        mass:float = constants.NEUTRON_MASS
        
        if color == 0:
            mass = constants.ELECTRON_MASS
            radius = constants.ELECTRON_RADIUS
        elif color == 1:
            mass = constants.PROTON_MASS
            radius = constants.PROTON_RADIUS

        elif color == 2:
            mass = constants.NEUTRON_MASS
            radius = constants.NEUTRON_RADIUS
        elif color == 3:
            mass = constants.EXTRA_MASS
            radius = constants.EXTRA_RADIUS

        self.radius = radius

        self.mass = mass
        
        self.color = constants.PARTICLE_COLORS[color]

        alive.append(self)
        

alive:list[Particle] = []

def getAlive() -> list[Particle]:
    return alive
